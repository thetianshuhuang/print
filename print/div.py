
"""Various visual dividers"""


import shutil
from .print import print


def hfill(s, sequence):
    """Pad a string s with a sequence to fill the terminal horizontally."""

    width = shutil.get_terminal_size().columns
    return (s + sequence * ((width - len(s)) // len(sequence)))


def center(s):
    """Return a centered string"""

    width = shutil.get_terminal_size().columns
    return ' ' * ((width - len(s)) // 2) + s


def drender(style, s=''):

    if len(style) == 1:
        if s == '':
            return hfill('', style)
        else:
            return hfill(style * 2 + ' ' + s + ' ', style)

    elif style[0] == style[-1]:
        return (
            hfill('', style[0]) + '\n' * (len(style) - 2) +
            center(s) +
            '\n' * (len(style) - 1) + hfill('', style[0]))

    else:
        return """Style not recognized. Available styles:
> '-', '=', or any other single character sequence
> '- -', '=  =', or any other repeated character with n>=0 separating spaces
    """


def div(style, *args, s=''):
    """Print a divider in the set style"""

    print(drender(style, s=s), *args)
