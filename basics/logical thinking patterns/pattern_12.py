"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""

rows = 5
space = 2*(rows-1)

for i in range(rows):
    # numbers
    for j in range(1, i+1):
        print(j, end=" ")

    # spaces
    for space in range(1, space+1):
        print(" ", end=" ")

    # numbers
    for j in range(i, 0 ,-1):
        print(j, end=" ")

    space -= 2
    print()