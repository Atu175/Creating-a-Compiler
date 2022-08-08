#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  adding and removing elements from a stack
# History:
#           2021-09-23, BRA, created


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        return self.stack

    def pop(self) -> object:
        a = len(self.stack)
        if a == 0:
            raise IndexError("Stack underflow")
        else:
            return self.stack.pop()


if __name__ == '__main__':
    s = Stack()
    s.push(15)
    x = s.pop()
    print(x)   # expect the integer 15 to be printed





