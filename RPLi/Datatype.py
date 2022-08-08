#  Author:  Brandon R. Atu & Colins
# College:  Berea College
#  Course:  CSC386
# Purpose:  return datatype
# History:
#           2021-09-22, BRA, created

from RPLi import Token


def objectType(object: any) -> str:
    a = str(type(object)).split("'")[1]
    if "." in a:
        return a.split(".")[1]
    return a


x = Token.Token()
print(objectType("1"))
print(objectType(x))
print(objectType(True))


