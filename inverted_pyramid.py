# inverted pyramid

print('  ##  inverted pyramid  ##  ')
print('============================')

length = int(input('length for inverted pyramid: '))
print()

for i in range(length):
    for j in range(i+1):
        print(' ', end='')
    
    for k in range(length-i):
        print('* ', end='')
    print()

# menggunakan satu for loop
# for i in range(length):
#     print(' ' * (i+1), end='')
#     print('* ' * (length-i))