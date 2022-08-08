#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  AST Node Class
# History:
#           2021-10-32, DMW, created

from anytree import NodeMixin, RenderTree


class ASTNODE(NodeMixin):
    def __init__(self, name: str, value=None, parent=None, children=None) -> None:
        self.name = name
        self.parent = parent

        if value:
            self.value = value

        if children:
            self.children = children


# limited functional testing
if __name__ == "__main__":
    root = ASTNODE("root")
    child2 = ASTNODE("child2")
    child3 = ASTNODE("child3")
    child = ASTNODE("child", parent=root, children=[child2, child3])
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
