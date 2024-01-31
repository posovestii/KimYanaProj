# Туристические агентства предлагают следующие туры. Вояж - Мексика,Канада,Израиль, Италия, США. РейнаТур - Англия, Япония,Канада, ЮАР. Радуга - США,Испания, Швеция, Австралия, Италия, Канада.
# Определить:
#
#  №1 каких турагенствах можно одновременно приобрести туры в Италию и Канаду.


Voyaj = { "Мексика", "Канада", "Израиль", "Италия", "США"}
Reynatur = { "Англия", "Япония", "Канада", "ЮАР" }
Raduga = {"США", "Испания", "Швеция", "Австралия", "Италия", "Канада"}

print("1. Можно одновременно приобрести туры в Италию и Канаду в турагенствах: ")
if "Италия" in Voyaj and "Канада" in Voyaj:
    print("Вояж")
if "Италия" in Reynatur and "Канада" in Reynatur:
        print("РейнаТур")
if "Италия" in Raduga and "Канада" in Raduga:
    print("Радуга")


# №2 в турагенство РейнаТур добавить тур в Индию.

Reynatur.add("Индия")
print("2. Обновленный список РейнаТур:", Reynatur)

# №3 полный список всех туров

all_tours = Voyaj.union(Reynatur, Raduga)
print("3. Полный список всех туров: ", all_tours)