# compilation of [test-whiledo.pas] started at: 2021-12-02 14:15:04.297976

"""
program
└── compound_statement
    └── optional_statements
        └── statement_list
            ├── statement_list
            │   ├── statement_list
            │   │   └── statement
            │   │       └── assign_op
            │   │           ├── id(b)
            │   │           └── expression
            │   │               └── number
            │   └── statement
            │       └── while
            │           ├── expression
            │           │   └── <
            │           │       ├── expression
            │           │       │   └── id
            │           │       └── expression
            │           │           └── number
            │           └── statement
            │               └── assign_op
            │                   ├── id(b)
            │                   └── expression
            │                       └── add
            │                           ├── expression
            │                           │   └── id
            │                           └── expression
            │                               └── number
            └── statement
                └── writeln
                    └── expression
                        └── id
"""
b = 1
while b < 10:
    b = b + 1

print(b)


# compilation to [test-whiledo.py] completed at: 2021-12-02 14:15:04.297976
# Elapsed time: 0:00:00
