"""Fancy exception."""

from .print import render
from . import constants as c


class RenderedException(Exception):
    """Exception, now featuring rendering."""

    style = [c.RED, c.SM, c.BOLD]

    def __str__(self):
        """Prints out ASCII art."""
        return(
            "\n" + render(type(self).__name__, *self.style)
            + " ".join([str(i) for i in self.args]))
