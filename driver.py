"""A driver to create patterns from a given letter function.

NOTE: DO NOT alter this file in any way.
"""
import re
import sys
import textwrap

# Note: Callable and List are deprecated as of Python 3.9.
# collections.abc.Callable and list support generics
from typing import Callable, List, TextIO

ILLEGAL_RE = re.compile("[^A-Z\n]")


def validate_strings(strings: List[str], illegal: re.Pattern) -> None:
    """Verifies each string does not contain any illegal characters.

    Args:
        strings: a list of strings
        illegal: a compiled regular expression to match illegal
            characters.

    Raises:
        ValueError: If an illegal character is present.
    """
    for row, string in enumerate(strings):
        match = illegal.search(string)
        if match:
            raise ValueError("Unsupported character {!r} in row {}".format(
                match.group(), row))


def read_pattern(in_stream: TextIO = sys.stdin) -> List[List[str]]:
    """Reads in the pattern from stdin.

    Args:
        in_stream: The input stream from which to read.  Defaults to
            stdin.

    Returns: The pattern as a list of lists.
    """
    lines = list(in_stream)

    # Validate before stripping to catch leading/trailing spaces.
    validate_strings(lines, ILLEGAL_RE)
    return [list(line.strip()) for line in lines]


def build_pattern(expected_pattern: List[List[str]],
                  letter: Callable[[int, int], str]) -> List[List[str]]:
    """Computes a pattern by calling the provided function.

    The function is called on each row/col.

    Args:
        expected_pattern: The pattern that is expected.  It provides the
            dimensions to use.
        letter: The function used to compute what letter goes at each
            entry in the generated pattern.

    Returns: The resulting pattern.

    Raises:
        TypeError: If the letter function returns anything other than a
            string of length 1.
    """
    pattern = []

    for row_number, row in enumerate(expected_pattern):
        pattern_row = []

        for col_number in range(len(row)):
            ch = letter(row_number, col_number)

            if not isinstance(ch, str):
                raise TypeError(
                    'letter({}, {}) returned {}, a string of length 1 was '
                    'expected'.format(
                        row_number, col_number, type(ch).__name__))
            elif len(ch) > 1:
                raise TypeError(
                    'letter({}, {}) returned a string of length {}, a string '
                    'of length 1 was expected'.format(
                        row_number, col_number, len(ch)))

            pattern_row.append(ch)

        pattern.append(pattern_row)

    return pattern


def print_difference(
        expected: List[List[str]], computed: List[List[str]]) -> None:
    """Prints the difference between the expected and computed patterns.

    The expected pattern is printed on the left and the computed pattern
    is printed on the right with:
    * Any non A-Z characters replaced with a '?'
    * incorrect letters replaced with the lower-case equivalent

    Args:
        expected: The expected pattern
        computed: The computed pattern
    """
    out_string = '{{:{}}}'.format(max(map(len, expected)))

    for row_number, expected_row in enumerate(expected):
        # row of expected pattern
        print(out_string.format(''.join(expected_row)), end='')

        # separation
        print('     ', end='')

        # row of computed pattern
        difference = []
        for col_number, ch in enumerate(computed[row_number]):
            if not ch.isupper():
                difference.append('?')
            elif expected_row[col_number] != ch:
                difference.append(computed[row_number][col_number].lower())
            else:
                difference.append(ch)

        print(''.join(difference))


def display_results(
        expected: List[List[str]], computed: List[List[str]]) -> None:
    """Checks if the expected pattern matches the computed pattern.

    If they match, this function displays a success message.  If they
    differ, displays the difference between the patterns.

    Args:
        expected: The expected pattern
        computed: The computed pattern
    """
    print()

    if expected == computed:
        print("Well done - your logic produced the specified pattern!")
    else:
        # Doesn't match :-(
        paragraphs = [
            "Not done yet - your logic did not produce the specified pattern.",
            "Below you see the expected pattern on the left and your pattern "
            "on the right.  Any '?' characters indicate that your code "
            "returned an unexpected character.  Any lower case letters "
            "indicate that your code returned the upper-case equivalent but "
            "it did not match the specified pattern.",
            "Fix your logic and test again!"
        ]

        for paragraph in paragraphs:
            print(textwrap.fill(paragraph), end='\n\n')

        print_difference(expected, computed)

    print()


def compare_patterns(letter: Callable[[int, int], str]) -> None:
    """Reads a pattern for standard input, computes a corresponding
    pattern using the provided function, and displays the results of
    comparison between the patterns.

    Args:
        letter: The function used to compute what letter goes at each
            entry in the generated pattern.
    """
    expected_pattern = read_pattern()
    computed_pattern = build_pattern(expected_pattern, letter)
    display_results(expected_pattern, computed_pattern)
