import os
os.system("cls")

# & 1-misol & #
# def sozlar(matn):
#     sozlar = matn.split()
#     hisob = {}
#     for s in sozlar:
#         if s in hisob:
#             hisob[s] += 1
#         else:
#             hisob[s] = 1
#     natija = sorted(hisob, key=hisob.get, reverse=True)
#     return natija[0], natija[1], natija[2]
# matn = "olma nok olma gilos olma nok shaftoli"
# print(sozlar(matn))

# & 2-misol & #
# def hisob(oquvchilar):
#     for ism in oquvchilar:
#         ballar = oquvchilar[ism]
#         jami = 0
#         soni = 0
#         for fan in ballar:
#             jami += ballar[fan]
#             soni += 1
#         ortacha = jami / soni
#         print(ism, ":", ortacha)
# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
# }
# hisob(students)

# & 3-misol & #
# def ombor_(mahsulotlar):
#     jami_miqdor = 0
#     for m in mahsulotlar:
#         jami_miqdor += m["miqdor"]
#     def saralash_(el):
#         return el["miqdor"]
#     mahsulotlar.sort(key=saralash_)
#     kam1 = mahsulotlar[0]["mahsulot"]
#     kam2 = mahsulotlar[1]["mahsulot"]
#     kam3 = mahsulotlar[2]["mahsulot"]
#     print("Umumiy miqdor:", jami_miqdor)
#     print("Eng kam qolganlar:", kam1, kam2, kam3)
# ombor = [
#     {"mahsulot": "olma", "miqdor": 5}, {"mahsulot": "nok", "miqdor": 9},
#     {"mahsulot": "shaftoli", "miqdor": 7}, {"mahsulot": "anor", "miqdor": 4},
#     {"mahsulot": "banan", "miqdor": 6}, {"mahsulot": "uzum", "miqdor": 8},
#     {"mahsulot": "gilos", "miqdor": 2}, {"mahsulot": "tarvuz", "miqdor": 1},
#     {"mahsulot": "qovun", "miqdor": 3}, {"mahsulot": "limon", "miqdor": 5}
# ]
# ombor_(ombor)

# & 4-misol & #
# def lugat(lugat):
#     tartib = sorted(lugat, key=lugat.get)
#     for k in tartib:
#         print(k)
# my_dict = {"t": 3, "p": 1, "y": 2, "o": 5, "h": 4, "n": 6}
# lugat(my_dict)

# & 5-misol & #
def tozalash(royxat):
    yangi = []
    for element in royxat:
        if element != "" and element not in yangi:
            yangi.append(element)
    return yangi
mylist = ["olma", "", "olma", "gilos", ""]
print(tozalash(mylist))