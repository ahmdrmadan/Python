a = 5 #ini adalah operator assignment
print("nilai a =", a)

a += 1 # artinya adalah a = a ditambah (+) 1
print("nilai a += 1, nilai a menjadi", a)

a -= 2 # artinya adalah a = a dikurang (-) 2
print("nilai a -= 1, nilai a menjadi", a)

a *= 5 # artinya adalah a = a dikali (*) 5
print("nilai a *= 1, nilai a menjadi", a)

a /= 2 # artinya adalah a = a dibagi (/) 2
print("nilai a /= 1, nilai a menjadi", a)

print("\n", 10*"=","\n")

b = 10
b %= 3 # artinya adalah b = b modulus (%) 3
print("nilai b %= 3, nilai b menjadi", b)

b = 10
b //= 3 # artinya adalah b = b floor division (//) 3
print("nilai b //= 3, nilai b menjadi", b)

a = 5
a **= 3 # artinya 5 di pangkatkan dengan 3
print("nilai a **= 3, nilai a menjadi", a)

print("\n", 10*"=","\n")
# operasi bitwise
# OR
c = True
print("nilai c =", c)
c |= False # c true or c false
print("nilai c |= False, nilai c menjadi", c)

c = False
print("nilai c =", c)
c |= False # c true or c false
print("nilai c |= False, nilai c menjadi", c)

# AND
c = True
print("nilai c =", c)
c &= False # c true AND c false
print("nilai c &= False, nilai c menjadi", c)

c = True
print("nilai c =", c)
c &= True # c true or c True
print("nilai c &= True, nilai c menjadi", c)

# XOR
c = True
print("nilai c =", c)
c ^= False # c true XOR c false
print("nilai c ^= False, nilai c menjadi", c)

c = True
print("nilai c =", c)
c ^= True # c true or c True
print("nilai c ^= True, nilai c menjadi", c)

#GESER GESER
d = 0b0100
print("nilai d =", format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d,'04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi", format(d,'04b'))