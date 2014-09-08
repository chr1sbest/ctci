class Player(object):
    def __init__(self):
        self.board = [[None for x in xrange(10)] for y in xrange(10)]
        self.ships = [Ship(5, self), Ship(4, self), Ship(3,self), 
                      Ship(3, self), Ship(2, self)]
        self.place_ships()

    def place_ships(self):
        """
        Place ships onto your board.
        """
        for ship in self.ships:
            valid = False
            while not valid:
                #Display Board
                #Prompt for (X,Y) Coordinates
                #Prompt for direction
                #Validate move
            for part in ship.parts:
                self.board[x][y] = part
                #Increment x,y by proper direction
            pass

    def attack(self, player, x, y):
        """
        Attack an X,Y Coordinate. Return Hit/Sunk/Miss.
        """
        attacked = player.board[x][y]
        if attacked == None:    #TODO don't let same spot get attacked
            move_outcome = (False, "Miss")
        else:
            attacked.status = False
            move_outcome = (True, attacked.ship.check_status())
            if player.check_loss():
                return (False, "You Win!")
        return move_outcome

    def check_loss():
        """
        Check if all ships sank.
        """
        for ship in self.ships:
            if ship.status = True:
                return False
        return True

class Ship(object):
    def __init__(self, board, size):
        self.board = board
        self.parts = [Part(self) for x in xrange(size)]
        self.status = True

    def check_status(self):
        """
        Check if ship is still alive.
        """
        for part in self.parts:
            if part.status = True:
                return "Hit!"
        self.status == False
        return "Ship({0}) sunk!".format(ship.size)

class Part(object):
    def __init__(self, ship):
        self.status = True
        self.ship = ship
