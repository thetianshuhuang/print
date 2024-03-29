# Print

![Print It!](https://github.com/thetianshuhuang/print/blob/master/print.png)

A new ```print``` function to add new and exciting functionality.

## Dependencies
- Python3 (Python2 does not allow overloading of the print statement)
- PyFiglet (ASII art, anyone?)

## Installation
Install with
```shell
pip install printtools
```

For the latest version, clone this repository and use
```shell
python3 setup.py install
```

## Usage
The first argument is the object to print; all other arguments are treated as modifiers. For example:
```
>>> import printtools as pt
>>> pt.print("You can print normally")
You can print normally
>>> pt.print(12345678)
12345678
>>> pt.print("or with ASCII art", pt.SM)
                  _ _   _        _   ___  ___ ___ ___            _
 ___ _ _  __ __ _(_) |_| |_     /_\ / __|/ __|_ _|_ _|  __ _ _ _| |_
/ _ \ '_| \ V  V / |  _| ' \   / _ \\__ \ (__ | | | |  / _` | '_|  _|
\___/_|    \_/\_/|_|\__|_||_| /_/ \_\___/\___|___|___| \__,_|_|  \__|

>>> pt.print("you can combine attributes", pt.RED, pt.BLUE + pt.BG, pt.BOLD)
you can combine attributes

<this will be bold red on a blue background on supported systems>

```

**NOTE**: since all other args are captured as formatting arguments, you cannot print multiple items at once as in
```print(1, 2, 3)```.

## Dividers
The ```div``` module can be used to create nice looking dividers:
```
>>> div.div('-')
----------------------------------------- # stretches all the way across the terminal
>>> div.div('*', 'Example')
** Example ******************************
>>> div.div('= =', 'Example')
=========================================

                Example

=========================================
```
Patterns include:
- single character: repeats that character across the screen. If a message is provided, two characters are displayed, followed by a space, the message, a space, then characters occupying the remainder of the screen
- character repeated, with spaces in between: draws two horizontal lines across the screens with that character; in between the two lines, the label text is drawn at the center. Blank lines equal to the number of spaces are added on top and below the label text.

## Tables
Use the ```table``` module to print out tables. Tables consist of two-dimensional arrays:
```
>>> from print import table
>>> t = [["Entry 1", 0.0001, "Value 1"], ["Entry 2", 12345, "Value 2"]]
>>> table(t)
+-------+------+-------+
|Entry 1|0.0001|Value 1|
+-------+------+-------+
|Entry 2|12345 |Value 2|
+-------+------+-------+
```

```table(render=True)``` and ```render``` can be combined to add formatting:

```
>>> from print import *
>>> t = [
	[pt.render("Entry 1", pt.RED), 0.0001, "Value 1"],
	[pt.render("Entry 2", pt.GREEN), 12345, "Value 2"]]
>>> print(pt.table(t, render=True), pt.BOLD)
```


## Custom Exception
Use the ```RenderedException``` class to provide a more colorful base exception class.
```
>>> class YouFuckedUpError(pt.RenderedException):
...    pass
...
>>> raise YouFuckedUpError("You've really fucked it up this time. Yeah you.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.YouFuckedUpError:
__   __        ___        _          _ _   _      ___
\ \ / /__ _  _| __|  _ __| |_____ __| | | | |_ __| __|_ _ _ _ ___ _ _
 \ V / _ \ || | _| || / _| / / -_) _` | |_| | '_ \ _|| '_| '_/ _ \ '_|
  |_|\___/\_,_|_| \_,_\__|_\_\___\__,_|\___/| .__/___|_| |_| \___/_|
                                            |_|
You've really fucked it up this time. Yeah you.
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
