import os
os.system("cls")
from datetime import datetime
from datetime import date
from translate import Translator
# /1-misol/
# hozir = datetime.now()
# print(f"Hozirgi sana va vaqt: {hozir}")
# print(f"Bugungi sana: {hozir.date()}")

# /2-misol/
# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))
# tugilgan_kun = date(yil, oy, kun)
# bugun = date.today()
# farq = bugun - tugilgan_kun
# print(f"{farq.days} kun o'tdi")

# /3-misol/
# bugun = date.today()
# yil = bugun.year
# bayram = date(yil, 9, 1)
# if bugun > bayram:
#     bayram = date(yil + 1, 9, 1)
# qoldi = bayram - bugun
# print(f"Keyingi Mustaqillik bayramiga {qoldi.days} kun qoldi.")

# /4-misol/
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# C = [
#     [0, 0],
#     [0, 0]
# ]
# for i in range(2):
#     for j in range(2):
#         C[i][j] = A[i][j] + B[i][j]
# print("C =", C)

# /5-misol/
# input_list = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]
# translator = Translator(from_lang="uz", to_lang="en")
# natija = {}
# for item in input_list:
#     if type(item) == str:
#         tarjima = translator.translate(item)
#         natija[item] = tarjima.lower()
# print(natija)

# /6-misol/
filmlar = {
    "Titanic": "Jack Dawson",
    "Harry Potter": "Harry Potter",
    "The Dark Knight": "Bruce Wayne (Batman)",
    "The Matrix": "Neo (Thomas Anderson)",
    "Forrest Gump": "Forrest Gump",
    "Gladiator": "Maximus Decimus Meridius",
    "Inception": "Dom Cobb",
    "Spider-Man": "Peter Parker",
    "Iron Man": "Tony Stark",
    "The Lord of the Rings": "Frodo Baggins"
}
kiritilgan_film = input("Film nomini kiriting: ")
try:
    print(filmlar[kiritilgan_film])
except KeyError:
    print("Bunday film yo'q")