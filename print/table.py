
from .print import print


def render(t):
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
    hdiv = '+' + '+'.join(['-' * width for width in widths]) + '+\n'
    tout += hdiv

    # Make cells
    for row in t:
        tout += (
            '|' +
            '|'.join([
                cell + ' ' * (width - len(cell))
                for width, cell in zip(widths, row)]) +
            '|\n')
        tout += hdiv

    return tout


def table(t):
    """Print an ASCII table"""
    print(render(t))
