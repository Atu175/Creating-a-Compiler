#  Author:  Brandon R. Atu
# College:  Berea College
#  Course:  CSC386
# Purpose:  To hold tokens
# History:
#           2021-09-22, BRA, created
#           2021-09-27, BRA, extra credit part


class Token:
    def __init__(self, name=None, value=None, data_type=None, line=None, pos=None, function=None):
        self.name = name
        self.value = value
        self.data_type = data_type
        self.line = line
        self.pos = pos
        self.function = function

    def __str__(self):
        return ("Token < name =" + self.name + ", value =" + str(self.value) + ", data_type =" + str(self.data_type) +
                ", line =" + str(self.line) + ", pos =" + str(self.pos) + ", function =" + str(self.function) + ">")


if __name__ == '__main__':
    t1 = Token("4")
    print(t1)
    t2 = Token("+", value=None, data_type="keyword", line=0, pos=1, function=None)
    print(t2)



