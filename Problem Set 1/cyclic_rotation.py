# Jeffrey Bolk
# 2026-11-03
# Rotate an array to the right by a given value

import random

# Array rotation function
def cyclic_rotation(a = [], k=0):

    # Repeat for number of rotations
    for x in range(k):
        
        # Save last value in arr
        make_first_num = a[len(a) - 1]

        # Rotate arr to the right
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i - 1]

        # Assign first value of arr to last value
        a[0] = make_first_num

    # Return rotated array
    return a


# Test Variables
rotation = 5
myArr = []
for i in range(1, 101):
    myArr.append(random.randrange(100))

# Original array myArr
print(f'\n\nOriginal Array:\n{myArr}')
for i in range(0, len(myArr)):
    print(f'Entry {i+1}: {myArr[i]}')

# Call function
myArr = cyclic_rotation(myArr, rotation)

# Print numbers shifted by rotation
print(f'\n\nArray rotated by {rotation}\n{myArr}')
for i in range(0, len(myArr)):
    print(f'Entry {i+1}: {myArr[i]}')
