import os
import random
import json
os.system("cls")

################################################################
# 1-misol:
# fayl1 = open("input1.txt", "r")
# kodlar = fayl1.read().split()
# gap = ""
# for kod in kodlar:
#     belgi = chr(int(kod))
#     gap = gap + belgi

# fayl2 = open("output1.txt", "w")
# fayl2.write(gap)

################################################################
# 2-misol:
# soz = input("So'z kiriting: ")

# fayl = open("matn.txt", "r")
# matn = fayl.read()

# if soz.lower() in matn.lower():
#     print("Siz kiritgan so'z faylda bor.")
# else:
#     print("Siz kiritgan so'z faylda yo'q.")

################################################################
# 3-misol:
# fayl = open("gaplar.txt", "r")
# matn = fayl.read()

# yangi_matn = matn.title()

# fayl2 = open("natija.txt", "w")
# fayl2.write(yangi_matn)

################################################################
# 4-misol:
fayl = open("sonlar.txt", "r")
sonlar_matni = fayl.read().split()

yigindi = 0
soni = 0

for s in sonlar_matni:
    yigindi = yigindi + int(s)
    soni = soni + 1

ortachasi = yigindi / soni
print(round(ortachasi))