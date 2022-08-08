#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Read in a file's lines
# History:
#           2021-10-14, DMW
#               now capture the raw text of the source text file in self.rawText;
#               moved class field initialization to the __init__ method;
#           2021-09-21, DMW, stronger typing added where appropriate
#           2021-09-08, DMW, created

class ReadFile:

    # this is the class constructor function
    def __init__(self, sourceFileName: str = ""):
        self.rawData = []
        self.rawText = ""
        self.rawLines = 0
        self.error = False
        self.errorMessage = ""
        self.sourceFileName = sourceFileName

        # this code was added for REPL support
        if len(sourceFileName) == 0:
            return

        self.readFile(sourceFileName)

    def readFile(self, sourceFileName: str) -> None:
        self.sourceFileName = sourceFileName
        try:
            sourceFile = open(sourceFileName, "r")
            self.rawText = sourceFile.read()  # 2021-10-14, DMW, added this to get full raw text
            # 2021-10-14, DMW, modification of readFile to have both the rawText and a list of lines
            #self.rawData = sourceFile.readlines()
            self.rawData = self.rawText.split('\n') # split text into a list of lines
            sourceFile.close()
            self.rawLines = len(self.rawData) # the number of source file lines
        except IOError as ex:
            self.error = True
            self.errorMessage = str(ex)


if __name__ == "__main__":
    # limited simple testing
    p = ReadFile("test-data.txt")
    print(p.rawData)
    print(p.error)
    print(p.errorMessage)
