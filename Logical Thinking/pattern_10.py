"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

rows = 5

for i in range(1, 2*rows-1 + 1):
    stars = i
    if i > rows: stars = 2*rows - i

    for j in range(1, stars+1):
        print("*", end=" ")
    print()