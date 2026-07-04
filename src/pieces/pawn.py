"""Contains the class Pawn, an important Peachess piece."""

from collections.abc import Sequence

from chessboard.chessboard import Chessboard
from piece import Piece, Color

class Pawn(Piece):
    """Represents a classic pawn piece in peachess game"""

    def __init__(self, position: tuple[int, int], color: Color):
        """Initializes a pawn piece.

        Args:
            position: Current position of the piece in the chessboard.
            color: Color of the piece (class defined in color.py).
        """
        super().__init__(position, color)
        self.has_moved: bool = False

    def possible_moves(self, board: Chessboard) -> list[tuple[int, int]]:
        """Returns the possible moves of the pawn in the board given.
        
        Args:
            board: Chessboard where the piece is placed.

        Returns:
            List of possible positions as pairs of integers.
        """
        possible_moves: list[tuple[int, int]] = []

        if not self.has_moved and board.is_cell_empty([self.position[0], self.position[1] + 2]):
            possible_moves.append((self.position[0], self.position[1] + 2))

        if board.is_cell_empty((self.position[0], self.position[1] + 1)):
            possible_moves.append((self.position[0], self.position[1] + 1))

        POSSIBLE_LATERAL_DISPLACEMENTS: Sequence[int] = (1, -1)
        for lateral_displacement in POSSIBLE_LATERAL_DISPLACEMENTS:
            if board.cell_has_enemy_piece((self.position[0] + lateral_displacement, self.position[1] + 1), self.color):
                possible_moves.append((self.position[0] + lateral_displacement, self.position[1] + 1))
        
        return possible_moves

    def get_representation(self) -> str:
        """Returns the string representation of the pawn."""
        return "P"

    def apply_after_move_effects(self, board: Chessboard, piece_captured: Piece | None = None) -> None:
        """Apply the effects of the pawn move, if it has reached the opposite limit
        of the board, it can become another Peachess piece.
        
        Args:
            board: Chessboard where the piece is placed.
            piece_captured: The kind of piece captured or None if no piece was captured.
        """
        self.has_moved = True
        match self.color:
            case Color.BLACK:
                if self.position[0] == board.max_amount_of_rows:
                    self.can_promote = True
            case Color.WHITE:
                if self.position[0] == 0:
                    self.can_promote = True