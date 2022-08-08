# compilation of [test-ifthen.pas] started at: 2021-12-02 14:27:33.881657

"""
program
└── compound_statement
    └── optional_statements
        └── statement_list
            ├── statement_list
            │   ├── statement_list
            │   │   ├── statement_list
            │   │   │   └── statement
            │   │   │       └── assign_op
            │   │   │           ├── id(a)
            │   │   │           └── expression
            │   │   │               └── ifthen
            │   │   │                   ├── expression
            │   │   │                   │   └── <
            │   │   │                   │       ├── expression
            │   │   │                   │       │   └── number
            │   │   │                   │       └── expression
            │   │   │                   │           └── number
            │   │   │                   ├── expression
            │   │   │                   │   └── number
            │   │   │                   └── expression
            │   │   │                       └── number
            │   │   └── statement
            │   │       └── assign_op
            │   │           ├── id(b)
            │   │           └── expression
            │   │               └── ifthen
            │   │                   ├── expression
            │   │                   │   └── =
            │   │                   │       ├── expression
            │   │                   │       │   └── number
            │   │                   │       └── expression
            │   │                   │           └── number
            │   │                   ├── expression
            │   │                   │   └── number
            │   │                   └── expression
            │   │                       └── number
            │   └── statement
            │       └── writeln
            │           └── expression
            │               └── id
            └── statement
                └── writeln
                    └── expression
                        └── id
"""
a = 3 if 1 < 2 else 4
b = 7 if 5 == 6 else 10
print(a)
print(b)


# compilation to [test-ifthen.py] completed at: 2021-12-02 14:27:33.881657
# Elapsed time: 0:00:00
