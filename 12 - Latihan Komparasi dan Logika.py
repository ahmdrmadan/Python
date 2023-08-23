# Membuat gabungan area rentang dari angka

# +++++3--------10+++++

inputUser = float(input("Masukan angka yang kurang dari 3 atau lebih dari 10: "))

#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print ("Kurang dari 3=", isKurangDari)

#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print ("Lebih dari 10=", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print ("angka yang anda masukan: ", isCorrect)


# -----3+++++++++++10-----
print("\n", 10*"=","\n")
inputUser = float(input("Masukan angka yang lebih dari 3 dan kurang dari 10: "))

#memeriksa angka lebih dari 3
isKurangDari = (inputUser > 3)
print ("Kurang dari 3=", isKurangDari)

#memeriksa angka kurang dari 10
isLebihDari = (inputUser < 10)
print ("Lebih dari 10=", isLebihDari)

isCorrect = isKurangDari and isLebihDari
print ("angka yang anda masukan: ", isCorrect)