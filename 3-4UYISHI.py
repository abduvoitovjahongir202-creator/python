import os
os.system("cls")

# =-=-=-=-=-=-=-1-misol:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
umumiy = set1.intersection(set2)
vazifa = set1.difference(set2)
natija = sum(umumiy) - sum(vazifa)
print(natija)

# =-=-=-=-=-=-=-2-misol:
set1 = {'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2 = {'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3 = {'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}
apple = set1.intersection(set2)
natija = apple.difference(set3)
print(natija)

# =-=-=-=-=-=-=-3-misol:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
element = set1.symmetric_difference(set2)
print(sorted(list(element), reverse=True))

# =-=-=-=-=-=-=-4-misol:
shaxzod = {"Toshkent", "Samarqand", "Sirdaryo", "Andijon"}
jaxongir = {"Toshkent", "Farg'ona", "Sirdaryo", "Samarqand"}
birgalikda = shaxzod.intersection(jaxongir)
shaxzodbek = shaxzod.difference(jaxongir)
print("Ikkalamiz borgan joyimiz:", birgalikda)
print("Faqat Shaxzod borgan joylar:", shaxzodbek)

# =-=-=-=-=-=-=-5-misol:
soz1 = input("1 ni kiriting: ").lower()
soz2 = input("2 ni kiriting: ").lower()
if len(soz1) == len(soz2) and sorted(soz1) == sorted(soz2):
    print("True")
else:
    print("False")
    
# =-=-=-=-=-=-=-5-misol:   
set1 = {4, 5, 6, 7, 8, 9}
set2 = {5, 6, 7, 10, 11}
simmetrik = set1.symmetric_difference(set2)
umumiy = set1.intersection(set2)
natija = sum(simmetrik) - sum(umumiy)
print(natija)    