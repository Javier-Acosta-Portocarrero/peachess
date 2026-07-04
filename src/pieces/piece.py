"""Contains the abstract class of the chess pieces."""

# Allows using type annotations for classes that are defined later (needed to use Piece argument in 'apply_after_move_effects').
from __future__ import annotations 

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from color import Color

# Used only by type annotations to avoid circular dependencies at runtime (needed because 
# chessboard.py imports Piece and piece.py imports chessboard).
if TYPE_CHECKING:
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
        self.can_promote = False
    
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

    def apply_after_move_effects(self, board: Chessboard, piece_captured: Piece | None = None) -> None:
        """General method used to apply the effects of a move, for a example, a pawn can promote if the 
        move ends in the last row od the chessboard, new non conventional pieces may be added, so information
        like if it has captured an specific enemy piece can be importante fot the effects.

        Args:
            piece_captured: The kind of piece captured or None if no piece was captured.
            board: Chessboard where the piece has been moved.
        """
        pass