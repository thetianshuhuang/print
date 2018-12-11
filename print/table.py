
from .print import print


def render(t, padding=''):
    """Render an ASCII table"""

    # Convert all to strings
    t = [[str(cell) for cell in row] for row in t]

    # Ensure table has same dimensions
    for row in t:
        assert len(row) == len(t[0])

    # Get column widths
    widths = [0 for _ in t[0]]
    for row in t:
        widths = [max(widths[i], len(cell)) for i, cell in enumerate(row)]

    tout = ''
    # Make horizontal divider
    hdiv = "{padding}+{content}+\n".format(
        padding=padding,
        content='+'.join(['-' * width for width in widths]))
    tout += hdiv

    # Make cells
    for row in t:
        tout += "{padding}|{content}|\n".format(
            padding=padding,
            content='|'.join([
                cell + ' ' * (width - len(cell))
                for width, cell in zip(widths, row)]))
        tout += hdiv

    return tout


def table(t, padding=''):
    """Print an ASCII table"""
    print(render(t, padding=padding))
