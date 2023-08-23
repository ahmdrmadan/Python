hasilminusharuspakevariabel1 = float(input("Masukkan angka yang bernilai lebih dari 0 tetapi kurang dari 5 atau lebih dari 8 tetapi kurang dari 11:"))

hasil1 = 0 < hasilminusharuspakevariabel1 < 5 
print ("Hasil1 :",hasil1)

hasilminusharuspakevariabel2 = float(input("Masukkan angka yang bernilai lebih dari 0 tetapi kurang dari 5 atau lebih dari 8 tetapi kurang dari 11:"))
hasil2 = 8 < hasilminusharuspakevariabel2 < 11
print ("Hasil2 :",hasil2)

hasil3 = hasil1 or hasil2
print ("hasil3 :", hasil3)


print("\n", 10*"=","\n")

angka = int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10:"))

hasil = angka<0 or 5<angka<8 or 11<angka
print ("Hasil :",hasil)

#dari komentar

angka = int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10:"))

hasil = 0<angka<5 or 8<angka<11
print ("Hasil :",hasil)


angka = int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10:"))

hasil = angka<0 or 5<angka<8 or 11<angka
print ("Hasil :",hasil)