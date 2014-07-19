"""
Given two strings, determine if the third string is a shuffled version
of the first two. The individual strings have to stay in order in
relation to the other characters in themselves.

'abc' and 'def' -> 'abdecf' TRUE
'abc' and 'def' -> 'acdecf' FALSE
"""


def shuffled(s1, s2, s3):
    """
    Uses two queues to determine if the third string is an interleaved
    version of the first string.

    Space Complexity: O(n)
    Time Complexity: O(n)
    """

    q1, q2 = Queue(list(s1)), Queue(list(s2))
    for letter in s3:
        val1, val2 = q1.peek(), q2.peek()
        if letter != val1 and letter != val2:
            return False
        elif letter == val1:
            val1 = q1.dq()
        else:
            val2 = q2.dq()
    return True


class Queue(object):
    def __init__(self, array):
        self.first = None
        self.last = None
        for element in array:
            self.eq(element)
    
    def eq(self, value):
        if not self.first:
            self.last = Node(value)
            self.first = self.last
        else:
            newNode = Node(value)
            self.last.next = newNode
            self.last = newNode

    def dq(self):
        assert self.first is not None, 'Queue is empty!'
        value = self.first.data
        self.first = self.first.next
        return value

    def peek(self):
        if self.first:
            return self.first.data
        else:
            return None

class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

print shuffled('abc', 'def', 'abcdef')
