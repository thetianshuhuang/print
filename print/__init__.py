
from .print import print, render


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


__all__ = [
    # Functions
    "print", "render",

    # Effects
    "RESET", "BOLD", "FAINT", "ITALIC",
    "UNDERLINE", "REVERSE", "CONCEAL", "STRIKEOUT",

    # Colors
    "BLACK", "RED", "GREEN", "YELLOW",
    "BLUE", "MAGENTA", "CYAN", "WHITE",

    # Modifiers
    "BRIGHT", "BR", "BACKGROUND", "BG",

    # Fonts
    "SM", "STD", "BIG", "ISO1", "ISO2", "ISO3", "ISO4",
    "SA", "DOOM", "DP", "L3D", "SMISO", "KB", "SLANT", "SMSLANT"
]
