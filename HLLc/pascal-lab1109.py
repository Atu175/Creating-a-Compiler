#  Author:  Deanna M. Wilborne
# College:  Berea College
#  Course:  CSC386 Fall 2021
# Purpose:  The Pascal Compiler Final Project
# History:
#           2021-12-02, BRA, implementing the factorial function
#           2021-12-01, BRA, implementing the ifthen function
#           2021-11-27, BRA, implementing sine function
#           2021-11-23, BRA, implementing while do
#           2021-11-22, BRA, implementing repeat until
#           2021-11-18, BRA, detect naming errors during compilation
#           2021-11-16, BRA, shortened the code by removing the elif and adding a dictionary
#           2021-11-15, BRA, add UPLUS, less than or equal to, greater than equal to and not equal to
#           2021-11-11, BRA, add grouping and UMINUS
#                       BRA, add less than, greater than, and equal to
#                       BRA, added power and sqrt functions
#           2021-11-04, DMW, add the ability to print expressions in the target language (team 11.04);
#                       DMW, added -, *, / production rule handlers and expression emitters
#           2021-11-02, DMW, add the ability to add expressions
#           2021-10-28, DMW, modified simple-ast.py to solve the lab 10.28
#           2021-10-26, DMW, updated this file to emit Python code during an in class demonstration
#           2021-10-21, DMW, created

from CLA import CLA
from ReadFile import ReadFile
from ply import lex
from anytree import RenderTree
from ASTNODE import ASTNODE
import os  # 2021-10-28, DMW, this is needed to process file names
import datetime  # 2021-11-09, necessary for calculation of compile time.

# ---------------------------------------------------------------- LEXER essentials

# a dictionary of reserved word and TOKEN key : value pairs
# 2021-11-11, BRA, added power and sqrt as keywords
# 2021-11-22, BRA, added until and repeat to the keywords
reserved_words = {
    "begin": 'BEGIN',
    "end": 'END',
    "writeln": 'WRITELN',
    "power": 'POWER',
    "sqrt": 'SQRT',
    "repeat": 'REPEAT',
    "until": 'UNTIL',
    "while": 'WHILE',
    "do": 'DO',
    "sin": 'SIN',
    "ifthen": 'IFTHEN',
    "factorial": 'FACTORIAL'

}

# these tokens are from dynamic content that is part of a program
# a list or tuple of tokens is required
tokens = [
    'ASSIGNOP',
    'ID',
    'LTE',
    'GTE',
    'NET',
    'NUMBER'
]

# create a single list of tokens and reserved words (which are also tokens)
tokens += list(reserved_words.values())

# 2021-11-04, DMW, added the literal tokens ( and )
# 2021-11-02, DMW, added the literal tokens +, -, /, *
# 2021-11-11, BRA, added the literal token ,
literals = ['.', ';', '+', '-', '*', '/', '(', ')', '%', '^', '=', ',', '<', '>']


# token definitions, simple tokens a single regular expression is enough

#t_ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_BEGIN(t):
    r'begin'
    return t


def t_END(t):
    r'end'
    return t


# 2021-11-04, DMW, added
def t_WRITELN(t):
    r'writeln'
    return t


# 2021-11-11, BRA, added power
def t_POWER(t):
    r'power'
    return t


# 2021-11-11, BRA, added sqrt
def t_SQRT(t):
    r'sqrt'
    return t


# 2021-12-01, BRA, added ifthen
def t_IFTHEN(t):
    r'ifthen'
    return t


# 2021-12-02, BRA, added factorial
def t_FACTORIAL(t):
    r'factorial'
    return t


# 2021-11-27, BRA, added sin
def t_SIN(t):
    r'sin'
    return t


# 2021-11-15, BRA, added less that equal
def t_LTE(t):
    "<="
    return t


# 2021-11-15, BRA, added greater that equal
def t_GTE(t):
    ">="
    return t


# 2021-11-15, BRA, added not equal to
def t_NET(t):
    "<>"
    return t


def t_ASSIGNOP(t):
    ":="
    return t


# 2021-11-22, BRA, added repeat
def t_REPEAT(t):
    r'repeat'
    return t


# 2021-11-22, BRA, added until
def t_UNTIL(t):
    r'until'
    return t


# 2021-11-23, BRA, added while
def t_WHILE(t):
    r'while'
    return t


