#merubah data ke tipe yang lain

data_int = 9

print("data:" , data_int, ", tipe data =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # 0 = false, selain 0 = true walaupun "-" minus

print("data:" , data_float, ", tipe data =", type(data_float))
print("data:" , data_str, ", tipe data =", type(data_str))
print("data:" , data_bool, ", tipe data =", type(data_bool))

#dan untuk mengubah data yang lain ya sama aja