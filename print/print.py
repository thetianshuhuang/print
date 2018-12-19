
"""ASCII Large Text and ANSI escape sequence print overloading

Examples
--------
print("Testing", RED, BOLD)
print("ASCII Art", BLUE+BR, BIG)
"""

import sys
import os

# Try to import pyfiglet
try:
    import pyfiglet
    def __pf_render(s, f):
        return s if f is None else pyfiglet.Figlet(f).renderText(s)
except ImportError:
    def __pf_render(s, f):
        return s
    print("PyFiglet not found (Large ASCII word art disabled)")


# Check for windows
if os.name == 'nt':
    try:
        import colorama
    except ImportError:
        raise Exception(
            "Must have colorama installed for color translation on windows "
            "systems")
    colorama.init(wrap=False)
    __stream = colorama.AnsiToWin32(sys.stderr).stream
else:
    __stream = None


def __esc(code):
    """Get ANSI escape string"""
    return "\u001b[{c}m".format(c=code)


def __get_font(args):
    return next((i for i in args if type(i) == str), None)


def render(s, *args):
    """Render text with color and font"""

    mods = "".join([__esc(i) for i in args if type(i) == int])
    s = mods + __pf_render(s, __get_font(args))

    # Remove trailing newline
    if len(s) > 0 and s[-1] == '\n':
        s = s[:-1]

    # Add escape
    return s + __esc(0)


# Save print statement
__print = print

# Log file
__LOG_FILE = None


def set_log(filename=None):
    """Set a log

    Parameters
    ----------
    filename : str
        New filename. If None, then no log file is generated.
    """
    global __LOG_FILE
    __LOG_FILE = filename


def print(s, *args):
    """Print statement overloading"""

    global __stream

    # Linux
    if __stream is None:
        __print(render(str(s), *args))
    # Windows
    else:
        __print(render(str(s), *args), file=__stream)

    # Logging
    global __LOG_FILE
    if __LOG_FILE is not None:

        with open(__LOG_FILE, 'a') as log:
            from .putil import clear_fmt
            log.write(clear_fmt(render(str(s), *args)) + '\n')
            log.close()


if __name__ == "__main__":

    print("print.py", )
