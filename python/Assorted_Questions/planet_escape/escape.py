"""
Problem:
-Planet is going to explode, need to escape on our ship.
-Asteroids orbit the planet at different speeds and offsets.
-Have to navigate around asteroids by changing velocity by -1 or +1 each turn.
-Considered a collision if asteroid and ship occupy same position.
-Planet explosion radiates outwards at certain speed, can't hang around.
-Find optimal way to escape asteroid belt!

Notes:
-Seemingly a tree problem (possibly graph), DFS could probably find solution.
-BFS could probably give optimal solution.
-Building out classes to manually solve problem before optimizing
-BFS worked, but the tree building scales terribly. Building simulator.
-Lazily build children now instead of building all from the start.
-Implemented choice pruning so failure subtrees aren't explored.
"""
from classes import Asteroid, AsteroidBelt, Ship

def escape(moves, belt, blast_time=2):
    """
    Takes an array of moves and an array of Asteroid objects and attempts to
    send ship through the asteroid belt to escape from Planet.
    """
    ship = Ship()
    belt.reset()
    print 'Trying {0}'.format(moves)
    for turn, direction in enumerate(moves):
        ship.thrust(direction)  # Change velocity accordingly
        ship.move()             # Move the ship accordingly
        belt.move()             # Move all the asteroids
        if ship.position > len(belt):
            print 'Congratulations, you have escaped the asteroid belt!'
            print 'Moves: {0}'.format(moves)
            return True
        elif belt.asteroids[ship.position].blocking:
            print 'Oh no! You have crashed'
            return False
        elif turn / blast_time > ship.position:
            print 'Oh no! You have been consumed by the planet'
            return False
    print 'Need more directions!'
    return None


if __name__ == "__main__":
    moves = (0, 0, 0, 1, 1, 1)
    asteroids = [(0, 2), (1, 3), (3, 4), (1, 2)]    #(offset, cycle)
    belt = AsteroidBelt()
    for asteroid in asteroids:
        new_asteroid = Asteroid(*asteroid)
        belt.asteroids.append(new_asteroid)
    escape(moves, belt, blast_time=10)
