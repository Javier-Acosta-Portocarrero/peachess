"""Contains the class King, an important Peachess piece."""

from chessboard.chessboard import Chessboard
from piece import Piece, Color

class King(Piece):
    """Represents a classic King piece in peachess game"""

    def __init__(self, position: tuple[int, int], color: Color):
        """Initializes a King piece.

        Args:
            position: Current position of the piece in the chessboard.
            color: Color of the piece (class defined in color.py).
        """
        super.__init__(position, color)
        self.has_moved: bool = False

    def possible_moves(self, board: Chessboard) -> list[tuple[int, int]]:
        """Returns the possible moves of the King in the board given.
        
        Args:
            board: Chessboard where the piece is placed.

        Returns:
            List of possible positions as pairs of integers.
        """
        # In develpment
        pass

    def get_representation(self) -> str:
        """Returns the string representation of the King."""
        return "K"

    def apply_after_move_effects(self, board: Chessboard, piece_captured: Piece | None = None) -> None:
        # In develpment
        pass