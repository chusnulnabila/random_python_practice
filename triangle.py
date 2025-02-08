# melatih nested lopp

# outer loop untuk tinggi segitiga
# inner loop untuk membentuk segitiga

print('  ## Triangle Python Program ##  ')
print('=================================')

length = int(input('length of tringle: '))

# for i in range(length):
#     for j in range(i+1):
#         print(' *', end='')
#     print()


# cara lain untuk for loop nya, bisa menggunakan 1 for loop aja
for i in range(length+1):
    print(' *' * i)