# 2021-11-23, BRA, added do
def t_DO(t):
    r'do'
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


# 2021-10-28, DMW, find the column position in the text for lexical errors
# this is based on the documentation from the manual of PLY
def find_column(token) -> int:
    global input_source
    line_start = input_source.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Error handling rule, this rule is required
def t_error(t):
    print("Syntax error at '{}' at column {} in line number {}".format(t.value[0], find_column(t), t.lineno))
    quit(1)


# 2021-11-11, DMW, added
def t_INLINE_COMMENT(t):
    r'//.*'
    pass  # consume the inline comment rather than creating a token


# 2021-11-11, DMW, added
# the following is for C, C++ block comments from the Ply Documentation
# http://www.dabeaz.com/ply/ply.html#ply_nn21
#    r'(/\*(.|\n)*?\*/)|(//.*)'
# this regular expressions is modified for Pascal style block comments

def t_BLOCK_COMMENT(t):
    r'(\(\*(.|\n)*?\*\))'
   # consume the block comment, this way it can appear anywhere
    t.lexer.lineno += t.value.count("\n")  # add all the linefeeds in the block comment to the line count


# Define a rule so we can track line numbers
# this rule isn't required, but it is useful to have
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# 2021-11-02, DMW, converted to a method for including source line number in the token
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.lineno = t.lexer.lineno
    return t


# A string containing ignored characters (spaces and tabs)
# this token rule isn't required, but is useful to have
t_ignore = ' \t'


# Build the lexer
lexer = lex.lex()


# ---------------------------------------------------------------- Grammar - Productions
precedence = (
    ('nonassoc', '=', '<', '>', 'LTE', 'GTE', 'NET'),
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
    ('right', '^'),
    ('right', 'UMINUS', 'UPLUS')   # 2021-11-11, BRA, added unary minus and unary plus
)

global imports
imports = []

start = "program"


def p_program(p):
    "program : compound_statement '.'"
    global root
    root = p[0] = ASTNODE("program", children=[p[1]])


# TODO:  2021-11-09, DMW, we need to implement ID lists in the future, time permitting
#def p_identifier_list(p):
#    """identifier_list : ID"""
#    p[0] = ASTNODE("identifier_list", children=[p[1]])
#
#
#def p_identifier_list2(p):
#    """identifier_list : identifier_list ',' ID"""
#    p[0] = ASTNODE("identifier_list", children=[p[1], p[3]])


def p_compound_statement(p):
    '''compound_statement : BEGIN optional_statements END'''
    p[0] = ASTNODE("compound_statement", children=[p[2]])


def p_id_expr(p):
    """expression : ID"""
    tmp_node = ASTNODE("id", value=p[1])
    p[0] = ASTNODE("expression", children=[tmp_node])


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


# 2021-11-08, DMW, moved ; statement separator to the statement list, where it belongs
def p_statement_list2(p):
    """statement_list : statement_list ';' statement"""
    p[0] = ASTNODE("statement_list", children=[p[1], p[3]])


# 2021-11-08, DMW, removed the terminating ;
# 2021-11-04, DMW, changed function name from p_statement()
def p_statement_asgn(p):
    """statement : ID ASSIGNOP expression"""
    id_node = ASTNODE("id"+"("+p[1]+")", value=p[1])
    p[0] = ASTNODE("statement", children=[ASTNODE("assign_op", children=[id_node, p[3]])])


# 2021-11-22, BRA, added the repeat statement
def p_statement_repeat(p):
    """statement : REPEAT statement_list UNTIL expression"""
    repeat_node = ASTNODE("repeat", children=[p[2], p[4]])
    p[0] = ASTNODE("statement", children=[repeat_node])


# 2021-11-23, BRA, added the while statement
def p_statement_while(p):
    """statement : WHILE expression DO statement"""
    while_node = ASTNODE("while", children=[p[2], p[4]])
    p[0] = ASTNODE("statement", children=[while_node])


# 2021-11-08, DMW, removed the terminating ;
# 2021-11-04, DMW, added the writeln statement
def p_statement_writeln(p):
    """statement : WRITELN '(' expression ')'"""
    p[0] = ASTNODE("statement", children=[ASTNODE("writeln", children=[p[3]])])


# 2021-11-08, DMW, removed the terminating ;
def p_statement_cs(p):
    """statement : compound_statement"""
    p[0] = ASTNODE("statement", children=[p[1]])


