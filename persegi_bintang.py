# melatih nested loop

# outer loop untuk membuat tinggi persegi
# inner loop untuk membuat lebar persegi

print('  # Star Square Python Program #  ')
print('==================================')

square = int(input('Large Square Input: '))
print()

for i in range(square):
    for j in range(square):
        print(' *', end='')
    print()


# new things to learn from the code:
# 1. penggunaan end='' untuk mengganti newline yang secara default ada di print() dengan output yang tetap berada di baris yang sama