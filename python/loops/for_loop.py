# The syntax of for loops is
#   for SINGLE_ELEMENT in ITERABLE:
#       CODE
# Where:
#   SINGLE_ELEMENT: name of the element you want to run the code on
#   ITERABLE: any data type which is an iterable

# Loop over a list or array
array = ['one', 'two', 'three']

for element in array:
    print(element)

# Loop over `x` number of times
x = 5

for i in range(x):
    print(i)

# The `range(x)` returns an iterable of numbers, 
# starting from 0 by default, and increments by 1 by default
# and stops before the specified number (x)

# Loop over a string
string = 'Syed'

for char in string:
    print(char)

# Loop over a string by words
string = 'Hi, I am Syed'

words = string.split() # Split on the whitespace
for word in words:
    print(word)
