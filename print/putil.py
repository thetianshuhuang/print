
"""Print Configuration and Various Utilities

Attributes
----------
LOG_FILE : str
    If not None, then all print output is saved to this file. Colors are not
    rendered.
"""

from itertools import zip_longest


LOG_FILE = None


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
