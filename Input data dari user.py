# data yang dimasukan pasti string
data = input("masukan data:")

print("data:", data,", type", type(data))

# jika ingin mengambil data int
angka1 = float(input("masukan angka:"))
angka2 = int(input("masukan angka:"))

print("data_int:", angka1,", type", type(angka1))
print("data_int:", angka2,", type", type(angka2))

# boolean harus menggunakan int
bool = bool(int(input("masukan angka:")))

print("data:", bool,", type", type(bool))