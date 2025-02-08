print(' # Program Python Mencari Gaji Karyawan #')
print('-----------------------------------------')

# bikin input untuk nama, golongan, jam kerja
nama = input('Nama = ')
golongan = input('Golongan = ')
jam_kerja = int(input('jam kerja = '))

if golongan == 'A':
    upah_per_jam = 5000
elif golongan == 'B':
    upah_per_jam = 7000
elif golongan == 'C':
    upah_per_jam = 8000
elif golongan == 'D':
    upah_per_jam = 10000

if (jam_kerja > 48):
    uang_lembur = (jam_kerja-48)*4000
elif (jam_kerja < 48):
    uang_lembur = 0

gaji = (upah_per_jam*jam_kerja) + uang_lembur

print(f'gaji pegawai {gaji} per minggu')