"""
Design a chess game.

In this incomplete implementation, I chose to build three distinct
components -- the Board, Pieces, and Players.

Board
-Builds an 8x8 matrix and instantiates the players and pieces.
-Updates accordingly when told to.
-Runs turns infinitely until a player is missing their King.

Pieces
-Each type of piece inherits from a parent Piece class.
-Each type of piece has a specific movement strategy.
-Checks with the player if a movement is possible before executing.

Players
-Hold a set of their pieces and their current positions.
-Validates moves for their pieces.
"""

class Board(object):
    def __init__(self):
        """ Build an 8x8 matrix of pieces for black and white. """
        self.board = [
            [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rook('w')],
            [Pawn('w'), Pawn('w'),   Pawn('w'),   Pawn('w'),  Pawn('w'), Pawn('w'),   Pawn('w'),   Pawn('w')],
            [None,      None,        None,        None,       None,      None,        None,        None],
            [None,      None,        None,        None,       None,      None,        None,        None],
            [None,      None,        None,        None,       None,      None,        None,        None],
            [None,      None,        None,        None,       None,      None,        None,        None],
            [Pawn('b'), Pawn('b'),   Pawn('b'),   Pawn('b'), Pawn('b'),  Pawn('b'),   Pawn('b'),   Pawn('b')],
            [Rook('b'), Knight('b'), Bishop('b'), King('b'), Queen('b'), Bishop('b'), Knight('b'), Rook('b')]
        ]
        self._add_pieces()

    def _add_pieces(self):
        """ Add pieces that were initialized on the board to each player's set """
        self.black, self.white = Player(self), Player(self)
        for square in row in self.board:
            if None:
                pass
            elif square.color = 'w':
                self.white.add_piece(square)
            elif square.color = 'b':
                self.black.add_piece(square)

    def play(self):
        """ Run game until white or black wins """
        turn = 0
        while True:
            self.white.turn() if turn % 2 == 0 else self.black.turn()
            if King('b') not in self.black.pieces:
                return 'White Wins!'
            if King('w') not in self.white.pieces:
                return 'Black Wins!'
            turn += 1


# Board Logic and Win Conditions
class Player(object):
    def __init__(self, board):
        self.pieces = set()
        self.board = board

    def add_piece(self, piece):
        self.pieces.add(piece)

    def turn(self):
        """ Prompt player to move pieces."""
        while True:
            print self.board
            user_move = raw_input("How would you like to move?")
            if self.validate(user_move):
                self.board.update(user_move)
            else:
                print "Invalid move!"

    def validate(self, user_move):
        """ Checks if move is valid."""
        return True if valid else False


# Piece Logic
class Piece(object):
    def __init__(self, color, x, y):
        assert color == 'w' or color == 'b', 'Color needs to be w or b'
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        """ Logic to be defined in subclasses. """
        pass

    def __str__(self):
        """ Knight('w') represented as 'w-Knight' """
        return "{0}-{1}".format(self.color, self.__name__)


class Pawn(Piece):
    def move(self):
        pass

    def upgrade(self):
        """ When the pawn reaches the end, upgrade to a Queen """
        pass


class Knight(Piece):
    def move(self):
        pass


class Rook(Piece):
    def move(self):
        pass


class Bishop(Piece):
    def move(self):
        pass


class Queen(Piece):
    def move(self):
        pass


class King(Piece):
    def move(self):
        pass
