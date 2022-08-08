#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  A scanner/lexer for the RPLi interpreter
# History:
#           2021-09-30, BRA, downloaded from moodle and named the class Scanner2
#           2021-09-30, DMW, added the json library to process values and strings
#           2021-09-28, DMW, created this class from Scanner.py, updated it to use the Token class
#           2021-09-21, DMW, created

import shlex
from Token import Token
import json

class Scanner2:

    # 2021-09-30, DMW, updated the constructor for additional features and requirements for scanning
    def __init__(self, sourceText = None, keywords = "", includeTokenEOL = False, includeTokenEOF = False) -> None:
        # flags for the Scanner's configuration
        self.includeTokenEOL = includeTokenEOL
        self.includeTokenEOF = includeTokenEOF

        # save the keywords
        self.keywords = keywords

        # we have both raw tokens, and then annotated tokens
        self.tokens = []

        if sourceText is not None:
            if type(sourceText) == str:
                self.string2tokens(sourceText)
            elif type(sourceText) == list:
                self.list2tokens(sourceText)
            else:
                raise TypeError("Scanner source should be a list of strings, or a single string.")

    # 2021-09-30, DMW, added the objectType helper method to this class
    # provide a short string description of the object's type or class
    # for example, 'int', 'float', 'str', etc.
    def objectType(self, obj: any) -> str:
        s = str(type(obj)).split("'")[1]
        if '.' in s:
            return s.split('.')[1]
        return s

    # 2021-09-30, DMW, added this helper function that will help identifying literal strings
    # determine if the text passed in is a quoted string
    def isQuotedString(self, text):
        if text[0] == "'" and text[-1] == "'":
            return True
        elif text[0] == '"' and text[-1] == '"':
            return True
        return False


    def string2tokens(self, sourceText: str, lineNumber = 0) -> None:
        # 2021-09-30, DMW, updated to include line number and position within line annotation for
        position = 1
        tout = []

        final_token = None
        if self.includeTokenEOL:
            if sourceText[-1] == '\n':  # this is lexical analysis, looking for new line at the end of string
                final_token = "EOL"

        rawTokens = list(shlex.shlex(sourceText, punctuation_chars=True))
        for i in range(0, len(rawTokens)):
            token = rawTokens[i]
            tType = None  # the default token type is none

            if rawTokens[i] in self.keywords:
                value = None
                tType = "keyword"
            elif self.isQuotedString(rawTokens[i]):
                value = rawTokens[i][1:-1]
                tType = "str"
            else:
                try:
                    value = json.loads(rawTokens[i])
                    tType = self.objectType(value)
                except json.decoder.JSONDecodeError as ex:
                    value = None  # unrecognized object -- SYNTAX ERROR
                    tType = "error"

            tToken = Token(rawTokens[i], value, tType, lineNumber, position)
            self.tokens.append(tToken)

            position += 1

        if self.includeTokenEOL:
            if final_token is not None:
                tToken = Token(final_token, None,'keyword', lineNumber, position)
                self.tokens.append(tToken)

    def list2tokens(self, sourceText: list) -> None:
        line = 1
        for token in sourceText:
            self.string2tokens(token, lineNumber = line)
            line += 1

        if self.includeTokenEOF:
            t = Token("EOF", None, "keyword", line, 1)
            self.tokens.append(t)

    def printTokenList(self):
        print("[")
        for t in self.tokens:
            print("\t{}".format(t))
        print("]")

# limited testing
if __name__ == "__main__":
    a = Scanner2("this is a test")
    a.printTokenList()
    b = Scanner2(['4 5 +', '3 7 +', '/', '"\n"'])
    #print(b.rawTokens)
    b.printTokenList()
    c = Scanner2('"this is a test"')
    print(c.tokens)
