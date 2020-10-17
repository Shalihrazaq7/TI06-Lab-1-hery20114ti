# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
h = eval (input("Angka pertama: "))
i = eval (input("Angka kedua: "))
j = eval (input("Angka ketiga: "))
k = ((h+i+j)/3)
print('Hasil rata-ratanya adalah ',k,end='\n')



# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
a = eval (input('Masukkan angka: '))
b = int (input('Jumlah angka kelipatan: '))
h = a
for i in range (1,b+1):
 print(h, end=' ')
 h = (a+h)
print(end='\n')