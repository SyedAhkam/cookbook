# `sys` module is part of the standard library
import sys 

# Like in c, you have `argv`
print(sys.argv)

# To get `argc`, like in c
argc = len(sys.argv)

# First element of `argv` is always the executable name
exec_name = sys.argv[0]

# As argv is a list, we can iterate over it
for arg in sys.argv:
    print(arg)

# Todo advanced argument and flag parsing, use `argparse` module
# `argparse` is only supported on python 3.2+
# On later versions, use `getopt`
