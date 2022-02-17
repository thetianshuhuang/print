"""A new print function that adds new and exciting functionality."""

from .print import print, render
from .table import table
from .putil import clear_fmt, join, span, pad, number
from .div import hfill, center, div

from .constants import *
from .exception import RenderedException

__all__ = [
    # Functions
    "print", "render", "table", "div",
    "clear_fmt", "join", "span", "pad", "number",

    # Error
    "RenderedException",

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
