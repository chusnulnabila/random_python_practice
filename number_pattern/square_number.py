print('  Python Program to make Square Number Series  ')
print('================================================')

number = int(input('Enter Input: '))
print()

current_number = 1
for i in range(1, number+1):
    for j in range(1, number+1):
        print(current_number, '', end='')
        current_number += 1
    print()