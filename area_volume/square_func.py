print(' luas persegi')
print('--------------')

def luas_persegi(sisi):
    return round(sisi*sisi,2)

sisi = float(input('Input= '))
print('Luas persegi = ', luas_persegi(sisi))