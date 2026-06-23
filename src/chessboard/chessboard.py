"""Contains the class that defines the chessboard of the peachess game."""

from pieces.piece import Piece

class Chessboard: 
    """Represents the board of the peachess game."""

    def __init__(self, board_distribution: list[list[Piece | None]] | None = None) -> None:
        """Initializes a chessboard object.
        
        Args:
            board_distribution: Consists of a matrix with the chess pieces or None if the space is empty. 
              If it is not provided, the distribution of the chessboard 
              will be built with the private method '_build_standard_distribution()'.  
        """
        if board_distribution is None:
            self._build_standard_distribution()
        else:
            self.board = board_distribution