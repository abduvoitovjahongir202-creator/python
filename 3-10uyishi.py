import os
import random
import json
import requests as rq
os.system("cls")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 1-misol:
# users = [
#     'Abdulla Abdullaev', 
#     'Samandar Asadov', 
#     'Shaxnoza Jurayeva', 
#     'Ikrom Karimov',
#     'Gulnora Xalilova',
#     'Ziyoda Yuldashova'
#     ] 
# men = []
# women = []

# for user in users:
#     if user.endswith('ov') or user.endswith('ev'):
#         men.append(user)
#     elif user.endswith('va'):
#         women.append(user)

# print(f"men = {men}")
# print(f"women = {women}")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 2-misol:
# products = {
#     "olma": [13000, 14000, 15000],
#     "anor": [19000, 22000, 24000, 15000],
#     "gilos": [6000, 9000, 5000, 4000],
#     "banan": [30000, 28000]
# }

# def ortacha_narx(data):
#     for product, prices in data.items():
#         average = sum(prices) // len(prices)
#         print(f"{product}: {average}")

# ortacha_narx(products)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 3-misol:
# books = [
#     ("O'tkan kunlar", "Roman"),
#     ("Mehrobdan chayon", "Roman"),
#     ("Shum bola", "Povest"),
#     ("Alkimyogar", "Roman"),
#     ("Boy va kambag'al", "Hikoya"),
#     ("Urush va tinchlik", "Roman"),
#     ("Kecha va kunduz", "Roman"),
#     ("Yulduzli tunlar", "Povest"),
#     ("Qorako'z Majnun", "Hikoya"),
#     ("Qalb ko'zi", "Hikoya")
# ]

# grouped_books = {}

# for name, genre in books:
#     if genre not in grouped_books:
#         grouped_books[genre] = []
#     grouped_books[genre].append(name)

# import json
# print(json.dumps(grouped_books, indent=4, ensure_ascii=False))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 4-misol:
def bank_kalkulyatori(depozit, foiz, yil):
    foyda = (depozit * foiz * yil) // 100
    yakuniy_summa = depozit + foyda
    return yakuniy_summa

natija = bank_kalkulyatori(depozit=10000, foiz=24, yil=3)
print(f"Yakuniy summa: {natija}")