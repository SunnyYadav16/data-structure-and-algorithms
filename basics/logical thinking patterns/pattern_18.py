"""
E
D E
C D E
B C D E
A B C D E
"""

rows = 5
end_char = ord("E")

for i in range(end_char, ord('A') - 1, -1):
    for j in range(i, end_char + 1):
        print(chr(j), end=" ")
    print()
