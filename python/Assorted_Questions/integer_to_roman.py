def int_to_roman(number):
    """
    Convert integer to Roman Numeral.
    """
    numerals = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
    patterns = [[], [0], [0, 0], [0, 0, 0], [0, 1], [1], 
                [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2], [2]]
    place = 0
    roman = ''
    while number >= 1:
        current = number % 10
        pattern = patterns[current]
        for value in pattern:
            roman = numerals[place][value] + roman
        number, place = number / 10, place + 1
    return roman

def roman_to_int(roman):
    """
    Convert Roman Numeral to integer.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    queue = Queue()
    for letter in roman:
        queue.eq(letter)
    integer = 0
    conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                   'C': 100, 'D': 500, 'M': 1000}
    while not queue.empty():
        first, next = queue.dq(), queue.peek() or 0
        if conversions[first] >= conversions[next]:
            integer += conversions[first]
        else:
            queue.dq()
            integer += conversions[next] - conversions[first]
    return integer

class Queue(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head.next

    def eq(self, value):
        if self.head.value == None:
            self.head = Node(data=value, next=self.tail)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dq(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.value

    def empty(self):
        if self.head == None:
            return True
        else:
            return False


class Node(object):
    def __init__(self, data=None, next=None):
        self.value = data
        self.next = next


if __name__ == "__main__":
    print int_to_roman(52)
    print int_to_roman(512)
    print roman_to_int('XXIV')

