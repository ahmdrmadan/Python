# 1. menyambung string

nama_depan = "Ahmad"
nama_tengah = "Rama"
nama_belakang = "dan"

nama_lengkap = nama_depan + " " + nama_tengah + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang

panjang = len(nama_lengkap)
print("Panjang dari", nama_lengkap + "=" + str(panjang))

# 3. Cek apakah ada kompoonen char atau string di dalam string

d = "d"
status = d in nama_lengkap
print (d + " ada di " + nama_lengkap + "=" +str(status))

d = "d"
status = d not in nama_lengkap
print (d + " tidak ada di " + nama_lengkap + "=" +str(status))

# 4. Mengulang string
print (10*"wk")
print ("wk"*20)

# 5. Indexing (untuk cek huruf keberapa [dimulai dari 0])
print ("index ke-0 : " + nama_lengkap[0])
print ("index ke-6 : " + nama_lengkap[6])
print ("index ke-[0:5] : " + nama_lengkap[0:5])
print ("index ke-[02,4,6,8,10] : " + nama_lengkap[0:10:2]) # cara bacanya 0 sampe 10 dengan increment 2

# kalo - ambil dari belaang
print ("index ke--1 : " + nama_lengkap[-1])

# item paling kecil
print("Item paling kecil adalah : " + min(nama_lengkap))

# item paling besar
print("Item paling besar adalah : " + max(nama_lengkap))

ascii_code = ord("a")
print("ASCI Code untuk huruf a adalah: " + str(ascii_code))

# 6. operasi dalam bentuk method

data = "RASA DEWA ALAM"
jumlah = data.count("A")
print("Jumlah A pada " + data + "=" + str(jumlah))