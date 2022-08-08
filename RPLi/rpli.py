#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  The RPLi interpreter
# History:
#           2021-09-14, BRA, created

import sys
import CLA
import ReadFile


def main():

    x = CLA.CLA()
    if x.num >= 2:
        y = ReadFile.ReadFile(sys.argv[1])


    else:
        print("Has less than 2 arguments")
        return
    print(str(sys.argv))
    print(y.x)


if __name__ == "__main__":
    main()