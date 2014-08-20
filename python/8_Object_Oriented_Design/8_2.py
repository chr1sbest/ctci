"""
Imagine you have a call center with three levels of employees:
Respondent, Manager, and Director. An incoming telephone call must
be first allocated to a respondent who is free. If the respondent
can't handle the call, he or she must escalate the call to a manager.
If the manager isn't free, he or she must escalate to a director.

Design all the classes and data structures for this problem. Implement
a method called dispatchCall() which assigns the call to the first
available employee.
"""
from abc import abstractproperty

class Call_Center(object):
    def __init__(self):
        # Build priority queue of employees
        self.employees = PriorityQueue()

    def add_employees(self, employees):
        """ Add list of employees to priority queue """
        for employee in employees:
            self.employees.add(employee.ranking, employee)

    def dispatch_call(self):
        receiver = self.employees.pop()
        receiver.answer_call()
        return receiver


class Employee(object):
    def __init__(self, call_center):
        self.call_center = call_center

    def answer_call(self):
        """ Logic to handle call. """
        print self.__class__.__name__ + "is receiving the call."

    def hang_up(self):
        """ Add self back to priority queue. """
        self.call_center.add(self)

    @abstractproperty
    def ranking(self):
        raise NotImplementedError


class Respondent(Employee):
    ranking = 1


class Manager(Employee):
    ranking = 2


class Director(Employee):
    ranking = 3


class PriorityQueue(object):
    def __init__(self):
        pass

    def add(self, key, value):
        pass

    def pop(self):
        pass

if __name__ == "__main__":
    cc = Call_Center()
    employees = [Respondent(cc), Manager(cc), Director(cc), Respondent(cc)]
    cc.add_employees(employees)
    receiver1 = cc.dispatch_call()
    receiver2 = cc.dispatch_call()
    receiver3 = cc.dispatch_call()
    receiver1.hang_up()
    receiver4 = cc.dispatch_call()
