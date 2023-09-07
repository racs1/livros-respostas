#cubos = [value**3 for value in range(1,11)]
#print(cubos)
cubos = []
lista = list(range(1,11))
for number in lista:
    cubos.append(number**3)
print(cubos)
