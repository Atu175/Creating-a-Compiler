# compilation of [test-lab1115-repeatuntil.pas] started at: 2021-11-23 14:24:12.031013

"""
program
└── compound_statement
    └── optional_statements
        └── statement_list
            ├── statement_list
            │   ├── statement_list
            │   │   └── statement
            │   │       └── assign_op
            │   │           ├── id(a)
            │   │           └── expression
            │   │               └── number
            │   └── statement
            │       └── repeat
            │           ├── statement_list
            │           │   ├── statement_list
            │           │   │   ├── statement_list
            │           │   │   │   ├── statement_list
            │           │   │   │   │   └── statement
            │           │   │   │   │       └── writeln
            │           │   │   │   │           └── expression
            │           │   │   │   │               └── id
            │           │   │   │   └── statement
            │           │   │   │       └── assign_op
            │           │   │   │           ├── id(a)
            │           │   │   │           └── expression
            │           │   │   │               └── add
            │           │   │   │                   ├── expression
            │           │   │   │                   │   └── id
            │           │   │   │                   └── expression
            │           │   │   │                       └── number
            │           │   │   └── statement
            │           │   │       └── assign_op
            │           │   │           ├── id(b)
            │           │   │           └── expression
            │           │   │               └── number
            │           │   └── statement
            │           │       └── repeat
            │           │           ├── statement_list
            │           │           │   ├── statement_list
            │           │           │   │   └── statement
            │           │           │   │       └── writeln
            │           │           │   │           └── expression
            │           │           │   │               └── id
            │           │           │   └── statement
            │           │           │       └── assign_op
            │           │           │           ├── id(b)
            │           │           │           └── expression
            │           │           │               └── add
            │           │           │                   ├── expression
            │           │           │                   │   └── id
            │           │           │                   └── expression
            │           │           │                       └── number
            │           │           └── expression
            │           │               └── =
            │           │                   ├── expression
            │           │                   │   └── id
            │           │                   └── expression
            │           │                       └── number
            │           └── expression
            │               └── =
            │                   ├── expression
            │                   │   └── id
            │                   └── expression
            │                       └── number
            └── statement
                └── writeln
                    └── expression
                        └── number
"""
a = 1
while True: 
    print(a)
    a = a + 1
    b = 1
    while True: 
        print(b)
        b = b + 1
        if b == 3 : break
    if a == 10 : break
print(999)


# compilation to [test-lab1115-repeatuntil.py] completed at: 2021-11-23 14:24:12.032011
# Elapsed time: 0:00:00.000998
