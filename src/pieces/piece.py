"""Contains the abstract class of the chess pieces."""

from abc import ABC, abstractmethod

from color import Color
from chessboard.chessboard import Chessboard

class Piece(ABC):
    """Represents a basic chess piece."""

    def __init__(self, position: tuple[int, int], color: Color) -> None:
        """Initializes a chess piece.

        Args:
            position: Current position of the piece in the chessboard.
            color: Color of the piece (class defined in color.py).
        """
        self.position = position
        self.color = color
    
    @abstractmethod
    def possible_moves(self, board: Chessboard) -> list[tuple[int, int]]:
        """Returns the possible moves of the chess piece int he board given.
        
        Args:
            board: Chessboard where the piece is placed.

        Returns:
            List of possible positions as pairs of integers.
        """
        pass

    @abstractmethod
    def get_representation(self) -> str:
        """Returns the string representation of the piece."""
        pass