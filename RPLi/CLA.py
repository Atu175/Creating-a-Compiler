#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Saves command line arguments
# History:
#           2021-09-14, BRA, created

import sys


class CLA:
    def __init__(self):
        self.num = len(sys.argv)
        self.list = str(sys.argv)


if __name__ == "__main__":
    x = CLA()
    print("Number of arguments:", x.num)
    print("Argument list:", x.list)


