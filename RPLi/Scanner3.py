#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  A scanner/lexer for the RPLi interpreter
# History:
#           2021-09-21, DMW, created

import shlex
from Token import Token

class Scanner:

    def __init__(self, sourceText = None) -> None:
        if sourceText is not None:
            self.rawTokens = []
            if type(sourceText) == str:
                self.string2tokens(sourceText)
            elif type(sourceText) == list:
                self.list2tokens(sourceText)
            else:
                raise TypeError("Scanner source should be a list of strings, or a single string.")

    def string2tokens(self, sourceText: str) -> None:
        tout = []
        tokens = shlex.shlex(sourceText, punctuation_chars=True)
        for token in tokens:
            t = Token(token)
            tout.append(t)
        self.rawTokens += tout

    def list2tokens(self, sourceText: list) -> None:
        for token in sourceText:
            self.string2tokens(token)

# limited testing
if __name__ == "__main__":
    a = Scanner("this is a test")
    print(a.rawTokens)
    b = Scanner(['4 5 +', '3 7 +', '/', '"\n"'])
    print(b.rawTokens)
    c = Scanner('"this is a test"')
    print(c.rawTokens)
