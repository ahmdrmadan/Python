# Operasi logika atau Boolean

# not, or, and, xor

#not
a = True
c = not a
print ('data a =',a)
print ('====NOT====')
print ('data c =',c)

# and (jika salah satu false maka hasilnya false)
a = True
b = True
c = a and b
print ('====AND====')
print (a, 'and', b ,'=' ,c)

a = False
b = True
c = a and b
print (a, 'and', b ,'=' ,c)

a = True
b = False
c = a and b
print (a, 'and', b ,'=' ,c)

a = False
b = False
c = a and b
print (a, 'and', b ,'=' ,c)

# or (jika salah satu true maka hasilnya true)
a = True
b = True
c = a or b
print ('====OR====')
print (a, 'OR', b ,'=' ,c)

a = False
b = True
c = a or b
print (a, 'OR', b ,'=' ,c)

a = True
b = False
c = a or b
print (a, 'OR', b ,'=' ,c)

a = False
b = False
c = a or b
print (a, 'OR', b ,'=' ,c)

# XOR (hasilnya true jika salah satu true)
a = True
b = True
c = a ^ b
print ('====XOR====')
print (a, 'XOR', b ,'=' ,c)

a = False
b = True
c = a ^ b
print (a, 'XOR', b ,'=' ,c)

a = True
b = False
c = a ^ b
print (a, 'XOR', b ,'=' ,c)

a = False
b = False
c = a ^ b
print (a, 'XOR', b ,'=' ,c)