# ---------------------------------------------------------------- EXPRESSION Productions
# 2021-11-02, DMW, added binary operator expression production
# based on calc.py
def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '^' expression
                  | expression '%' expression '''
    if p[2] == "+":
        add_expr_node = ASTNODE("add", children=[ p[1], p[3] ])
        p[0] = ASTNODE("expression", children=[add_expr_node])
    elif p[2] == "-":
        add_expr_node = ASTNODE("sub", children=[ p[1], p[3] ])
        p[0] = ASTNODE("expression", children=[add_expr_node])
    elif p[2] == "*":
        add_expr_node = ASTNODE("mul", children=[ p[1], p[3] ])
        p[0] = ASTNODE("expression", children=[add_expr_node])
    elif p[2] == "/":
        add_expr_node = ASTNODE("div", children=[ p[1], p[3] ])
        p[0] = ASTNODE("expression", children=[add_expr_node])
    elif p[2] == '^':
        expo_node = ASTNODE("expo", children=[p[1], p[3]])
        p[0] = ASTNODE("expression", children=[expo_node])
    elif p[2] == '%':
        mod_node = ASTNODE("mod", children=[p[1], p[3]])
        p[0] = ASTNODE("expression", children=[mod_node])


# 2021-11-11, BRA, added the power production
def p_expression_power(p):
    """expression : POWER '(' expression ',' expression ')'"""
    power_node = ASTNODE("power", children=[p[3], p[5]])
    p[0] = ASTNODE("expression", children=[power_node])


# 2021-11-11, BRA, added the sqrt production
def p_expression_sqrt(p):
    """expression : SQRT '(' expression ')'"""
    sqrt_node = ASTNODE("sqrt", children=[p[3]])
    p[0] = ASTNODE("expression", children=[sqrt_node])


# 2021-12-01, BRA, added the ifthen production
def p_expression_ifthen(p):
    """expression : IFTHEN '(' expression ',' expression ',' expression ')'"""
    ifthen_node = ASTNODE("ifthen", children=[p[3], p[5], p[7]])
    p[0] = ASTNODE("expression", children=[ifthen_node])


# 2021-11-27, BRA, added the sin production
def p_expression_sin(p):
    """expression : SIN '(' expression ')'"""
    sin_node = ASTNODE("sin", children=[p[3]])
    p[0] = ASTNODE("expression", children=[sin_node])
    imports.append("sin")


# 2021-12-02, BRA, added the sin production
def p_expression_factorial(p):
    """expression : FACTORIAL '(' expression ')'"""
    factorial_node = ASTNODE("factorial", children=[p[3]])
    p[0] = ASTNODE("expression", children=[factorial_node])
    imports.append("factorial")


def p_expression_number(p):
    "expression : NUMBER"   # expression --> NUMBER
    num_node = ASTNODE("number", value=p[1])
    p[0] = ASTNODE("expression", children=[num_node])


def p_expression_group(p):
    """expression : '(' expression ')'"""
    group_expr_node = ASTNODE("group", children=[p[2]])
    p[0] = ASTNODE("expression", children=[group_expr_node])


def p_expression_uminus(p):
    """expression : '-' expression %prec UMINUS"""
    neg_one_node = ASTNODE("number", value=-1)
    mul_node = ASTNODE("mul", children=[neg_one_node, p[2]])
    p[0] = ASTNODE("expression", children=[mul_node])


# 2021-11-15, BRA, added uplus
def p_expression_uplus(p):
    """expression : '+' expression %prec UPLUS"""
    p[0] = ASTNODE("expression", children=[p[2]])


def p_expression_rel_op(p):
    """expression : expression '=' expression
                  | expression '<' expression
                  | expression '>' expression"""
    rel_op_node = ASTNODE(p[2], children=[ p[1], p[3]] )
    p[0] = ASTNODE("expression", children=[rel_op_node])


# 2021-11-15, BRA, added less than equal to
def p_expression_lte(p):
    """expression : expression LTE expression"""
    p[0] = ASTNODE("expression", children=[ASTNODE("lte", children=[p[1], p[3]])])


# 2021-11-15, BRA, added greater than equal to
def p_expression_gte(p):
    """expression : expression GTE expression"""
    p[0] = ASTNODE("expression", children=[ASTNODE("gte", children=[p[1], p[3]])])


# 2021-11-15, BRA, added not equal to
def p_expression_net(p):
    """expression : expression NET expression"""
    p[0] = ASTNODE("expression", children=[ASTNODE("net", children=[p[1], p[3]])])





# ---------------------------------------------------------------- Production ERROR during runtime
# 2021-10-28, DMW, quit when there's a production error
# a p_error(p) rule is required
def p_error(p):
    if p:
        print("Syntax error at '{}' in line number {}".format(p.value, p.lineno))
    else:
        print("Syntax error at EOF")
    quit(1)


# ---------------------------------------------------------------- Code for Using the LEXER

# 2021-10-28, DMW, updated usage() to include information about the output file name
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
# 2021-10-28, DMW, a helper function for emit_code; this isolates the global variable use to this single location
def write_code(s: str) -> None:
    global emit_file
    emit_file.write(s)
    # if "math." in s:    check this later
    #     print("yes")




check_list = []   # 2021-11-18, BRA, creating a list to store the node value
level = 0



def emit_code(node: ASTNODE) -> None:

    def follow_children(nodes: list):
        if not None and len(nodes) > 0:
            for node in nodes:
                emit_code(node)

    def emit_expr(node: ASTNODE) -> None:


        # 2021-11-16, BRA, added a list of node names
        node_names = ['add', 'sub', 'mul', 'div', '=', '<', '>', 'net', 'lte', 'gte', 'power', 'mod']
        # 2021-11-16, BRA, added keys to the node names
        node_keys = {'add': " + ", 'sub': " - ", 'mul': " * ", 'div': " / ", '=': " == ", '<': " < ",
                     '>': " > ", 'net': " != ", 'lte': " <= ", 'gte': " >= ", 'power': " ** ", 'mod': " % "}
        if node.name == "expression":
            if node.children:
                for n in node.children:
                    emit_expr(n)
        elif node.name == "number":
            write_code(str(node.value))  # 2021-10-28, DMW, modified for file output
        elif node.name in node_names:  # 2021-11-16, BRA, added the dictionary to take care of the operators
            lhs_node = node.children[0]
            emit_expr(lhs_node)
            write_code(node_keys[node.name])
            rhs_node = node.children[1]
            emit_expr(rhs_node)
        # elif node.name == "sub":  # 2021-11-04, DMW, added the sub(tract) node handler
        #     lhs_node = node.children[0]
        #     emit_expr(lhs_node)
        #     write_code(' - ')
        #     rhs_node = node.children[1]
        #     emit_expr(rhs_node)
        # elif node.name == "mul":  # 2021-11-04, DMW, added the mul(tiply) node handler
        #     lhs_node = node.children[0]
        #     emit_expr(lhs_node)
        #     write_code(' * ')
        #     rhs_node = node.children[1]
        #     emit_expr(rhs_node)
        # elif node.name == "div":  # 2021-11-04, DMW, added the div(ide) node handler
        #     lhs_node = node.children[0]
        #     emit_expr(lhs_node)
        #     write_code(' / ')
        #     rhs_node = node.children[1]
        #     emit_expr(rhs_node)
        elif node.name == "expo":
            left_child = node.children[0]
            emit_expr(left_child)
            write_code(" ** ")
            right_child = node.children[1]
            emit_expr(right_child)
        # 2021-11-04, BRA, handle emitting expressions for modulo
        # elif node.name == "mod":
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" % ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        elif node.name == "id":  # 2021-11-09, BRA, we're now using variable names in expressions
            # 2021-11-18, BRA, checking to see if the node value is in the list
            if node.value in check_list:
                write_code(node.value)
            else:
                raise NameError("NameError: Variable was not declared")

        elif node.name == "group":   # 2021-11-11, BRA, added grouping
            write_code('(')
            emit_expr(node.children[0])
            write_code(')')
        # elif node.name == "=":
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" == ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == "<":
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" < ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == ">":
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" > ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == "lte":   # 2021-11-15, BRA, added less than or equal node handler
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" <= ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == "gte":   # 2021-11-15, BRA, added greater than or equal node handler
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" >= ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == "net":   # 2021-11-15, BRA, added not equal node handler
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" != ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        # elif node.name == "power":  # 2021-11-11, BRA, handle emitting expressions with power
        #     left_child = node.children[0]
        #     emit_expr(left_child)
        #     write_code(" ** ")
        #     right_child = node.children[1]
        #     emit_expr(right_child)
        elif node.name == "sqrt":  # 2021-11-11, BRA, handle emitting expression with sqrt
            write_code('(')
            emit_expr(node.children[0])
            write_code(" ** 0.5")
            write_code(')')
        elif node.name == "sin":  # 2021-11-27, BRA, handle emitting expression with sin
            write_code('math.sin(')
            emit_expr(node.children[0])
            write_code(')')
        elif node.name == "ifthen":  # 2021-12-01, BRA, handle emitting expression with ifthen
            emit_expr(node.children[1])
            write_code(" if ")
            emit_expr(node.children[0])
            write_code(" else ")
            emit_expr(node.children[2])
        elif node.name == "factorial":  # 2021-12-02, BRA, handle emitting expression with factorial
            write_code('math.factorial(')
            emit_expr(node.children[0])
            write_code(')')


    global level

    if node.name == "program" or node.name == "compound_statement"\
            or node.name == "statement_list" or node.name == "optional_statements":
        follow_children(node.children)
    elif node.name == "statement":
        follow_children(node.children)
        write_code("\n")  # 2021-10-21, DMW add a linefeed after statements
    elif node.name == "assign_op":
        id_node = node.children[0]
        check_list.append(id_node.value)   # 2021-11-18, BRA, stores the left child
        write_code((level * "    ") + id_node.value + " = ")  # 2021-10-28, DMW, modified for file output
        expr = node.children[1]
        emit_expr(expr)
    # 2021-11-04, DMW, handle emitting expressions for the writeln statement
    elif node.name == "writeln":
        write_code(level * "    ")  # 2021-11-22, BRA, making sure it prints out multiple writeln
        write_code("print(")
        emit_expr(node.children[0])
        write_code(")")
    # 2021-11-22, BRA, handle emitting repeat until statement
    elif node.name == "repeat":
        write_code(level * "    " + 'while True: \n')
        level = level + 1
        emit_code(node.children[0])
        write_code(level * "    " + "if ")
        emit_expr(node.children[1])
        write_code(" : break")
        level = level - 1
    elif node.name == "while":
        whileLevel = 0
        write_code(whileLevel * "    " + 'while ')
        emit_expr(node.children[0])
        write_code(":\n")
        whileLevel = whileLevel + 1
        write_code(whileLevel * "    ")
        emit_code(node.children[1])
        whileLevel -= 1

    return


# ---------------------------------------------------------------- main()
def main():
    global root
    global emit_file
    global input_source

    args = CLA()
    if args.argc < 2:
        usage("Required source text file was not specified.")
    elif args.argc < 3:
        # 2021-10-27, DMW, based on:  https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python?rq=1
        output_file = os.path.splitext(args.argv[1])[0] + ".py"
    else:
        output_file = args.argv[2]

    input_file = args.argv[1]
    f = ReadFile(input_file)
    if f.error:
        usage("Error reading file:  {}".format(f.sourceFileName))

    input_source = f.rawText

    # debugging
    if False:
        lexer.input(f.rawText)
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break # No more input
            print(tok)
        quit(0)

    start_time = datetime.datetime.now()
    emit_file = open(output_file, "w", encoding="utf-8")
    write_code("# compilation of [{}] started at: {}\n\n".format(input_file, start_time))
    #yacc.parse(input_source, debug=1)  # extra debugging
    yacc.parse(input_source)
    if len(imports) > 0:
        write_code("import math \n")
    write_code('"""\n')
    for pre, fill, node in RenderTree(root):
        #print("%s%s" % (pre, node.name))
        write_code("{}{}\n".format(pre, node.name))
    write_code('"""\n')
    # output target code
    try:
        #emit_imports(required_imports)
        emit_code(root)
    except NameError as ex:
        print(str(ex))
    end_time = datetime.datetime.now()
    write_code("\n\n# compilation to [{}] completed at: {}".format(output_file, end_time))
    write_code("\n# Elapsed time: {}\n".format(str(end_time - start_time)))
    emit_file.close()



# here's where we'll test our example lexer
if __name__ == "__main__":
    emit_file = None
    root = None # create the root of the AST
    input_source = ""
    text_indent = 0  # this will keep track of the indentation level (if/else, etc.)
    main() # execute the main function





# ---------------------------------------------------------------- diagnostic code, save until later
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

