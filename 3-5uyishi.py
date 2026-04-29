import os
os.system("cls")

#:"1-masala":#
# cars = {
#   "Malibu": 35000, 
#         "Spark": 12000, 
#         "Cobalt": 18000, 
#         "Tracker": 28000
# }
# nomlar = list(cars.keys())
# narxlar = list(cars.values())
# eng_qimmat_narx = narxlar[0]
# eng_qimmat_nom = nomlar[0]
# eng_arzon_narx = narxlar[0]
# eng_arzon_nom = nomlar[0]
# jami_narx = 0
# for nom, narx in cars.items():
#     if narx > eng_qimmat_narx:
#         eng_qimmat_narx = narx
#         eng_qimmat_nom = nom
#     if narx < eng_arzon_narx:
#         eng_arzon_narx = narx
#         eng_arzon_nom = nom
#     jami_narx += narx
# print("Eng qimmat: ", eng_qimmat_nom)
# print("Eng arzon: ", eng_arzon_nom)
# print("Ortacha: ", jami_narx / len(cars))

#:"2-masala":#
# movies = {
#     "Titanic": 1997, 
#     "Avatar": 2009,     
#     "Inception": 2010,  
#     "Interstellar": 2014
# }

# for kino, yil in movies.items():
#     if yil > 2000:
#         print(kino)

#:"3-masala":#
# speed = {
#     "Tesla": 200, 
#     "BMW": 320, 
#     "Mercedes": 290, 
#     "Audi": 310
# }
# data = list(speed.items())
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i][1] < data[j][1]:
#             data[i], data[j] = data[j], data[i]

# for k, v in data:
#     print(k, v)

#:"4-masala":#
# professions = {
#     "Bill Gates": "Dasturchi", 
#     "Cristiano Ronaldo": "Futbolchi", 
#     "Elon Musk": "Tadbirkor", 
#     "Messi": "Futbolchi"
# }
# ism = input("Ismni kiriting: ")
# kasb = professions.get(ism)
# if kasb:
#     print(kasb)
# else:
#     print("Bunday shaxs topilmadi.")

#:"5-masala":#
# car_count = {
#     "Chevrolet": 120, 
#     "Toyota": 95, 
#     "BMW": 60, 
#     "Kia": 75
# }
# nomlar = list(car_count.keys())
# sonlar = list(car_count.values())
# eng_kop_son = sonlar[0]
# eng_kop_nom = nomlar[0]
# eng_kam_son = sonlar[0]
# eng_kam_nom = nomlar[0]
# for nom, son in car_count.items():
#     if son > eng_kop_son:
#         eng_kop_son = son
#         eng_kop_nom = nom
#     if son < eng_kam_son:
#         eng_kam_son = son
#         eng_kam_nom = nom
# print("Eng ko'p sotilgan:", eng_kop_nom)
# print("Eng kam sotilgan:", eng_kam_nom)

#:"6-masala":#
books = {
    "O'tkan kunlar": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1926,
        "tarjimalar soni": 5
    },
    "Mehrobdan chayon": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1929,
        "tarjimalar soni": 3
    },
    "Kecha va kunduz": {
        "muallifi": "Cho'lpon",
        "janri": "Roman",
        "chop etilgan yili": 1934,
        "tarjimalar soni": 4
    },
    "Sarob": {
        "muallifi": "Abdulla Qahhor",
        "janri": "Roman",
        "chop etilgan yili": 1935,
        "tarjimalar soni": 2
    },
    "Ulug'bek xazinasi": {
        "muallifi": "Odil Yoqubov",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1974,
        "tarjimalar soni": 6
    },
    "Don Kixot": {
        "muallifi": "Migel de Servantes",
        "janri": "Roman",
        "chop etilgan yili": 1605,
        "tarjimalar soni": 50
    },
    "Urush va tinchlik": {
        "muallifi": "Lev Tolstoy",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1869,
        "tarjimalar soni": 45
    },
    "Alkimyogar": {
        "muallifi": "Paulo Koelyo",
        "janri": "Falsafiy roman",
        "chop etilgan yili": 1988,
        "tarjimalar soni": 80
    },
    "1984": {
        "muallifi": "Jorj Oruell",
        "janri": "Antiutopik roman",
        "chop etilgan yili": 1949,
        "tarjimalar soni": 65
    },
    "Kichkina shahzoda": {
        "muallifi": "Antuan de Sent-Ekzyuperi",
        "janri": "Falsafiy ertak",
        "chop etilgan yili": 1943,
        "tarjimalar soni": 300
    }
}
user_input = input("Kitob nomini kiriting: ").lower()
topildi = False
for nom, info in books.items():
    if nom.lower() == user_input:
        print(info)
        topildi = True
        break
if not topildi:
    print("Kitob topilmadi")