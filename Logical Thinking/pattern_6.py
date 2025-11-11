"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

rows = 5

for i in range(rows):
    for j in range(1, rows-i+1):
        print(j, end=" ")
    print()