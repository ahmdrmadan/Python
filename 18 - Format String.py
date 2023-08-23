# contoh generic
# string

nama = "adan"
format = f"helo {nama}"
print (format)

#boolean
boolean = True
format_str = f"boolean {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka {angka}"
print(format_str)

## Bilangan bulat
angka = 15
format_str = f"bulat {angka:d}"
print(format_str)

## Bilangan ribuan
angka = 2000
format_str = f"ribuan {angka:,}"
print(format_str)

# bilangan desimal :.2f untuk ambil 2 angka dibelakang titik .
angka = 2005.546543
format_str = f"desimal {angka:.2f}"
print(format_str)

# menampilkan tanda + -

angka_minus = -10
angka_plus = +10.4214
format_minus = f"minus {angka_minus:+d}"
format_plus = f"plus {angka_plus:+.2f}"

print (format_minus)
print (format_plus)

# memformat %

persentase = 0.045
format_persen = f"persentase adalah {persentase:.2%}"

print(format_persen)

# melakukan operasiaritmatika (perhitungan mtk)

harga = 5000
jumlah = 4

total = f"total = {harga*jumlah}"
print(total)

# format angka lain (biner, oktal, hexsa)

angka = 1981

format_binary = f"binary = {bin(angka)}"
format_oktal = f"oktal = {oct(angka)}"
format_hexa = f"hexa = {hex(angka)}"

print (format_binary)
print (format_oktal)
print (format_hexa)