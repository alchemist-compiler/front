# Transmuter front-end, front-end libraries and utilities for the
# Transmuter language processing infrastructure
# Copyright (C) 2024  Natan Junges <natanajunges@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from ..common import TransmuterCondition
from ..lexical import TransmuterTerminalTag, TransmuterLexer
from .common import lexical, syntactic


class Whitespace(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {1, 2, 3}

    @staticmethod
    def ignore(conditions: set[type[TransmuterCondition]]) -> bool:
        return True


class Identifier(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {4}


class Colon(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {6}


class Semicolon(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {7}


class CommercialAt(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {8}


class LeftParenthesis(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {9}


class RightParenthesis(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {10}


class GreaterThanSign(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {11}

        return set()


class VerticalLine(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {12}


class Solidus(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {13}

        return set()


class DoubleVerticalLine(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {14}


class Comma(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {16}


class DoubleAmpersand(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {17}


class Ignore(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {19}

        return set()


class Optional(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {25}

        return set()


class Start(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {33}

        return set()


class Asterisk(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {38}

        return set()


class PlusSign(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {39}

        return set()


class QuestionMark(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {40}

        return set()


class ExpressionRange(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {41}

        return set()


class LeftCurlyBracket(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {50}

        return set()


class LeftCurlyBracketSolidus(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {51}

        return set()


class RightCurlyBracket(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {53}

        return set()


class OrdChar(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {54}

        return set()


class QuotedChar(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {55}

        return set()


class FullStop(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {60}

        return set()


class BracketExpression(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if lexical in conditions:
            return {61}

        return set()


class ExclamationMark(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        return {93}


class LeftSquareBracket(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {94}

        return set()


class LeftSquareBracketSolidus(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {95}

        return set()


class RightSquareBracket(TransmuterTerminalTag):
    @staticmethod
    def states_start(conditions: set[type[TransmuterCondition]]) -> set[int]:
        if syntactic in conditions:
            return {97}

        return set()


class Lexer(TransmuterLexer):
    TERMINAL_TAGS = {Whitespace, Identifier, Colon, Semicolon, CommercialAt, LeftParenthesis, RightParenthesis, GreaterThanSign, VerticalLine, Solidus, DoubleVerticalLine, Comma, DoubleAmpersand, Ignore, Optional, Start, Asterisk, PlusSign, QuestionMark, ExpressionRange, LeftCurlyBracket, LeftCurlyBracketSolidus, RightCurlyBracket, OrdChar, QuotedChar, FullStop, BracketExpression, ExclamationMark, LeftSquareBracket, LeftSquareBracketSolidus, RightSquareBracket}

    def nfa(self, char: str, current_states: set[int]) -> tuple[set[type[TransmuterTerminalTag]], set[int]]:
        current_terminal_tags = set()
        next_states = set()

        # Whitespace
        # 1:21
        if 1 in current_states and (char in {"\t", " "}):
            current_terminal_tags |= {Whitespace}
            next_states |= {self.STATE_ACCEPT, 1}

        # 1:30
        if 2 in current_states and (char == "\r"):
            next_states |= {3}

        # 1:34
        if 3 in current_states and (char == "\n"):
            current_terminal_tags |= {Whitespace}
            next_states |= {self.STATE_ACCEPT}

        # Identifier
        # 3:22
        if 4 in current_states and ("A" <= char <= "Z" or char == "_" or "a" <= char <= "z"):
            current_terminal_tags |= {Identifier, OrdChar}
            next_states |= {self.STATE_ACCEPT, 5}

        # 3:32
        if 5 in current_states and ("0" <= char <= "9" or "A" <= char <= "Z" or char == "_" or "a" <= char <= "z"):
            current_terminal_tags |= {Identifier, OrdChar}
            next_states |= {self.STATE_ACCEPT, 5}

        # Colon
        # 5:17
        if 6 in current_states and (char == ":"):
            current_terminal_tags |= {Colon, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # Semicolon
        # 7:12
        if 7 in current_states and (char == ";"):
            current_terminal_tags |= {Semicolon}
            next_states |= {self.STATE_ACCEPT}

        # CommercialAt
        # 9:24
        if 8 in current_states and (char == "@"):
            current_terminal_tags |= {CommercialAt, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # LeftParenthesis
        # 11:18
        if 9 in current_states and (char == "("):
            current_terminal_tags |= {LeftParenthesis}
            next_states |= {self.STATE_ACCEPT}

        # RightParenthesis
        # 13:19
        if 10 in current_states and (char == ")"):
            current_terminal_tags |= {RightParenthesis}
            next_states |= {self.STATE_ACCEPT}

        # GreaterThanSign
        # 15:35
        if 11 in current_states and (char == ">"):
            current_terminal_tags |= {GreaterThanSign, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # VerticalLine
        # 17:15
        if 12 in current_states and (char == "|"):
            current_terminal_tags |= {VerticalLine}
            next_states |= {self.STATE_ACCEPT}

        # Solidus
        # 19:20
        if 13 in current_states and (char == "/"):
            current_terminal_tags |= {Solidus}
            next_states |= {self.STATE_ACCEPT}

        # DoubleVerticalLine
        # 21:30
        if 14 in current_states and (char == "|"):
            next_states |= {15}

        # 21:31
        if 15 in current_states and (char == "|"):
            current_terminal_tags |= {DoubleVerticalLine, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # Comma
        # 23:17
        if 16 in current_states and (char == ","):
            current_terminal_tags |= {Comma, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # DoubleAmpersand
        # 25:27
        if 17 in current_states and (char == "&"):
            next_states |= {18}

        # 25:28
        if 18 in current_states and (char == "&"):
            current_terminal_tags |= {DoubleAmpersand, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # Ignore
        # 27:39
        if 19 in current_states and (char == "i"):
            next_states |= {20}

        # 27:40
        if 20 in current_states and (char == "g"):
            next_states |= {21}

        # 27:41
        if 21 in current_states and (char == "n"):
            next_states |= {22}

        # 27:42
        if 22 in current_states and (char == "o"):
            next_states |= {23}

        # 27:43
        if 23 in current_states and (char == "r"):
            next_states |= {24}

        # 27:44
        if 24 in current_states and (char == "e"):
            current_terminal_tags |= {Ignore, OrdChar}
            current_terminal_tags -= {Identifier}
            next_states |= {self.STATE_ACCEPT}

        # Optional
        # 29:41
        if 25 in current_states and (char == "o"):
            next_states |= {26}

        # 29:42
        if 26 in current_states and (char == "p"):
            next_states |= {27}

        # 29:43
        if 27 in current_states and (char == "t"):
            next_states |= {28}

        # 29:44
        if 28 in current_states and (char == "i"):
            next_states |= {29}

        # 29:45
        if 29 in current_states and (char == "o"):
            next_states |= {30}

        # 29:46
        if 30 in current_states and (char == "n"):
            next_states |= {31}

        # 29:47
        if 31 in current_states and (char == "a"):
            next_states |= {32}

        # 29:48
        if 32 in current_states and (char == "l"):
            current_terminal_tags |= {Optional, OrdChar}
            current_terminal_tags -= {Identifier}
            next_states |= {self.STATE_ACCEPT}

        # Start
        # 31:31
        if 33 in current_states and (char == "s"):
            next_states |= {34}

        # 31:32
        if 34 in current_states and (char == "t"):
            next_states |= {35}

        # 31:33
        if 35 in current_states and (char == "a"):
            next_states |= {36}

        # 31:34
        if 36 in current_states and (char == "r"):
            next_states |= {37}

        # 31:35
        if 37 in current_states and (char == "t"):
            current_terminal_tags |= {Start}
            current_terminal_tags -= {Identifier}
            next_states |= {self.STATE_ACCEPT}

        # Asterisk
        # 33:19
        if 38 in current_states and (char == "*"):
            current_terminal_tags |= {Asterisk}
            next_states |= {self.STATE_ACCEPT}

        # PlusSign
        # 35:19
        if 39 in current_states and (char == "+"):
            current_terminal_tags |= {PlusSign}
            next_states |= {self.STATE_ACCEPT}

        # QuestionMark
        # 37:23
        if 40 in current_states and (char == "?"):
            current_terminal_tags |= {QuestionMark}
            next_states |= {self.STATE_ACCEPT}

        # ExpressionRange
        # 39:26
        if 41 in current_states and (char == "{"):
            next_states |= {42, 43}

        # 39:30
        if 42 in current_states and (char == "0"):
            next_states |= {45, 49}

        # 39:34
        if 43 in current_states and ("1" <= char <= "9"):
            next_states |= {44, 45, 49}

        # 39:40
        if 44 in current_states and ("0" <= char <= "9"):
            next_states |= {44, 45, 49}

        # 39:49
        if 45 in current_states and (char == ","):
            next_states |= {46, 47, 49}

        # 39:52
        if 46 in current_states and (char == "0"):
            next_states |= {49}

        # 39:56
        if 47 in current_states and ("1" <= char <= "9"):
            next_states |= {48, 49}

        # 39:62
        if 48 in current_states and ("0" <= char <= "9"):
            next_states |= {48, 49}

        # 39:73
        if 49 in current_states and (char == "}"):
            current_terminal_tags |= {ExpressionRange}
            next_states |= {self.STATE_ACCEPT}

        # LeftCurlyBracket
        # 41:29
        if 50 in current_states and (char == "{"):
            current_terminal_tags |= {LeftCurlyBracket}
            next_states |= {self.STATE_ACCEPT}

        # LeftCurlyBracketSolidus
        # 43:36
        if 51 in current_states and (char == "{"):
            next_states |= {52}

        # 43:39
        if 52 in current_states and (char == "/"):
            current_terminal_tags |= {LeftCurlyBracketSolidus}
            next_states |= {self.STATE_ACCEPT}

        # RightCurlyBracket
        # 45:30
        if 53 in current_states and (char == "}"):
            current_terminal_tags |= {RightCurlyBracket}
            next_states |= {self.STATE_ACCEPT}

        # OrdChar
        # 47:18
        if 54 in current_states and not current_terminal_tags & {Identifier, Colon, CommercialAt, GreaterThanSign, DoubleVerticalLine, Comma, DoubleAmpersand, Ignore, Optional} and (not ("\000" <= char <= "\037" or char in {" ", "$", "(", ")", "*", "+", ".", ";", "?", "[", "\\", "^", "{", "|", "\177"})):
            current_terminal_tags |= {OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # QuotedChar
        # 49:21
        if 55 in current_states and (char == "\\"):
            next_states |= {56, 57}

        # 49:25
        if 56 in current_states and (char in {" ", "$", "(", ")", "*", "+", ".", ";", "?", "[", "\\", "^", "a", "b", "f", "n", "r", "t", "v", "{", "|"}):
            current_terminal_tags |= {QuotedChar}
            next_states |= {self.STATE_ACCEPT}

        # 49:52
        if 57 in current_states and (char in {"0", "1"}):
            next_states |= {58}

        # 49:57:1
        if 58 in current_states and ("0" <= char <= "7"):
            next_states |= {59}

        # 49:57:2
        if 59 in current_states and ("0" <= char <= "7"):
            current_terminal_tags |= {QuotedChar}
            next_states |= {self.STATE_ACCEPT}

        # FullStop
        # 51:19
        if 60 in current_states and (char == "."):
            current_terminal_tags |= {FullStop}
            next_states |= {self.STATE_ACCEPT}

        # BracketExpression
        # 53:28
        if 61 in current_states and (char == "["):
            next_states |= {62, 63, 64, 69}

        # 53:32
        if 62 in current_states and (char == "^"):
            next_states |= {63, 64}

        # 53:37
        if 63 in current_states and (not ("\000" <= char <= "\037" or char in {"\\", "^", "\177"})):
            next_states |= {71, 78, 79, 91, 92}

        # 53:59
        if 64 in current_states and (char == "\\"):
            next_states |= {65, 66}

        # 53:63
        if 65 in current_states and (char in {"\\", "a", "b", "f", "n", "r", "t", "v"}):
            next_states |= {71, 78, 79, 91, 92}

        # 53:77
        if 66 in current_states and (char in {"0", "1"}):
            next_states |= {67}

        # 53:82:1
        if 67 in current_states and ("0" <= char <= "7"):
            next_states |= {68}

        # 53:82:2
        if 68 in current_states and ("0" <= char <= "7"):
            next_states |= {71, 78, 79, 91, 92}

        # 53:95
        if 69 in current_states and (char == "^"):
            next_states |= {70}

        # 53:98
        if 70 in current_states and (char == "^"):
            next_states |= {71, 78, 79, 91, 92}

        # 53:103
        if 71 in current_states and (char == "-"):
            next_states |= {72, 73}

        # 53:106
        if 72 in current_states and (not (char == "]" or "\000" <= char <= "\037" or char in {"\\", "\177"})):
            next_states |= {78, 79, 91, 92}

        # 53:128
        if 73 in current_states and (char == "\\"):
            next_states |= {74, 75}

        # 53:132
        if 74 in current_states and (char in {"\\", "a", "b", "f", "n", "r", "t", "v"}):
            next_states |= {78, 79, 91, 92}

        # 53:146
        if 75 in current_states and (char in {"0", "1"}):
            next_states |= {76}

        # 53:151:1
        if 76 in current_states and ("0" <= char <= "7"):
            next_states |= {77}

        # 53:151:2
        if 77 in current_states and ("0" <= char <= "7"):
            next_states |= {78, 79, 91, 92}

        # 53:166
        if 78 in current_states and (not (char == "]" or "\000" <= char <= "\037" or char in {"\\", "\177", "-"})):
            next_states |= {78, 79, 84, 91, 92}

        # 53:189
        if 79 in current_states and (char == "\\"):
            next_states |= {80, 81}

        # 53:193
        if 80 in current_states and (char in {"\\", "a", "b", "f", "n", "r", "t", "v"}):
            next_states |= {78, 79, 84, 91, 92}

        # 53:207
        if 81 in current_states and (char in {"0", "1"}):
            next_states |= {82}

        # 53:212:1
        if 82 in current_states and ("0" <= char <= "7"):
            next_states |= {83}

        # 53:212:2
        if 83 in current_states and ("0" <= char <= "7"):
            next_states |= {78, 79, 84, 91, 92}

        # 53:224
        if 84 in current_states and (char == "-"):
            next_states |= {85, 86}

        # 53:227
        if 85 in current_states and (not (char == "]" or "\000" <= char <= "\037" or char in {"\\", "\177"})):
            next_states |= {78, 79, 91, 92}

        # 53:249
        if 86 in current_states and (char == "\\"):
            next_states |= {87, 88}

        # 53:253
        if 87 in current_states and (char in {"\\", "a", "b", "f", "n", "r", "t", "v"}):
            next_states |= {78, 79, 91, 92}

        # 53:267
        if 88 in current_states and (char in {"0", "1"}):
            next_states |= {89}

        # 53:272:1
        if 89 in current_states and ("0" <= char <= "7"):
            next_states |= {90}

        # 53:272:2
        if 90 in current_states and ("0" <= char <= "7"):
            next_states |= {78, 79, 91, 92}

        # 53:287
        if 91 in current_states and (char == "-"):
            next_states |= {92}

        # 53:290
        if 92 in current_states and (char == "]"):
            current_terminal_tags |= {BracketExpression}
            next_states |= {self.STATE_ACCEPT}

        # ExclamationMark
        # 55:27
        if 93 in current_states and (char == "!"):
            current_terminal_tags |= {ExclamationMark, OrdChar}
            next_states |= {self.STATE_ACCEPT}

        # LeftSquareBracket
        # 57:30
        if 94 in current_states and (char == "["):
            current_terminal_tags |= {LeftSquareBracket}
            next_states |= {self.STATE_ACCEPT}

        # LeftSquareBracketSolidus
        # 59:37
        if 95 in current_states and (char == "["):
            next_states |= {96}

        # 59:40
        if 96 in current_states and (char == "/"):
            current_terminal_tags |= {LeftSquareBracketSolidus}
            next_states |= {self.STATE_ACCEPT}

        # RightSquareBracket
        # 61:31
        if 97 in current_states and (char == "]"):
            current_terminal_tags |= {RightSquareBracket}
            next_states |= {self.STATE_ACCEPT}

        return (current_terminal_tags, next_states)
