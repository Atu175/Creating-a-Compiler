#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  A class for Interpreting tokens
# History:
#           2021-10-07, BRA, extra credit
#           2021-10-07, BRA, add stack method and keyword
#           2021-10-07, BRA, add false keyword
#           2021-10-07, BRA, add true keyword
#           2021-10-07, BRA, added == keyword
#           2021-10-07, BRA, added kw_pi method and pi keyword
#           2021-10-01, DMW, added code block capabilities
#           2021-09-30, DMW, created

from Scanner2_atub import Scanner2
from StackOPS import StackOPS
import math


class Interpreter:

    def __init__(self, source = None) -> None:
        self.line = 0
        self.position = 0
        self.source = source
        self.stack = StackOPS()
        self.keywords = {
            "+": self.stack.add,
            "-": self.stack.sub,
            "*": self.stack.mul,
            "/": self.stack.div,
            "swap": self.stack.swap,
            "swp": self.stack.swap,
            "print": self.printTOS,
            "pi": self.kw_pi,   # pi keyword
            "==": self.stack.equal,   # equal keyword
            "true": self.stack.true,   # true keyword
            "false": self.stack.false,  # true keyword
            "if":  self.kw_if,
            "stack": self.kw_print_stack,  # stack keyword
            "<": self.stack.lessthan,
            ">": self.stack.greaterthan,
            "<=": self.stack.lessthanequal,
            ">=": self.stack.greaterthanequal,
            "!=": self.stack.notequal
        }

        keywords = self.keywords.keys()
        self.scanner = Scanner2(source, keywords)

        # post scanner annotation of tokens with functions
        for t in self.scanner.tokens:
            if t.data_type  == "keyword":
                t.function = self.keywords[t.name]

        # execute the program
        self.rpl_eval(self.scanner.tokens)

    # 2021-10-01, DMW, raise code block exception
    def raiseCodeBlockException(self):
        raise ValueError("Close block encountered with Open block in line {} at position {}.".format(self.line, self.position))

    # ------------------------------------------  This is the actual interpreter
    # 2021-10-01, DMW, an evaluation function that evaluates tokens
    def rpl_eval(self, tokens):
        # run the program
        for t in tokens:
            self.line = t.line
            self.position = t.pos
            if t.data_type == "keyword":
                self.keywords[t.name]()
            elif t.data_type == "error":
                # TODO: code for syntax error needs to be added
                pass
            else:
                self.stack.push(t.value)

    # print keyword function implementation
    def printTOS(self):
        print(self.stack.stack[-1])

    # pi method
    def kw_pi(self) -> None:
        self.stack.push(math.pi)

    # if method
    def kw_if(self) -> None:
        if len(self.stack.stack) < 3:
            raise IndexError("Insufficient operands for if")
        else:
            x = self.stack.pop()
            y = self.stack.pop()
            z = self.stack.pop()
            if x == "true":
                self.stack.push(z)
            else:
                self.stack.push(y)

    # stack method
    def kw_print_stack(self) -> None:
        print(self.stack.stack)



if __name__ == "__main__":
    i = Interpreter("'ABCD' 4 5 + print")
    i.scanner.printTokenList()
    print(i.stack.stack)

