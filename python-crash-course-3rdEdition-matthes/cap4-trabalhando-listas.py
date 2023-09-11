# %%
#4.1 - Pizzas

pizzas = ['calabresa', 'quatro queijos', 'pepperoni','margherita', 'frango']
for pizza in pizzas:
    print(pizza)
    print(f"Gosto de pizza de {pizza.title()}")
print("Eu amo pizza!")

# %%
#4.2 - Animals

animais = ['gato', 'cachorro', 'cavalo', 'porco', 'vaca']
for mamifero in animais:
    print(mamifero)
    print(f"Um(a) {mamifero.title()} seria um ótimo animal de estimação (pet)")
print("Todos os animais listados são mamíferos!")

# %%
#4.3 - One to twenty

for number in range(1,21):
    print(number)

# %%
#4.4 - One Milion

lista = list(range(1,1000001))
for number in lista:
    print(number)

# %%
#4.5 - One Milion 2

lista = list(range(1,1000001))
print(min(lista))
print(max(lista))
print(sum(lista))

# %%
#4.6 - Odd numbers

impares = list(range(1,21,2))
for number in impares:
    print(number)

# %%
#4.7 - Three

multiplos_3 = list(range(3,31,3))
for number in multiplos_3:
    print(number)

# %%
#4.8 - Cubes

#cubos = [value**3 for value in range(1,11)]
#print(cubos)
cubos = []
lista = list(range(1,11))
for number in lista:
    cubos.append(number**3)
print(cubos)

# %%
#4.9 - Cube Comprehension

cubos = [value**3 for value in range(1,11)]
print(cubos)

# %%
#4.10 - Slices

cubos = [value**3 for value in range(1,12)]
print(cubos)
print(f"Os três primeiros elementos da lista são: {cubos[:3]}")
print(f"Os três elementos que ficam no meio da lista são: {cubos[4:7]}")
print(f"Os três últimos elementos da lista são: {cubos[-3:]}")

# %%
#4.11 - My pizzas your pizzas

pizzas = ['calabresa', 'quatro queijos', 'pepperoni','margherita', 'frango']
friend_pizzas = pizzas[:]
pizzas.append('portuguesa')
friend_pizzas.append('atum')
print('Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)
print('Minhas pizzas favoritas são:')
for pizza in friend_pizzas:
    print(pizza)

# %%
#4.12 - Food

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
for food in my_foods:
    print(food)
print("\n")
for food in friend_foods:
    print(food)

# %%
#4.13 - Buffet

refeicoes = ("lasanha", "pizza", "estrogonofe", "hamburguer", "macarronada")
for refeicao in refeicoes:
    print(refeicao)

#refeicoes[0] = "salada"
refeicoes = ("pipoca", "salada", "estrogonofe", "hamburguer", "macarronada")
print("\n")
for refeicao in refeicoes:
    print(refeicao)