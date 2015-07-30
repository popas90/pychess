from pychess.Piece import *
from pychess.Pawn import Pawn
from pychess.Rook import Rook
from pychess.Bishop import Bishop
from pychess.Knight import Knight
from pychess.Queen import Queen
from pychess.King import King


class BoardParser:
    def parse_board(self, file_path):
        """
        Parses the file to retrieve a board configuration.
        :param file_path: path to file
        :return: the board configuration read from the file
        """
        if not self._verify_board_from_file(file_path):
            return False, None
        ## TODO load the file to memory, check for compliance, then send new structure to board creation
        rows, columns = range(1, 9), "ABCDEFGH"
        board = [{col: None for col in columns} for _ in rows]

        with open(file_path, "r") as file:
            row_iter, column_iter = iter(rows), iter(columns)
            for line in file:
                row, col = next(row_iter), next(column_iter)
                symbols = line.split(" ")
                for sym in symbols:
                    board[row][col] = self._get_piece_from_symbol(sym, row, col)

        return True, board

    @staticmethod
    def _verify_board_from_file(file_path):
        pass

    @staticmethod
    def _get_piece_from_symbol(sym, row, col):
        """
        Returns a new Piece object from the two-letter symbol parameter.
        :param sym: string representing piece and color
        :param row: row location
        :param col: column location
        :return: a new Piece object or None
        """
        color = Color.white if sym[1].capitalize() == "W" else Color.black
        piece = sym[0].capitalize()
        if piece == "K":
            return King(color, (row, col), True)
        elif piece == "Q":
            return Queen(color, (row, col), True)
        elif piece == "R":
            return Rook(color, (row, col), True)
        elif piece == "B":
            return Bishop(color, (row, col), True)
        elif piece == "N":
            return Knight(color, (row, col), True)
        elif piece == "P":
            return Pawn(color, (row, col), True)
        else:
            return None