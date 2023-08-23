# tipe data: Angka Satuan (Integer) tidak ada "," koma 

data_integer = 1
print(type(data_integer)) # buat print tipe data
print("data:" , data_integer)

# tipe data float ada "," koma
data_float = 1.4
print(type(data_float)) # buat print tipe data
print("data:" , data_float)

# tipe data string
data_string = "Adan"
print(type(data_string)) # buat print tipe data
print("data:" , data_string)

# tipe data boolean (biner (true/fals))
data_bool = True
print(type(data_bool)) # buat print tipe data
print("data:" , data_bool)

# Bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex)) # buat print tipe data
print("data:" , data_complex)

# import dari bahasa C

from ctypes import c_double 

data_c_double = c_double(10.4)
print(type(data_c_double)) # buat print tipe data
print("data:" , data_c_double)