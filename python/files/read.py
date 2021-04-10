# Use the builtin function `open`
#   open(FILE, mode=MODE) 
# Where:
#   FILE: filename of the file you wish to open
#   MODE: what mode to use while opening the file, defaults to `r`

file_name = 'test_file.txt'

# Simple read
file = open(file_name) # returns a file object
contents = file.read()

file.close() # don't forget this

# Read using a context manager
with open(file_name) as f: # here `f` is the file object
    contents = f.read()
    print(contents)

# It's mostly preferred to use a context manager whenever we can
# Because it takes care of closing and releasing the file

# Read bytes
file = open(file_name, mode='rb') # [r]ead as [b]inary
bytes = file.read() # reads `512` bytes by default

# To read manual number of bytes, `file.read(number_of_bytes)`

# Read line by line
with open(file_name) as f:
    lines = f.readlines()
    
    for line in lines:
        print(line)
