#  ##  Python Program Triangle Number (DERET)  ##
# -----------------------------------------------
# Input = 6
#  1
#  2  3
#  4  5  6
#  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20 21

print(' ##  Python Program Triangle Number (DERET)  ##')
print('-----------------------------------------------')

length = int(input('Input = '))

k=1
for i in range(length):
    for j in range(i+1):
        print(f'{k:>2}', ' ', sep='', end='')
        k=k+1
    print()