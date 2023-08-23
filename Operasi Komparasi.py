#setiap hasil dari operasi komparasi adalah bolean

# >,<,>=,<=,==,!=,is, is not

a = 4
b = 2

# lebih besar >
print("LEBIH BESAR >")
hasil = a > b
print(a, '>', b, '=' ,hasil)

hasil = b > a
print(b, '>', a, '=' ,hasil)

# kurang dari <
print("KURANG DARI <")
hasil = a < b
print(a, '<', b, '=' ,hasil)

hasil = b < a
print(b, '<', a, '=' ,hasil)

# lebih besar sama dengan >=
print("LEBIH BESAR SAMA DENGAN >= ")
hasil = a >= b
print(a, '>=', b, '=' ,hasil)

hasil = b >= a
print(b, '>=', a, '=' ,hasil)

# kurang dari SAMADENGAN <=
print("KURANG DARI SAMADENGAN <=")
hasil = a <= b
print(a, '<=', b, '=' ,hasil)

hasil = b <= a
print(b, '<=', a, '=' ,hasil)

# SAMA DENGAN =
print("SAMA DENGAN =")
hasil = a == b
print(a, '==', b, '=' ,hasil)

hasil = b == a
print(b, '==', a, '=' ,hasil)

# SAMA DENGAN =
print("TIDAK SAMA DENGAN !=")
hasil = a != b
print(a, '!=', b, '=' ,hasil)

hasil = b != a
print(b, '!=', a, '=' ,hasil)

# "is" sebagai komparasi(perbandingan) object identity 'is' harus menggunakan variabel (x/y/z)
print("OBJECT IDENTITY IS")
x = 5
y = 5
print('nilai x =', x,',id = ', hex(id(x)))
print('nilai y =', y,',id = ', hex(id(y)))

hasil = x is y
print('x is y =', hasil)

x = 5
y = 4
print('nilai x =', x,',id = ', hex(id(x)))
print('nilai y =', y,',id = ', hex(id(y)))

hasil = x is y
print('x is y =', hasil)

print("OBJECT IDENTITY IS NOT")
x = 5
y = 5
print('nilai x =', x,',id = ', hex(id(x)))
print('nilai y =', y,',id = ', hex(id(y)))

hasil = x is not y
print('x is not y =', hasil)

x = 5
y = 4
print('nilai x =', x,',id = ', hex(id(x)))
print('nilai y =', y,',id = ', hex(id(y)))

hasil = x is not y
print('x is y =', hasil)