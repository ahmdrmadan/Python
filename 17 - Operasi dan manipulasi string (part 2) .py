# 1. menyambung string

# Merupah ke upper case

salam = "Halo Adan!"
print ("normal =" , salam)

salam = salam.upper()
print ("Upper nya =" , salam)

#Merubah ke lower
salam = "Halo Adan!"
print ("normal =" , salam)
salam = salam.lower()
print ("Upper nya =" , salam)

#cek apakah lower / upper
salam = "HALO ADAN!"
apakah_lower = salam.islower() #hasilnya boolean jadi harus di convert ke string dulu
print ("Apakah lower ?" , str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya boolean jadi harus di convert ke string dulu
print ("Apakah Upper ?" , str(apakah_upper))

# is.title untuk cek huruf awal kapital

salam = "Apakah Ini Benar?"
cek_title = salam.istitle() #hasilnya boolean jadi harus di convert ke string dulu
print ("Cek Title =" , str(cek_title))

# Cek komponen awal / akhir

kata = "Halo Adan!".startswith("Halo")
print ("Apakah Kata diatas di Awali dengan Halo?", str(kata))

kata = "Halo Adan!".endswith("Adan!")
print ("Apakah Kata diatas di Akhiri dengan Adan?", str(kata))

# penggabungan menggunakan join() dan split()
pisah =  ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print (pisah)
print (gabungan)

gabungan = ' hehe '.join(pisah)
print (gabungan)

gabungan = "akuhehesayanghehekamu"
print(gabungan.split('hehe'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print(kanan)

kiri = "kiri".ljust(10)
print(kiri)

tengah = "tengah".center(20, ":")
print(tengah)

# strip() kebalikan dari yang diatas
tengah = tengah.strip(":") # Menghilangkan tanda :
print(tengah)

kanan = kanan.strip() # Menghilangkan tanda spasi
print(kanan)

