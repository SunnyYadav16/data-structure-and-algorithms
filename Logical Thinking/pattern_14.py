"""
A
A B
A B C
A B C D
A B C D E
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')
    print()