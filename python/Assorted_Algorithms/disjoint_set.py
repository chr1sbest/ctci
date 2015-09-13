class DisjointSet(object):
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

    def find(self):
        """ Determine which set a node belongs to by recursively traversing
        upwards through the tree while utilizing path compression by assigning
        each node.parent to its parent.parent.

        O(logN) worst-case. """
        if self.parent != self:
            self.parent = self.parent.find()
            return self.parent
        return self

    def union(self, other):
        """ Union with ranking. """
        self_root, other_root = self.find(), other.find()
        # Determine which set is ranked higher by root.rank
        if self_root.rank > other_root.rank:
            greater_root, lesser_root = self_root, other_root
        elif self_root.rank < other_root.rank:
            greater_root, lesser_root = other_root, self_root
        else:
            # If both sets are equal in rank, randomly assign the
            # greater root and increment its rank by 1
            greater_root, lesser_root = self_root, other_root
            greater_root.rank += 1
        # In all cases, connect the lesser set to the greater set by assigning
        # the lesser_root parent to the parent of the greater_root
        lesser_root.parent = greater_root


def test_disjoin_set():
    # Initialize individual sets
    a = DisjointSet('a')
    b = DisjointSet('b')
    c = DisjointSet('c')
    d = DisjointSet('d')
    e = DisjointSet('e')
    f = DisjointSet('f')
    g = DisjointSet('g')

    # Test basic union/find
    a.union(b)
    assert b.find() == a
    a.union(c)
    # Set A now contains {A, B, C}, all pointing to A as parent
    assert c.find() == a and b.find() == a

    # Now we will create a separate Set D of {D, E, F, G}
    d.union(e)
    e.union(f)
    f.union(g)

    # Combine the sets to check that ranking is properly compared and the
    # smaller set is added onto the larger set. We will check that a member
    # of Set D {D, E, F, G} will now have the same parent as a member from
    # Set A {A, B, C}. Specifically, we will check that this parent is from
    # the larger of the sets (D).
    d.union(a)
    assert f.find() == c.find()
    assert f.find() == d and c.find() == d
