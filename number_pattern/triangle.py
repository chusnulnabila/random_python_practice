# OUTPUT
  ##  Python Program to Make Triangle Number  ##
# ------------------------------------------------
# Input number = 3

# 1
# 1 2
# 1 2 3


print('  ##  Python Program to Make Triangle Number  ##')
print('------------------------------------------------')

number = int(input('Input number = '))
print()

for i in range(1, number+1):
    for j in range(1, i+1):
        print(j,' ', end='', sep='')
    print()