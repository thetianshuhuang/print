
"""ASCII Large Text and ANSI escape sequence print overloading

Examples
--------
print("Testing", RED, BOLD)
print("ASCII Art", BLUE+BR, BIG)
"""

import sys

try:
    import pyfiglet
    def __pf_render(s, f):
        return s if f is None else pyfiglet.Figlet(f).renderText(s)
except ImportError:
    def __pf_render(s, f):
        return s


def __esc(code):
    """Get ANSI escape string"""
    return "\u001b[{c}m".format(c=code)


def render(s, *args):
    """Render text with color and font"""

    font = next((i for i in args if type(i) == str), None)
    mods = "".join([__esc(i) for i in args if type(i) == int])

    s = mods + __pf_render(s, font) + __esc(0)
    if font is None:
        s += "\n"

    return s

def print(s, *args):
    """Print statement overloading"""
    sys.stdout.write(render(str(s), *args))


if __name__ == "__main__":

    print("print.py", )
