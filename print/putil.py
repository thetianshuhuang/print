
"""Print Configuration and Various Utilities"""

import re

from itertools import zip_longest
from shutil import get_terminal_size

from .print import render


def clear_fmt(s):
    """Clear ANSI formatting from a string"""

    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)


def join(*args):
    """Join multi-line strings line-by-line, and pad with the appropriate
    number of spaces needed to preserve alignment
    """

    # Split
    args = [arg.split('\n') for arg in args]

    # Get widths and height
    widths = [max([len(s) for s in arg]) for arg in args]
    height = max(len(arg) for arg in args)

    output = [''] * height
    for width, arg in zip(widths, args):
        output = [
            out + (row + ' ' * (width - len(row)))
            for out, row in zip_longest(output, arg, fillvalue='')]

    return '\n'.join(output)


def span(left, right, *args, width=get_terminal_size().columns, char=' '):
    """Set up left and right alignment

    Parameters
    ----------
    left : str
        Left string; to be left aligned
    right : str
        Right string; to be right aligned
    *args : list
        Additional arguments to render the span with

    Keyword Args
    ------------
    width : int
        Width of the span; defaults to terminal width
    char : str
        Character to fill the span with; defaults to ' '
    """

    slen = width - len(clear_fmt(left)) - len(clear_fmt(right))
    return left + render(char * slen, *args) + right


def pad(string, *args, width=get_terminal_size().columns, char=' '):
    """Pad a possibly multi-line string to the desired width"""

    return '\n'.join([
        span(s, '', *args, width=width, char=char)
        for s in string.split('\n')
    ])


def number(
        entries, left_args=[], right_args=[], margin=6,
        width=get_terminal_size().columns, height=get_terminal_size().lines):
    """Render a list with line numbers

    Parameters
    ----------
    entries : str[]
        List of entries to print

    Keyword Args
    ------------
    left_args : list
        Arguments for line number render
    right_args : list
        Arguments for line entry render
    margin : int
        Line number margin size
    width : int
        Width of desired window
    height : int
        Height of desired window

    Returns
    -------
    str
        Rendered string
    """

    ret = ''
    width = width - margin - 1

    idx = 0
    row = 0
    while row < height:

        # Entries remaining
        if idx < len(entries):
            s = str(entries[idx])

            # First row
            ret += render(pad(' ' + str(idx + 1), width=margin), *left_args)
            ret += render(pad(' ' + s[:width], width=width), *right_args)
            ret += '\n'
            row += 1

            # Subsequent rows (no new line numbers)
            while len(s) > width and row < height:
                s = s[width:]

                ret += render(' ' * margin, *left_args)
                ret += render(' ' + s[:width], *right_args)
                ret += '\n'
                row += 1

            idx += 1

        # No entries remaining
        else:
            ret += render(' ' * margin, *left_args)
            ret += render(' ' + ' ' * width, *right_args)
            ret += '\n'
            row += 1

    return ret
