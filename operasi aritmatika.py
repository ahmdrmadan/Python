# operasi aritmatika

#pertambahan
a = 10
b = 3

hasil = a + b
print(a, '+', b, '=', hasil)

#pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

#perkalian
hasil = a * b
print(a, '*', b, '=', hasil)

#pembagian
hasil = a / b
print(a, '/', b, '=', hasil)

#pangkat **
hasil = a ** b
print(a, '**', b, '=', hasil)

#modulus (sisa pembagian) %
hasil = a % b
print(a, '%', b, '=', hasil)

#floor division (pembulatan hasil pembagian) //
hasil = a // b
print(a, '//', b, '=', hasil)

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

#urutan pengerjaan 1. (), 2. exponen, 3. perkalian, 4. pertambahan

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)

#cara penulisan kurung
hasil = (x + y) * z
print('(',x,'+',y,') *',z, '=', hasil)