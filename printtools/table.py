"""Table Rendering."""

from .print import print
from .putil import clear_fmt


def __get_widths(t):
    """Get column widths."""
    widths = [0 for _ in t[0]]
    for row in t:
        widths = [
            max(widths[i], len(clear_fmt(cell)))
            for i, cell in enumerate(row)]

    return widths


def __table_standard(t, padding=' ', indent='', hline=True, heading=False):
    """Print table with vertical dividers."""
    t = [[padding + cell + padding for cell in row] for row in t]

    widths = __get_widths(t)

    # Make horizontal divider
    hdiv = "{indent}+{content}+\n".format(
        indent=indent,
        content='+'.join(['-' * width for width in widths]))

    tout = ''
    if hline:
        tout += hdiv

    for i, row in enumerate(t):
        row_contents = [
            cell + ' ' * (width - len(clear_fmt(cell)))
            for width, cell in zip(widths, row)]
        tout += indent + "|" + "|".join(row_contents) + "|\n"
        if hline or (heading and i == 1):
            tout += hdiv

    return tout


def __table_nosep(t, indent='', spacing='  ', hline=False, heading=False):
    """Table with no vertical dividers."""
    widths = __get_widths(t)
    hdiv = "-" * (sum(widths) + len(spacing) * (len(widths) - 1)) + "\n"

    tout = ''
    if hline:
        tout = hdiv

    for i, row in enumerate(t):
        row_contents = [
            cell + ' ' * (width - len(clear_fmt(cell)))
            for width, cell in zip(widths, row)]
        tout += indent + spacing.join(row_contents) + "\n"
        if hline or (heading and i == 0):
            tout += hdiv

    return tout


def table(t, vline=True, render=False, **kwargs):
    """Print or render an ASCII table."""
    # Ensure table has same dimensions
    for row in t:
        assert len(row) == len(t[0])

    t = [[str(cell) for cell in row] for row in t]
    tout = (__table_standard if vline else __table_nosep)(t, **kwargs)

    if render:
        return tout
    else:
        print(tout)
