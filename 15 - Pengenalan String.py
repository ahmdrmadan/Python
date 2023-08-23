data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan singel quote ''
    2. dengan menggunakan double quote ""
'''

data = 'Menggunakan singel quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo apa kabar!"')
print("'Hallo apa kabar!'")
print("Hari Jum'at")

# 2. Menggunakan tanda \ membuat tanda spesial (',",\,* dll) jadi terbaca
print('Hari Jum\'at')
print('C:\\user\\Ucup')

# Tab
print('Heka\t\t\tYuri, fungsinya untuk tab')

# Backspace
print('Adan \bYuri, fungsinya untuk backspace')

# New line
print('Adan \nYuri')

# Menggunakan Raw String
print(r'C:\user\Ucup') # Fungsi r yaitu membuat semua yang ada didalam tanda kutip menjadi string

# Multipel literal string (akan print semua sesuai apa yang kita ketik)
print("""
adan
yuri
""")

# Multipel literal string kombo sama Raw string
print(r"""
adan/adan
yuri/yuri
""")