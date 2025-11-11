"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

rows = 5

# Upward Triangle
for i in range(rows):
    for left_space in range(rows-i-1):
        print(" ", end=" ")

    for j in range(2*i + 1):
        print("*", end=" ")

    for right_space in range(rows-i-1):
        print(" ", end=" ")
    print()

# Downward Triangle
for i in range(rows):
    for left_space in range(i):
        print(" ", end=" ")

    for j in range(2*rows - (2*i + 1)):
        print("*", end=" ")

    for right_space in range(i):
        print(" ", end=" ")
    print()