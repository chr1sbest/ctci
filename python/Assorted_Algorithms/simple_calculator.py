def calculate(user_input):
    """
    Uses Djikstra's Two Stack Arithmetic Evaluation.

    Parses input and evaluates infix expressions using two stacks.
    Removes '(' because they are not needed for evaluation.
    """
    parsed = [x for x in user_input.split(' ') if x != ' ' and x != '(']
    int_stack, oper_stack = Stack(), Stack()
    opers = set(['*', '/', '+', '-'])
    for value in parsed:
        if value in opers:
            oper_stack.push(value)
        elif value is ')':
            val2, val1 = int_stack.pop(), int_stack.pop()
            operation = oper_stack.pop()
            print val1, operation, val2
            new_val = evaluate(operation, val1, val2)
            int_stack.push(new_val)
        else:
            try:
                int_stack.push(int(value))
            except:
                print 'Unrecognized value "{0}"'.format(value)
                return Fale
    return int_stack.pop()

def evaluate(operation, val1, val2):
    options = { '*': lambda x,y: x * y
              , '/': lambda x,y: float(x) / float(y)
              , '+': lambda x,y: x + y
              , '-': lambda x,y: x - y
              }
    return options[operation](val1, val2)


class Stack(object):
    def __init__(self):
        self.stack = Node()

    def push(self, data):
        self.stack = Node(data, self.stack)

    def pop(self):
        tmp =  self.stack.data
        self.stack = self.stack.next_node
        return tmp

    def peek(self):
        return self.stack.data


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

if __name__ == "__main__":
    maths = '( 30 / ( 3 + 5 ) )'
    print '{0} = {1}'.format(maths, calculate(maths))
