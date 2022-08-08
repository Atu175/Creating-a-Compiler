#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Creating class that reads a text file and runs it as a list
# History:
#           2021-09-09, BRA, created

class ReadFile:
    def __init__(self, filename):
        self.filename = filename

        try:
            my_file = open(filename, "r")
            self.x = my_file.readlines()
            #print(x)
        except:
            print("File doesn't exist")


if __name__ == "__main__":
    ReadFile('test-data.txt')
# test code is indented like this comment and follows the if statement
