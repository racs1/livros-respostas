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

