"""
A
B B
C C C
D D D D
E E E E E
"""

rows = 5

for i in range(rows):
    start_char = chr(ord('A') + i)
    for j in range(i+1):
        print(start_char, end=' ')
    print()