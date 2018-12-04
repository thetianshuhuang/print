
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


# Text Effects
RESET = 0
BOLD = 1
FAINT = 2
ITALIC = 3
UNDERLINE = 4
REVERSE = 7
CONCEAL = 8
STRIKEOUT = 9

# Colors
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37

# Modifiers
BRIGHT = 60
BR = 60
BACKGROUND = 10
BG = 10

# Standard fonts
SM = "small"
STD = "standard"
BIG = "big"

# Isometric fonts
ISO1 = "isometric1"
ISO2 = "isometric2"
ISO3 = "isometric3"
ISO4 = "isometric4"

# Other fonts
SA = "contessa"
DOOM = "doom"
DP = "drpepper"
L3D = "larry3d"
SMISO = "smisome1"
KB = "smkeyboard"
SLANT = "slant"
SMSLANT = "smslant"


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
