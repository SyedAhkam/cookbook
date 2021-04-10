# Use the builtin function `open`
#   open(FILE, mode=MODE) 
# Where:
#   FILE: filename of the file you wish to open
#   MODE: what mode to use while opening the file, defaults to `r`

file_name = 'test_file.txt'

# Simple write
file = open(file_name, mode='w') # returns a file object
file.write('Heyyyyyy')

file.close() # don't forget this

# Write using a context manager
with open(file_name, mode='w') as f: # here `f` is the file object
    f.write('Heyo')

# It's mostly preferred to use a context manager whenever we can
# Because it takes care of closing and releasing the file

# Write bytes
file = open(file_name, mode='wb') # [r]ead as [b]inary
file.write(bytearray([
    0x43,
    0x6f,
    0x6f,
    0x6c
])) 
file.close()

# Append to the end of file
# Use mode `a` instead of `w`
file = open(file_name, mode='a')
file.write('this will be appended to the file')

file.close()

# Create a file
# Use mode `x` to create a new file to write
# This will error out if the file already exists
file = open('new_file.txt', mode='x')
file.write('new')

file.close()
