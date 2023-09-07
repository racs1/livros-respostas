# %%
# 5.3 - Cor dos Aliens 1
alien_color = 'green'
if alien_color == 'green':
    print("+5 pontos!")

if alien_color == 'red':
    print("-5 pontos!")

# %%
# 5.4 - Cor dos Aliens 2
alien_color = 'green'
if alien_color == 'green':
    print("+5 pontos for kill alien")
else:
    print("+10 pontos")
# %%
# 5.5 - Cor dos Aliens 3
alien_color = 'red'
if alien_color == 'green':
    print("+5 pontos for kill alien")
else:
    print("+10 pontos") 

alien_color = 'green'
if alien_color == 'green':
    print("+5 pontos")
elif alien_color == 'yellow':
    print('+10 pontos')
elif alien_color == 'red':
    print("+15 pontos")
else:
    print("0 pontos")

alien_color = 'yellow'
if alien_color == 'green':
    print("+5 pontos")
elif alien_color == 'yellow':
    print('+10 pontos')
elif alien_color == 'red':
    print("+15 pontos")
else:
    print("0 pontos")
# %%
alien_color = 'red'
if alien_color == 'green':
    print("+5 pontos")
elif alien_color == 'yellow':
    print('+10 pontos')
elif alien_color == 'red':
    print("+15 pontos")
else:
    print("0 pontos")

# %%
# 5.6 - Idades
age = 70
if age < 2:
    print("neném")
elif age < 4:
    print("criança")
elif age < 13:
    print("garoto")
elif age < 20:
    print("adolescente")
elif age < 65:
    print("adulto")
else:
    print("idoso")

# %%
# 5.7 - Frutas Favoritas
favorite_fruits = ['pitanga', 'acerola', 'lichia', 'kiwi', 'caqui']
fruit1 = 'manga'
if fruit1 in favorite_fruits:
    print(f"Você realmente gosta de {fruit1}")
else:
    print(f"Você não gosta de {fruit1}")

# %%
# 5.8 - Olá Admin
names = ['cliver', 'luiz', 'julio', 'german', 'fabio', 'admin']

for name in names:
    if name == 'admin':
        print(f"Olá {name.title()}, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {name.title()}, obrigado por fazer login novamente")

# %%
# 5.9 - Olá Admin 2
names = ['cliver', 'luiz', 'julio', 'german', 'fabio', 'admin']

if names:
    for name in names:
        if name == 'admin':
            print(f"Olá {name.title()}, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {name.title()}, obrigado por fazer login novamente")
else:
    print("Necessário encontrar usuários!")

names = []

if names:
    for name in names:
        if name == 'admin':
            print(f"Olá {name.title()}, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {name.title()}, obrigado por fazer login novamente")
else:
    print("Necessário encontrar usuários!")

# %%
# 5.10 - Nome de usuários
current_users = ['Igor', 'selma', 'CAROL', 'ademar', 'rodrigo']
new_users = ['cliver', 'luiz', 'Carol', 'igor', 'joão']
current_users_lower = []

for name in current_users:
    current_users_lower.append(name.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} já existe. Digite um nome diferente")
    else:
        print(f"{user} disponível")

# %%
# 5.11 - Números ordinais
numbers = list(range(1,10))

if numbers:
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")
