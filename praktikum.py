#python 3.7.1

absen=int(input("masukkan nilai absen,"))
uts=int(input("masukkan nilai uts,"))
uas=int(input("masukkan nilai uas,"))

standar=55
jumlah= absen + uts + uas
rata_rata = jumlah /3

print("jumlah nilai yang didapatkan adalah=", jumlah)
print("nilai rata_rata yang didapatkan adalah=", rata_rata) 

nilai= int(input("masukkan nilai siswa,"))

nilai =0
if nilai >=85:
  print('predikat A/memuaskan')
elif nilai >=75:
  print('predikat B/bagus') 
elif nilai >=65:
  print('predikat C/cukup')
elif nilai >=55:
  print('predikat D/kurang')
else:
  print('predikat')') 