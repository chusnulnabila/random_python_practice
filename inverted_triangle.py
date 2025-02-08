# Inverted Triangle Python Program

print('  ###  Inverted Triangle  ###  ')
print('===============================')

length = int(input('Please input length of triangle: '))
print()

for i in range(length):
    for j in range(length-i):
        print(' *', end='')
    print()


# dengan menggunalan satu for loop
# for i in range(length):
#     print(' *' * (length-i))