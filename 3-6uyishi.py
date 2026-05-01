import os
os.system("cls")

# < 1-MASALA > #
# def nollar(listim):
#     yangi = []
#     nollar = []
#     for son in listim:
#         if son != 0:
#             yangi.append(son)
#         else:
#             nollar.append(0)
#     return yangi + nollar
# a = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
# print(nollar(a))

# < 2-MASALA > #
# def dublikat(umumiy_list):
#     yangi_list = []
#     for ichki_list in umumiy_list:
#         if ichki_list not in yangi_list:
#             yangi_list.append(ichki_list)
#     return yangi_list
# input_data = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print(dublikat(input_data))

# < 3-MASALA > #
# def birlashtir(l1, l2):
#     natija = []
#     uzunlik = max(len(l1), len(l2))
    
#     for i in range(uzunlik):
#         if i < len(l1):
#             natija.append(l1[i])
#         if i < len(l2):
#             natija.append(l2[i])
#     return natija
# print(birlashtir([1, 2, 3], [11, 22, 33]))

# < 4-MASALA > #
# def birxil(list_a, list_b):
#     new = []
#     for son in list_a:
#         if son in list_b and son not in new:
#             new.append(son)
#     return new
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(birxil(a, b))

# < 5-MASALA > #
# def takrorlanganlar():
#     n = int(input("N = "))
#     sonlar = []
#     for i in range(n):
#         sonlar.append(int(input(f"{i+1}-son: ")))
    
#     saralangan = []
#     for son in sonlar:
#         if sonlar.count(son) > 1:
#             saralangan.append(son)
#     return saralangan
# print(takrorlanganlar())

# < 6-MASALA > #
# kvadrat_oshir = lambda royxat: [x**2 for x in royxat]
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# print(kvadrat_oshir(sonlar))

# < 7-MASALA > #
def belgi_sana(matn):
    lugat = {}
    for harf in matn:
        if harf in lugat:
            lugat[harf] += 1
        else:
            lugat[harf] = 1
    return lugat
print(belgi_sana('w3resource'))