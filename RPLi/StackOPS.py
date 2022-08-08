#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  A class for stacks operations
# History:
#           2021-10-07, BRA, extra credit
#           2021-10-07, BRA, add false method
#           2021-10-07, BRA, add true method
#           2021-10-07, BRA, add == method
#           2021-09-23, BRA, created

from Stack import Stack
import math


class StackOPS(Stack):
    # StackOPS constructor
    def __init__(self):
        # call the parent class constructor
        Stack.__init__(self)

    # add two numbers on the stack, push the result back on the stack
    def add(self) -> None:
        #x = self.pop()
        #y = self.pop()
        #result = x + y
        #self.push(result)
        self.push(self.pop() + self.pop())

    def sub(self) -> None:
        x = self.pop()
        y = self.pop()
        result = y - x
        self.push(result)

    def mul(self) -> None:
        x = self.pop()
        y = self.pop()
        result = x * y
        self.push(result)

    def div(self) -> None:
        x = self.pop()
        y = self.pop()
        result = y / x
        self.push(result)

    def swap(self) -> None:
        x = self.pop()
        y = self.pop()
        self.push(x)
        self.push(y)

    # add == method
    def equal(self) -> None:
        x = self.pop()
        y = self.pop()
        if x == y:
            self.push(True)
        else:
            self.push(False)

    # add true method
    def true(self) -> None:
        self.push(True)

    # add false method
    def false(self) -> None:
        self.push(False)

    # extra credit
    def lessthan(self) -> None:
        x = self.pop()
        y = self.pop()
        if x < y:
            self.push(False)
        else:
            self.push(True)

    def greaterthan(self) -> None:
        x = self.pop()
        y = self.pop()
        if y > x:
            self.push(True)
        else:
            self.push(False)

    def lessthanequal(self) -> None:
        x = self.pop()
        y = self.pop()
        if x <= y:
            self.push(False)
        else:
            self.push(True)

    def greaterthanequal(self) -> None:
        x = self.pop()
        y = self.pop()
        if y >= x:
            self.push(True)
        else:
            self.push(False)

    def notequal(self) -> None:
        x = self.pop()
        y = self.pop()
        if x != y:
            self.push(True)
        else:
            self.push(False)







if __name__ == '__main__':
    a = StackOPS()
    a.push(15)
    a.push(17)
    print(a.stack)
    a.add()
    print(a.stack)  # we should see the sum of 15 and 17
    a.push(17)
    a.sub()
    print(a.stack)  # we should have 15 = 32 - 17
    a.push(3)
    a.mul()
    print(a.stack)  # we should have 15 * 3
    a.push(5)
    a.div()
    print(a.stack)  # we should have 9
    a.push(10)
    a.swap()
    print(a.stack)


