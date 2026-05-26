'''
ASSIGNMENT no-1 : Using loop generate following patterns (17 Aug):
'''
# 1. Pattern 1
print('Pattern 1')
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

print('Pattern 2')
#  2.pattern 2.
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#   3.pattern 3
print('Pattern 3')
row=5
for i in range(1,row + 1):
    print(" " * (row-i), end="")
    print("* " * i)

# pattern 4 .
print('Pattern 4')
for i in range(1, 5):
    print(" " * (6 - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 4) + "*")

print(" " * 2 + "******")
rws=5
for i in range(3):
    print(" " * (2 - i) + "*" + " " * rws + "*")
    rws += 2
