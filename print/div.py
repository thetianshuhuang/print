
"""Various visual dividers"""


import shutil
import os
from .print import print


def hfill(s, sequence):
    """Pad a string s with a sequence to fill the terminal horizontally."""

    width = shutil.get_terminal_size().columns
    return (s + sequence * ((width - len(s)) // len(sequence)))


def center(s):
    """Return a centered string"""

    width = shutil.get_terminal_size().columns
    return ' ' * ((width - len(s)) // 2) + s


def drender(style, label=''):

    if len(style) == 1:
        if label == '':
            return hfill('', style)
        else:
            return hfill(style * 2 + ' ' + label + ' ', style)

    elif style[0] == style[-1]:
        # Windows does line wrapping weird
        sp_left = '\n' * (len(style) - (2 if os.name == 'nt' else 1))
        sp_right = '\n' * (len(style) - 1)
        return (
            hfill('', style[0]) + sp_left +
            center(label) +
            sp_right + hfill('', style[0]))

    else:
        return """Style not recognized. Available styles:
> '-', '=', or any other single character sequence
> '- -', '=  =', or any other repeated character with n>=0 separating spaces
    """


def div(style, *args, label=''):
    """Print a divider in the set style"""

    print(drender(style, label=label), *args)
