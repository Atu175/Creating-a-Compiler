#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Read in a file's lines
# History:
#           2021-09-30, BRA, downloaded from moodle and named the class ReadFile1
#           2021-09-21, DMW, stronger typing added where appropriate
#           2021-09-08, DMW, created

class ReadFile1:
    rawData = []
    rawLines = 0
    error = False
    errorMessage = ""
    sourceFileName = ""

    # this is the class constructor function
    def __init__(self, sourceFileName: str = ""):
        # this code was added for REPL support
        if len(sourceFileName) == 0:
            return

        self.readFile(sourceFileName)

    def readFile(self, sourceFileName: str) -> None:
        self.sourceFileName = sourceFileName
        try:
            sourceFile = open(sourceFileName, "r")
            self.rawData = sourceFile.readlines()
            sourceFile.close()
            self.rawLines = len(self.rawData) # the number of source file lines
        except IOError as ex:
            self.error = True
            self.errorMessage = str(ex)


if __name__ == "__main__":
    # limited simple testing
    p = ReadFile1("test-data.txt")
    print(p.rawData)
    print(p.error)
    print(p.errorMessage)
