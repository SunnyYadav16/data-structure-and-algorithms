"""
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""

rows = 5

for i in range(rows):
    # space
    for left_space in range(rows-i-1):
        print(" ", end=" ")

    # ascending character
    for j in range(i + 1):
        print(chr(ord("A") + j), end=" ")

    # descending character
    for j in range(i, 0, -1):
        print(chr(ord("A") + j - 1), end=" ")

    # space
    for right_space in range(rows-i):
        print(" ", end=" ")

    print()