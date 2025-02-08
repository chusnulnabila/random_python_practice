# piramida bintang disebut juga sebagai segitiga bintang sama sisi
# if input = 6
# output :
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * *

print('  ## Star Pyramid ## ')
print('=======================')

length = int(input('length for pyramid: '))
print()

for i in range(length):
    for j in range(length-i):
        print(' ', end='')
    
    for k in range(i+1):
        print('* ', end='')
    print()


# dengan menggunakan satu for loop
# biasanya ini cuma bisa dilakuiin di python
# for i in range(length):
#     print(' ' * (length-i), end='')
#     print('* ' * (i+1))