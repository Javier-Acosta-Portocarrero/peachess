"""Contains the enum that represents the possible colors of chess pieces."""

from enum import Enum

class Color(Enum):
    """Represents the possible colors of chess pieces, being an enum makes it easier to expand the game."""
    
    WHITE = "white"
    BLACK = "black"