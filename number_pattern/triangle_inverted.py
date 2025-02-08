#   ##  Python Program Inverted Triangle  ##
# -----------------------------------
# Input= 6

# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


print('  ##  Python Program Inverted Triangle  ##')
print('-----------------------------------')


length = int(input('Input= '))
print()

for i in range(length):
    for j in range(1, length-i+1):
        print(j,' ', sep='', end='')
    print()
