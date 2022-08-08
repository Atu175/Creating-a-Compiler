#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  A class for Interpreting tokens
# History:
#           2021-09-30, BRA, created

from Scanner import Scanner2
from StackOPS import StackOPS
from Token import Token


class Interpreter:

    def __init__(self, source = None) -> None:  # returns nothing and = means the source is optional
        self.source = source
        self.stack = StackOPS()
        self.keywords = {
            "+": self.stack.add,
            "-": self.stack.sub,
            "*": self.stack.mul,
            "/": self.stack.div,
            "swap": self.stack.swap,
            "print": self.printTOS

            # to do, add pi as a keyword, add more stuffs to the operator and more things to the interpreter
        }

        keywords = list(self.keywords.keys())
        #keywords = (self.keywords.keys()
        self.scanner = Scanner2(source, keywords)

        # post scanner annotation of functions
        for t in self.scanner.tokens:
            if t.data_type == "keyword":
                t.function = self.keywords[t.name]

        # run the program
        for t in self.scanner.tokens:
            if t.data_type == "keyword":
                self.keywords[t.name]()  # returns a function and () executes the function
            elif t.data_type == "error":
                pass
            else:
                self.stack.push(t.value)

    # print keyword function implementation
    def printTOS(self):
        print(self.stack.stack[-1])


if __name__ == '__main__':
    i = Interpreter("4 5 + print")
    i.scanner.printTokenList()
    #print(i.stack.stack)







