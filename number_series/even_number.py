print('Python Even Number Program')

start_num = int(input('Input initial number: '))
final_num = int(input('Input final number: '))

for i in range(start_num, final_num+1):
    if(i%2 == 0):
        print(i, end=' ')

# --- OUTPUT ---
# Python Even Number Program
# Input initial number: 4
# Input final number: 50
# 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 