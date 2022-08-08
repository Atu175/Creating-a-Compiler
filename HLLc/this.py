# compilation of [test-sine.pas] started at: 2021-12-02 14:13:20.910119

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
            │   │   │               └── sin
            │   │   │                   └── expression
            │   │   │                       └── number
            │   │   └── statement
            │   │       └── assign_op
            │   │           ├── id(b)
            │   │           └── expression
            │   │               └── sin
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
a = math.sin(25)
b = math.sin(90)
print(a)
print(b)


# compilation to [this.py] completed at: 2021-12-02 14:13:20.910119
# Elapsed time: 0:00:00
