import os
os.system("cls")
#                    1-MISOL:
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# sonlar = []
# for i in range(a, b):
#     if i % 2 == 0:
#         sonlar.append(i)
# print("sonlar=", sonlar)

#                    2-MISOL:
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# print(tuple1[3]) 
# print(tuple1[-4])

#                    3-MISOL:
# son1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# yangi_list = []
# for t in son1:
#     yangi_tuple = (t[0], t[1], 100)
#     yangi_list.append(yangi_tuple)
# print(yangi_list)

#                    4-MISOL:
# matn = "python 3.0"
# natija = tuple(matn)
# print(natija)

#                    5-MISOL:
# data = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# eng_katta = max(data, key=sum)
# print(eng_katta)

#                    6-MISOL:
tuple24 = [1, 2, 3, 4]
string = "emp"
yangi_list = []

for i in tuple24:
    yangi_list.append(string + str(i))

print(yangi_list)