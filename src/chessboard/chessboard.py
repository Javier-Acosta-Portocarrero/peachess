"""Contains the class that defines the chessboard of the peachess game."""

from typing import TYPE_CHECKING

from pieces.piece import Piece, Color

# Used only by type annotations to avoid circular dependencies at runtime (needed because 
# chessboard.py imports Piece and piece.py imports chessboard).
if TYPE_CHECKING:
    from chessboard.chessboard import Chessboard

class Chessboard: 
    """Represents the board of the peachess game."""

    MIN_ROWS: int = 3
    MIN_COLUMNS_PER_ROW: int = 1

    def __init__(self, board_distribution: list[list[Piece | None]]) -> None:
        """Initializes a chessboard object.
        
        Args:
            board_distribution: Consists of a matrix with the chess pieces or None if the space is empty. 

        Raises:
            ValueError: If board_distribution is not valid (at least MIN_ROWS rows and MIN_COLUMNS_PER_ROW columns per row).
        """
        if len(board_distribution) >= self.MIN_ROWS and all(len(row) >= self.MIN_COLUMNS_PER_ROW for row in board_distribution):
            self.board = board_distribution
        else:
            raise ValueError(f"the distribution of the chessboard must have, at leat, {self.MIN_ROWS} rows and {self.MIN_COLUMNS_PER_ROW} column/s per row.")

    @property
    def max_amount_of_rows(self) -> int:
        """Property with the maximum amount of rows of the chessboard."""
        return len(self.board)
    
    @property
    def max_amount_of_columns(self) -> int:
        """Property with the maximum amount of columns of the chessboard."""
        return len(self.board[0])
    
    def move_piece(self, piece_position: tuple[int, int], destination: tuple[int, int]) -> None:
        """If the move is valid, moves a piece from its position to the destination given
        
        Args:
            piece_position: position of the piece that will be moved.
            destination: position where the piece will be moved.

        Raises:
            ValueError: If the move is not valid (_validate_move is encharged of doing it).
        """
        self._validate_move(piece_position, destination)

        origin_row, origin_column = piece_position
        destination_row, destination_column = destination
       
        current_piece: Piece | None = self.board[origin_row][origin_column]
        # A second validation can be safer and helps type checking.
        if current_piece is None:
            raise ValueError("There is no piece at the origin position.")

        self.board[origin_row][origin_column] = None
        # Already validated, so it can only be a piece of a different color or None.
        captured_piece: Piece | None = self.board[destination_row][destination_column]
        
        self.board[destination_row][destination_column] = current_piece
        current_piece.position = destination
        current_piece.after_move_effects(self, captured_piece)

    def is_cell_empty(self, cell: tuple[int, int]) -> bool:
        """Checks if a given cell of the chessboard is empty.
        
        Args:
            cell: Position of the cell.

        Returns: True if it is empty or False if not.
        """
        row, column = cell
        if self._is_valid_cell() and self.board[row][column] is None:
            return True
        return False
    
    def cell_has_enemy_piece(self, cell: tuple[int, int], piece_color: Color) -> bool:
        """Checks if a given cell of the chessboard has a enemy piece from the color specified.
        
        Args:
            cell: Position of the cell.
            piece_color: Color of the piece.

        Returns: True if it has an enemy piece or False if not.
        """
        row, column = cell
        if self._is_valid_cell() and self.board[row][column].color != piece_color:
            return True
        return False
    
    def _is_valid_cell(self, cell: tuple[int, int]) -> bool:
        """Checks if a given cell of the chessboard exists.
        
        Args:
            cell: Position of the cell.

        Returns: True if it a valid cell or False if not.
        """
        row, column = cell

        if row < 0 or row >= self.amount_of_rows:
            return False
        elif column < 0 or column >= len(self.board[row]):
            return False
        
        return True
    
    def _validate_move(self, piece_position: tuple[int, int], destination: tuple[int, int]) -> None:
        """Validates a move, if it is valid nothing happens, but if it is not, an exception is raised.
        
        Args:
            piece_position: position of the piece that will be moved.
            destination: position where the piece will be moved.

        Raises:
            ValueError: If the move is not valid.
        """
        origin_row, origin_column = piece_position
        destination_row, destination_column = destination

        if not self._is_valid_cell(piece_position) or not self._is_valid_cell(destination):
            raise ValueError("One or both of the cells specified doesn not belong to the chessboard.")
        
        current_piece: Piece | None = self.board[origin_row][origin_column]
        if current_piece is None:
            raise ValueError("The cell specified does not have a peachess piece on it.")
        if destination not in current_piece.possible_moves(self):
            raise ValueError("The destination cell can not be reached by the selected piece.")
        
        destination_piece: Piece | None = self.board[destination_row][destination_column]
        if destination_piece is not None and destination_piece.color == current_piece.color:
            raise ValueError("The destination cell has already a piece of the same color on it.")