#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  The RPLi interpreter
# History:
#           2021-09-30, BRA, downloaded from moodle
#           2021-09-14, DMW, created

import sys
from CLA1 import CLA1
from ReadFile1 import ReadFile1
from Interpreter_atub import Interpreter

# this function will show an error message and the usage of the program
def usage(errorMessage):
    if errorMessage != "":
        print("Error: ", errorMessage,"\n")
    print("Usage:  python rpli.py [SOURCE_FILE_NAME]")
    print("Where:  SOURCE_FILE_NAME is the optional program source file")
    sys.exit(1)


# this is our main function
def main():
    cla = CLA1()
    if cla.argc < 2:
        usage("Required source file was not specified.")

    # complete this function
    f = ReadFile1(cla.argv[1])
    if f.error:
        usage("Source file is not found or cannot be read.")

    #print(cla.argv)
    #print(f.rawData)
    #print(f.rawData)
    i = Interpreter(f.rawData)


# execute our program
if __name__ == "__main__":
    main()
