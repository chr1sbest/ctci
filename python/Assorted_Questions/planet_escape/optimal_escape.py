from escape import escape
from classes import Ship, Asteroid, AsteroidBelt, ChoiceTree, Queue
from asteroid_parser import asteroid_parser

def bfs(belt, choice_tree):
    """
    Using Breadth-First Search,
    Iteratively explore solutions with Queue until shortest solution is found.

    Prune choice subtrees that result in a crash.
    """
    visited, queue = set(), Queue()
    queue.eq(choice_tree)
    try:
        while queue:
            choice = queue.dq()
            if choice.data not in visited:
                visited.add(choice.data)
                choice.build_children()             # Lazily build children
                result = escape(choice.data, belt)
                if result == True:
                    return choice.data
                elif result == False:
                    choice.prune()
                for child in choice.children:
                    queue.eq(child)
    except AssertionError, error:
        print 'Choice tree was not able to find a solution.'


def simulation_runner(asteroid_list, rocket_power=1, blast_time=2):
    """
    Runs a simulation using different asteroid belts and different
    options for thruster power.

    A rocket with power of 1 has the options [1, 0, -1]
    A rocket with power of 3 has the options [3, 2, 1, 0, -1, -2, -3]
    """
    # Build Asteroid Belt
    belt = AsteroidBelt()
    for asteroid in asteroids:
        new_asteroid = Asteroid(*asteroid)
        belt.asteroids.append(new_asteroid)

    # Prioritize positive thrust values over negative.
    thrust_options = [x for x in range(rocket_power, -(rocket_power + 1), -1)]

    # Run BFS
    choice_tree = ChoiceTree((0,), thrust_options)
    bfs(belt, choice_tree)

if __name__ == "__main__":
    asteroids = asteroid_parser('chart.json')[:60]
    simulation_runner(asteroids, blast_time=2)
