# compilation of [Lab1109_Test.pas] started at: 2021-11-11 21:57:11.022180

"""
program
└── compound_statement
    └── optional_statements
        └── statement_list
            ├── statement_list
            │   ├── statement_list
            │   │   ├── statement_list
            │   │   │   ├── statement_list
            │   │   │   │   ├── statement_list
            │   │   │   │   │   ├── statement_list
            │   │   │   │   │   │   ├── statement_list
            │   │   │   │   │   │   │   └── statement
            │   │   │   │   │   │   │       └── assign_op
            │   │   │   │   │   │   │           ├── id(a)
            │   │   │   │   │   │   │           └── expression
            │   │   │   │   │   │   │               └── sqrt
            │   │   │   │   │   │   │                   └── expression
            │   │   │   │   │   │   │                       └── number
            │   │   │   │   │   │   └── statement
            │   │   │   │   │   │       └── assign_op
            │   │   │   │   │   │           ├── id(b)
            │   │   │   │   │   │           └── expression
            │   │   │   │   │   │               └── sqrt
            │   │   │   │   │   │                   └── expression
            │   │   │   │   │   │                       └── sqrt
            │   │   │   │   │   │                           └── expression
            │   │   │   │   │   │                               └── sqrt
            │   │   │   │   │   │                                   └── expression
            │   │   │   │   │   │                                       └── number
            │   │   │   │   │   └── statement
            │   │   │   │   │       └── assign_op
            │   │   │   │   │           ├── id(c)
            │   │   │   │   │           └── expression
            │   │   │   │   │               └── power
            │   │   │   │   │                   ├── expression
            │   │   │   │   │                   │   └── number
            │   │   │   │   │                   └── expression
            │   │   │   │   │                       └── number
            │   │   │   │   └── statement
            │   │   │   │       └── assign_op
            │   │   │   │           ├── id(d)
            │   │   │   │           └── expression
            │   │   │   │               └── power
            │   │   │   │                   ├── expression
            │   │   │   │                   │   └── number
            │   │   │   │                   └── expression
            │   │   │   │                       └── power
            │   │   │   │                           ├── expression
            │   │   │   │                           │   └── number
            │   │   │   │                           └── expression
            │   │   │   │                               └── number
            │   │   │   └── statement
            │   │   │       └── writeln
            │   │   │           └── expression
            │   │   │               └── id
            │   │   └── statement
            │   │       └── writeln
            │   │           └── expression
            │   │               └── id
            │   └── statement
            │       └── writeln
            │           └── expression
            │               └── id
            └── statement
                └── writeln
                    └── expression
                        └── id
"""
a = (16 ** 0.5)
b = (((256 ** 0.5) ** 0.5) ** 0.5)
c = 2 ** 3
d = 2 ** 2 ** 2
print(a)
print(b)
print(c)
print(d)


# compilation to [lab1109_test.py] completed at: 2021-11-11 21:57:11.024174
# Elapsed time: 0:00:00.001994
