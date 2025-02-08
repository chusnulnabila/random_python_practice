print('  ###  Square pattern  ###')
print('--------------------------')

length = int(input('Input: '))
print()

for i in range(1,length+1):
    for j in range(length):
        print(i, ' ', sep='', end='')
    print()