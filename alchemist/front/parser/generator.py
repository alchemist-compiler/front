# This file is part of the Alchemist front-end libraries
# Copyright (C) 2023  Natan Junges <natanajunges@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# The code generated by this library is also under the GNU General Public
# License.

from typing import Union, TypeVar, Generic

_RuleTemplate = Union["_RuleTemplates", "_Rule", str]
_RuleTemplates = tuple[_RuleTemplate, ...] | list[_RuleTemplate]
_T = TypeVar("_T", list["_Rule"], "_Group", str)


class _Rule(Generic[_T]):
    @staticmethod
    def get(template: _RuleTemplate) -> "_Rule":
        if isinstance(template, tuple):
            return _Group(template)

        if isinstance(template, list):
            return _Optional(template)

        if isinstance(template, str):
            return _Term(template)

        return template

    @staticmethod
    def _filter(templates: _RuleTemplates) -> list["_Rule"]:
        rules = [
            _Rule.get(template) for template in templates
            if not isinstance(template, Switch) or template.enabled
        ]
        rules = [
            rule for rule in rules
            if isinstance(rule, _Term) or len(
                rule.rules.rules
                if isinstance(rule.rules, _Group)
                else rule.rules
            ) > 0
        ]
        return rules

    def __init__(self, rules: _T):
        self.rules: _T = rules

    def __call__(self, indent: int, level: int) -> str:
        raise NotImplementedError()


class _Group(_Rule[list[_Rule]]):
    def __init__(self, templates: _RuleTemplates):
        super().__init__(self._filter(templates))
        i = 0

        while i < len(self.rules):
            if isinstance(self.rules[i], _Group):
                rules = self.rules[i].rules
                self.rules = self.rules[:i] + rules + self.rules[i + 1:]
                i += len(rules)
            else:
                i += 1

    def __call__(self, indent: int, level: int) -> str:
        code = ""

        for rule in self.rules:
            code += rule(indent, level)

        return code


class _Optional(_Rule[_Group]):
    def __init__(self, templates: list[_RuleTemplate]):
        super().__init__(_Group(templates))

        if len(self.rules.rules) == 1 and isinstance(
            self.rules.rules[0], _Optional
        ):
            self.rules = self.rules.rules[0].rules

    def __call__(self, indent: int, level: int) -> str:
        code = "\n"
        code += f"\n{'    ' * indent}try:  # optional"
        code += f"\n{'    ' * (indent + 1)}paths{level + 1} = paths{level}"
        code += self.rules(indent + 1, level + 1)
        code += f"\n{'    ' * (indent + 1)}paths{level} |= paths{level + 1}"
        code += f"\n{'    ' * indent}except (CompilerSyntaxError, CompilerEOIError):"  # noqa: E501
        code += f"\n{'    ' * (indent + 1)}pass"
        code += "\n"
        return code


class Switch(_Rule[_Group]):
    enabled: bool = False

    def __init__(self, *templates: _RuleTemplate):
        if self.enabled:
            super().__init__(_Group(templates))

    def __call__(self, indent: int, level: int) -> str:
        return self.rules(indent, level)


class repeat(_Rule[_Group]):  # pylint: disable=C0103
    def __init__(self, *templates: _RuleTemplate):
        super().__init__(_Group(templates))

        if len(self.rules.rules) == 1 and isinstance(
            self.rules.rules[0], repeat
        ):
            self.rules = self.rules.rules[0].rules

    def __call__(self, indent: int, level: int) -> str:
        code = "\n"
        code += f"\n{'    ' * indent}# begin repeat"
        code += f"\n{'    ' * indent}paths{level + 1} = paths{level}"
        code += "\n"
        code += f"\n{'    ' * indent}while True:"
        code += f"\n{'    ' * (indent + 1)}try:"
        code += self.rules(indent + 2, level + 1)
        code += f"\n{'    ' * (indent + 2)}paths{level} |= paths{level + 1}"
        # pylint: disable-next=C0301
        code += f"\n{'    ' * (indent + 1)}except (CompilerSyntaxError, CompilerEOIError):"  # noqa: E501
        code += f"\n{'    ' * (indent + 2)}break"
        code += "\n"
        code += f"\n{'    ' * indent}# end repeat"
        code += "\n"
        return code


class oneof(_Rule[list[_Rule]]):  # pylint: disable=C0103
    def __init__(self, *templates: _RuleTemplate):
        super().__init__(self._filter(templates))
        i = 0

        while i < len(self.rules):
            if isinstance(self.rules[i], oneof):
                rules = self.rules[i].rules
                self.rules = self.rules[:i] + rules + self.rules[i + 1:]
                i += len(rules)
            else:
                i += 1

    def __call__(self, indent: int, level: int) -> str:
        if len(self.rules) == 1:
            return self.rules[0](indent, level)

        code = "\n"
        code += f"\n{'    ' * indent}# begin oneof"
        code += f"\n{'    ' * indent}paths{level + 1} = set()"

        for i, rule in enumerate(self.rules):
            code += "\n"
            code += f"\n{'    ' * indent}try:  # option {i + 1}"
            code += f"\n{'    ' * (indent + 1)}paths{level + 2} = paths{level}"
            code += rule(indent + 1, level + 2)
            code += f"\n{'    ' * (indent + 1)}paths{level + 1} |= paths{level + 2}"  # noqa: E501
            code += f"\n{'    ' * indent}except CompilerSyntaxError:"
            code += f"\n{'    ' * (indent + 1)}pass"

        code += "\n"
        code += f"\n{'    ' * indent}if len(paths{level + 1}) == 0:"
        code += f"\n{'    ' * (indent + 1)}raise CompilerSyntaxError(self)"
        code += "\n"
        code += f"\n{'    ' * indent}paths{level} = paths{level + 1}"
        code += f"\n{'    ' * indent}# end oneof"
        code += "\n"
        return code


class _Term(_Rule[str]):
    def __init__(self, node: str):
        super().__init__(node)

    def __call__(self, indent: int, level: int) -> str:
        # pylint: disable-next=C0301
        return f"\n{'    ' * indent}paths{level} = self._process_paths(paths{level}, {self.rules})"  # noqa: E501


class ProductionTemplate:  # pylint: disable=R0903
    _template: _RuleTemplate = ()

    @classmethod
    def generate(cls) -> str:
        # pylint: disable-next=E1101
        if isinstance(cls._template, Switch) and not cls._template.enabled:
            return ""

        rule = _Rule.get(cls._template)

        if (
            not isinstance(rule, _Term)
            and len(
                rule.rules.rules
                if isinstance(rule.rules, _Group)
                else rule.rules
            ) == 0
        ):
            return ""

        code = f"class {cls.__name__}(Production):"
        # pylint: disable-next=C0301
        code += '\n    def __init__(self, parent: Optional[Production], lexer: "Lexer"):'  # noqa: E501
        code += "\n        super().__init__(parent, lexer)"
        code += "\n        paths0 = {lexer.get_state()}"
        code += rule(2, 0).replace("\n\n\n", "\n\n")
        code += '\n        self.paths: set["Terminal"] = paths0'
        return code
