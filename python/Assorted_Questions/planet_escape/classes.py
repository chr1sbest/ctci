class Ship(object):
    """
    Basic ship that can accelerate and decelerate velocity by thrusting.
    """
    def __init__(self):
        self.position = 0
        self.velocity = 0

    def move(self):
        self.position += self.velocity

    def thrust(self, value):
        self.velocity += value
    

class Asteroid(object):
    """
    Asteroids have a base offset value and a cycle for how often they make
    a full rotation around the planet.
    """
    def __init__(self, offset, cycle):
        self.offset = offset
        self.cycle = cycle
        self.original_offset = self.offset

    def move(self):
        self.offset += 1

    def reset(self):
        self.offset = self.original_offset

    @property
    def blocking(self):
        if self.offset % self.cycle:
            return True
        else:
            return False


class AsteroidBelt(object):
    """
    Belt of asteroids and a planet to revolve around.
    """
    def __init__(self):
        planet = Asteroid(1000, 1)   # We consider the planet the initial asteroid
        self.asteroids = [planet]

    def move(self):
        """
        Move all asteroid positions by 1.
        """
        map(lambda ast: ast.move(), self.asteroids)

    def reset(self):
        """
        Reset the positions of all asteroids to the original position.
        """
        map(lambda ast: ast.reset(), self.asteroids)

    def __len__(self):
        return len(self.asteroids) - 1


class ChoiceTree(object):
    def __init__(self, data, options):
        self.data = data
        self.children = []
        self.options = options
        self.pruned = False

    def build_children(self):
        """
        Lazily build children for each option when needed.
        Do not build children if the tree is already pruned!
        """
        if not self.children and not self.pruned:
            for option in self.options:
                new_data = self.data + (option,)
                new_child = ChoiceTree(new_data, self.options)
                self.children.append(new_child)

    def prune(self):
        """
        Remove subtrees.
        """
        self.children = []
        self.pruned = True


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def eq(self, data):
        if not self.first:
            self.last = Node(data)
            self.first = self.last
        else:
            newNode = Node(data)
            self.last.nextNode = newNode
            self.last = newNode

    def dq(self):
        assert self.first is not None, 'Queue is empty!'
        value = self.first.data
        self.first = self.first.nextNode
        return value


class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

