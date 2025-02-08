print(' # persegi panjang #')
print()

rectangle_length = int(input('panjang:'))
rectangle_width = int(input('lebar:'))

for i in range(rectangle_length):
    for j in range(rectangle_width):
        print(' *', end='')
    print()


# cara kedua dengan loop yang berbeda
# for i in range(rectangle_length):
#     print(' *' * rectangle_width)