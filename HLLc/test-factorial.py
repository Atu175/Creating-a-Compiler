# compilation of [test-factorial.pas] started at: 2021-12-02 14:23:39.622794

import math 
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
            │   │   │               └── factorial
            │   │   │                   └── expression
            │   │   │                       └── number
            │   │   └── statement
            │   │       └── assign_op
            │   │           ├── id(b)
            │   │           └── expression
            │   │               └── factorial
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
a = math.factorial(5)
b = math.factorial(10)
print(a)
print(b)


# compilation to [test-factorial.py] completed at: 2021-12-02 14:23:39.622794
# Elapsed time: 0:00:00
