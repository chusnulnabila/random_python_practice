print('Python Odd Number Program')

start_num = int(input('Input initial number: '))
final_num = int(input('Input final number: '))

for i in range(start_num, final_num+1):
    if(i%2 == 1):
        print(i, end=' ')

# ---OUTPUT---
# Python Odd Number Program
# Input initial number: 9
# Input final number: 40
# 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39