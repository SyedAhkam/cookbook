# The syntax of while loops is
#   while CONDITION:
#       CODE

# The CONDITION should return a boolean value ie True and False

# Loop over `x` number of times
x = 10
i = 0

while i < x:
    print(i)
    i += 1

# Loop over an array
array = ['one', 'two', 'three']
i = 0

# Make sure to increment `i` at last, or you will end up with an infinite loop

# Intentional infinite loop
while i < len(array):
    print(array[i])
    i += 1

