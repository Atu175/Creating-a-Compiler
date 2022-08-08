#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  A class for organizing tokens
# History:
#           2021-09-30, BRA, downloaded from moodle
#           2021-09-30, DMW, updated to handle \n in strings to be printed
#           2021-09-19, DNW, added recurwsive prettify method
#           2021-09-18, DMW, created

class Token:

    def __init__(self, name = None, value=None, data_type=None, line=None, pos=None, function=None):
        self.name = name
        self.value = value
        self.data_type = data_type
        self.line = line
        self.pos = pos
        self.function = function

    #def __str__(self):
    #    return "Token<name={}, value={}, data_type={}, line={}, pos={}, function={}>".format(
    #            self.name, self.value, self.data_type, self.line, self.pos, self.function
    #        )

    # this helper function returns True if the type of an object is not None
    def is_not_none(self, x):
        return True if x is not None else False

    # 2021-09-30, DMW, added quoting of literal strings
    # this helper function provides special string conversion of data and quoting around
    # literal strings
    def make_str_var(self, varname: str, varval: any, quote_char = "'"):
        if self.is_not_none(varval):
            t = (quote_char + varval + quote_char) if type(varval) == str else str(varval)
            return " " + varname + "=" + t + " "
        else:
            return ""

    # 2021-09-30, DMW, a method to escape the escape character \ in strings
    def escape_string(self, s: str) -> str:
        if chr(10) in s:
            return s.replace(chr(10), chr(92)+"n")
        else:
            return s

    # 2021-09-30, DMW, modified this method to escape \ when dealing with strings
    # not a great implementation; simpler with use of helper functions above
    def __str__(self):
        s = "Token<"

        if type(self.name) == str:
            s += self.make_str_var("name", self.escape_string(self.name))
        else:
            s += self.make_str_var("name", self.name)

        if type(self.value) == str:
            s += self.make_str_var("value", self.escape_string(self.value))
        else:
            s += self.make_str_var("value", self.value)

        s += self.make_str_var("data_type", self.data_type)
        s += self.make_str_var("line", self.line)
        s += self.make_str_var("pos", self.pos)
        s += self.make_str_var("function", self.function)
        s+= ">"
        return s


if __name__ == '__main__':
    t1 = Token("4")
    print(t1)
    t2 = Token("+", value=None, data_type="keyword", line=0, pos=1, function = None)
    print(t2)
    # 2021-09-30, DMW, added this test case for special line feed literal strings
    t3 = Token('"\n"', value='"\n"', data_type='str')
    print(t3)

