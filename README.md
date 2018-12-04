# Print

Overloads Python's ```print``` function to add new and exciting functionality.

## Dependencies
- Python3 (Python2 does not allow overloading of the print statement)
- PyFiglet (ASII art, anyone?)

## Usage
Install with
```python
python3 setup.py install
```

First, ```import *``` from print to get access to all constants. Then, call the print statement. The first argument is the object to print; all other arguments are treated as modifiers. For example:
```python
>>> from print import *
>>> print("You can print normally")
You can print normally
>>> print(12345678)
12345678
>>> print("or with ASCII art", SM)
```
```
                  _ _   _        _   ___  ___ ___ ___            _   
 ___ _ _  __ __ _(_) |_| |_     /_\ / __|/ __|_ _|_ _|  __ _ _ _| |_ 
/ _ \ '_| \ V  V / |  _| ' \   / _ \\__ \ (__ | | | |  / _` | '_|  _|
\___/_|    \_/\_/|_|\__|_||_| /_/ \_\___/\___|___|___| \__,_|_|  \__|
                                                                     
>>> print("you can combine attributes", RED, BLUE+BG, BOLD)
you can combine attributes

<this will be bold red on a blue background on supported systems>

```

## Constants
All constants are accessible with ```from print import *``` or by by calling ```print.<CONST>```.

### Basic formatting
```python
RESET = 0
BOLD = 1
FAINT = 2
ITALIC = 3
UNDERLINE = 4
REVERSE = 7
CONCEAL = 8
STRIKEOUT = 9
```

### Colors
```python
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37
```

### Modifiers
```python
BRIGHT = 60
BR = 60
BACKGROUND = 10
BG = 10
```
- ```BRIGHT``` / ```BR```: use the brighter version of the color (not available on all terminals; your mileage may vary)
- ```BACKGROUND``` / ```BG```: set the background color instead of the text color

### Fonts
Only these fonts are included as constants. Other Figlet fonts (see Figlet's [website](http://www.figlet.org/)) can be passed as a string argument.
```python
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
```
