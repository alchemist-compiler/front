# Transmuter front-end

Front-end libraries and utilities for the Transmuter language processing infrastructure.

## Features

- Aether - a self-declared and self-implemented language declaration language
- Conditional declaration of language features

### Lexical Analyzer

- POSIX ERE-based language
- NFA-based implementation
- `O(n)` complexity
- Ignorable tokens (for eg. comments, newlines and whitespaces)
- On-demand and memoized tokenization
- Longest match tokenization
    - Ambiguous generalization as workaround
- Ambiguous tokenization
    - Precedence-based disambiguation

### Syntactic Analyzer

- Generalized CFG-based language (including ambiguities and left-recursion)
- Recursive Descent-based implementation (using backtracking instead of lookahead)
    - Memoized parsing
- `O(n^3)` complexity
- Recursive Ascent-based left-recursion implementation
    - Iteration-based alternative to (left-)recursion
- `SPACE(n^3)` ambiguous BSR-based output
    - Ordered choice and longest match-based disambiguation
- Syntax sugar for optionals and expression grouping

### Semantic Analyzer

- Dual BSR / Syntax Tree APIs
    - Visitors and transformers
    - BSR <-> Syntax Tree converters
- Symbol Table

## References
- FROST, R. A.; HAFIZ, R.; CALLAGHAN, P. C. **Modular and efficient top-down parsing for ambiguous left-recursive grammars**. Proceedings of the 10th International Conference on Parsing Technologies - IWPT ’07. Morristown, NJ, USA: Association for Computational Linguistics, 2007. Available at: https://doi.org/10.3115/1621410.1621425.
- COX, R. **Regular expression matching can be simple and fast**, 2007. Available at: https://swtch.com/~rsc/regexp/regexp1.html.
- SCOTT, E.; JOHNSTONE, A. GLL Parsing. **Electronic Notes in Theoretical Computer Science**, v. 253, n. 7, p. 177–189, 2010. Available at: https://doi.org/10.1016/j.entcs.2010.08.041.
- SCOTT, E.; JOHNSTONE, A.; VAN BINSBERGEN, L. T. Derivation representation using binary subtree sets. **Science of Computer Programming**, v. 175, p. 63–84, 2019. Available at: https://doi.org/10.1016/j.scico.2019.01.008.
- THE IEEE AND THE OPEN GROUP. Regular Expressions. In: __________. **The Open Group Base Specifications, Issue 8**, v. 1, c. 9, 2024. Available at: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap09.html.
