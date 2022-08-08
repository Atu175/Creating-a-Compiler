#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Command Line Arguments class
# History:
#           2021-09-30, BRA, downloaded from moodle and named the class CLA1
#           2021-09-08, DMW, created

import sys

class CLA1:
    def __init__(self):
        self.argc = len(sys.argv)
        self.argv = sys.argv

if __name__ == "__main__":
    cla = CLA1()
    print(cla.argc) # the number of items on the command line
    print(cla.argv) # the command line arguments
