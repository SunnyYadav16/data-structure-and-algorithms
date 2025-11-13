"""
A B C D E
A B C D
A B C
A B
A
"""

rows = 5

for i in range(rows):
    for j in range(rows-i):
        print(chr(ord('A') + j), end=' ')
    print()