#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  Scanner that takes the source code from ReadFile class and break lines of text into a list of tokens
# History:
#           2021-09-16, BRA, created

import shlex


class Scanner:
    def __init__(self, source):
        self.rawTokens = []
        if type(source) == str:
            self.tokens = shlex.split(source)
            for x in self.tokens:
                self.rawTokens.append(x)
        elif type(source) == list:
            for i in range(len(source)):
                self.tokens = shlex.split(source[i])
                for y in self.tokens:
                    self.rawTokens.append([y])
        else:
            self.rawTokens.append(source)


if __name__ == '__main__':
    a = Scanner("This is a test")
    print(a.rawTokens)
    b = Scanner(['4 5 +', '3 7 +', '/', '"\n"'])
    print(b.rawTokens)




