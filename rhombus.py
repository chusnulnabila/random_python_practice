# belah ketupat
# the output will look like this:
# ==========================
# length for rhombus: 3
#    *
#   * *
#  * * *
#   * *
#    *
# ==========================

print('  ##  Rhombus Python Program  ##  ')
print('==================================')


length = int(input('length for rhombus: '))
print()

for i in range(length):
    for j in range(length-i):
        print(' ', end='')
    
    for k in range(i+1):
        print('* ', end='')
    print()

for l in range(1, length):
    for m in range(l+1):
        print(' ', end='')

    for n in range(length-l):
        print('* ', end='')
    print()


# cara lain dengan menggunakan 2 buah for loop
# for i in range(length):
#     print(' ' * (length-i), end='')
#     print('* ' * (i+1))

# for j in range(1, length):
#     print(' ' * (j+1), end='')
#     print('* ' * (length-j))