#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  Test making an AST, based on Empty-Compiler.py
# History:
#           2021-10-26, DMW, updated this file to emit Python code during an in class demonstration
#           2021-10-21, DMW, created

from CLA import CLA
from ReadFile import ReadFile
from ply import lex
from anytree import RenderTree
from ASTNODE import ASTNODE

# ---------------------------------------------------------------- LEXER essentials

# a dictionary of reserved word and TOKEN key : value pairs
reserved_words = {
    "begin": 'BEGIN',
    "end": 'END'
}

# these tokens are from dynamic content that is part of a program
# a list or tuple of tokens is required
tokens = [
    'ASSIGNOP',
    'ID',
    'NUMBER'
]

# create a single list of tokens and reserved words (which are also tokens)
tokens += list(reserved_words.values())

literals = ['.', ';']

# token definitions, simple tokens a single regular expression is enough

t_ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_BEGIN(t):
    r'begin'
    return t


def t_END(t):
    r'end'
    return t


def t_ASSIGNOP(t):
    ":="
    return t


# complex tokens can be described using a function
def t_NUMBER(t):
    # this code works for all numbers
    # 2021-05-29, DMW, regular expression is from:
    # https://www.regular-expressions.info/floatingpoint.html
    r'[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    try:
        t.value = int(t.value)
    except ValueError as ex:
        t.value = float(t.value)
    return t


# Error handling rule, this rule is required
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Define a rule so we can track line numbers
# this rule isn't required, but it is useful to have
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
# this token rule isn't required, but is useful to have
t_ignore = ' \t'


# Build the lexer
lexer = lex.lex()

# ---------------------------------------------------------------- Grammar - Productions
start = "program"


def p_program(p):
    "program : compound_statement '.'"
    global root
    root = p[0] = ASTNODE("program", children=[p[1]])


def p_identifier_list(p):
    """identifier_list : ID"""
    p[0] = ASTNODE("identifier_list", children=[p[1]])


def p_identifier_list2(p):
    """identifier_list : identifier_list ',' ID"""
    p[0] = ASTNODE("identifier_list", children=[p[1], p[3]])


def p_compound_statement(p):
    '''compound_statement : BEGIN optional_statements END'''
    p[0] = ASTNODE("compound_statement", children=[p[2]])


# 2021-10-21, DMW, the empty rule from the manual
def p_empty(p):
    'empty :'
    p[0] = ASTNODE("empty")


def p_optional_statements(p):
    """optional_statements : statement_list"""
    p[0] = ASTNODE("optional_statements", children=[p[1]])


def p_optional_statements2(p):
    """optional_statements : empty"""
    p[0] = ASTNODE("optional_statements", children=[p[1]])


def p_statement_list(p):
    """statement_list : statement"""
    p[0] = ASTNODE("statement_list", children=[p[1]])
    #p[0] = p[1]


def p_statement_list2(p):
    """statement_list : statement_list statement"""
    p[0] = ASTNODE("statement_list", children=[p[1], p[2]])


def p_statement(p):
    """statement : ID ASSIGNOP expression ';'"""
    id_node = ASTNODE("id"+"("+p[1]+")", value=p[1])
    p[0] = ASTNODE("statement", children=[ASTNODE("assign_op", children=[id_node, p[3]])])


def p_statement_cs(p):
    """statement : compound_statement ';'"""
    p[0] = ASTNODE("statement", children=[p[1]])


def p_expression_number(p):
    "expression : NUMBER"   # expression --> NUMBER
    p[0] = ASTNODE("expression", children=[ASTNODE("number", value=p[1])])


# a p_error(p) rule is required
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


# ---------------------------------------------------------------- Code for Using the LEXER

# a method that helps the user understand how to use the example
def usage(mesg: str = "") -> None:
    if mesg != "":
        print("Error:  {}\n".format(mesg))
    print("Usage:  python lex.py SOURCE_FILE_NAME [OUTPUT_FILE_NAME]")
    print("Where:  SOURCE_FILE_NAME is a source text file.")
    print("        OUTPUT_FILE_NAME is the optional compiled output file name.")
    quit(1) # exit with error status 1


import ply.yacc as yacc
parser = yacc.yacc()

# ---------------------------------------------------------------- emit_code()


def emit_code(node: ASTNODE) -> None:
    def follow_children(nodes: list):
        if not None and len(nodes) > 0:
            for node in nodes:
                emit_code(node)

    def emit_expr(node: ASTNODE) -> None:
        if node.name == "expression":
            if node.children:
                for n in node.children:
                    emit_expr(n)
        if node.name == "number":
            print(node.value)

    if node.name == "program" or node.name == "compound_statement"\
            or node.name == "statement_list" or node.name == "optional_statements":
        follow_children(node.children)
    elif node.name == "statement":
        follow_children(node.children)
    elif node.name == "assign_op":
        id_node = node.children[0]
        print(id_node.value, "=", end=' ')
        expr = node.children[1]
        emit_expr(expr)

    return



# ---------------------------------------------------------------- main()
def main():
    global root
    args = CLA()
    if args.argc < 2:
        usage("Required source text file was not specified.")

    f = ReadFile(args.argv[1])
    if f.error:
        usage("Error reading file:  {}".format(f.sourceFileName))

    #lexer.input(f.rawText)

    # Tokenize
    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #        break # No more input
    #    print(tok)

    #while True:
    #    try:
    #        s = input('calc > ')
    #    except EOFError:
    #        break
    #
    #    if not s:
    #        continue
    #
    #    yacc.parse(s)

    yacc.parse(f.rawText)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    # output target code
    emit_code(root)

# here's where we'll test our example lexer
if __name__ == "__main__":
    root = ASTNODE("root") # create the root of the AST
    main() # execute the main function
