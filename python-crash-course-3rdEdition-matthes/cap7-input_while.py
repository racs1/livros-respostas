# %%
# 7.1 - Aluguel de carro
marca = input("Qual marca de carro você gostaria de alugar?")
if marca.isalpha():
    print(f"Vejamos se consigo encontrar um {marca.title()} para você")
else:
    print("Digite uma informação válida!")
# %%
# 7.2 - Reservas em um restaurante
assentos = input("Você precisa de uma mesa de quantos lugares?")
if int(assentos) > 8:
    print("Aguarde uma mesa ficar disponível!")
else:
    print("Mesa disponível!")
# %%
# 7.3 - Múltiplos de dez
num = input("Digite um número:")
if int(num)%10 == 0:
    print("Múltiplo de dez")
else:
    print("Não múltiplo de dez")
# %%
# 7.4 - Ingredientes de pizza
pedido = ''
ingredientes = []
while pedido.lower() != 'quit':
    pedido = input("Digite o ingrediente da sua pizza:")
    if pedido.lower() == 'quit':
        break
    else:
        print(f"{pedido.title()} adicionado à sua pizza!")
        ingredientes.append(pedido)
print("Sua pizza contém os seguintes ingredientes:")
for ingrediente in ingredientes:
    print(f"{ingrediente.title()}")
# %%
# 7.5 - Ingressos de Cinema
idade = ''
while idade != 'quit':
    idade = input("Digite sua idade para saber o preço do ingresso:")
    if idade == 'quit':
        break
    elif int(idade) < 3:
        print("Ingresso gratuito")
    elif int(idade) <= 12:
        print("Ingresso custa US$10")
    elif int(idade) > 12:
        print("Ingresso custa US$15")
# %%
# 7.6 - Três Saídas
pedido = ''
ingredientes = []
active = True
while active:
    pedido = input("Digite o ingrediente da sua pizza:")
    if pedido.lower() == 'quit':
        active = False
    else:
        print(f"{pedido.title()} adicionado à sua pizza!")
        ingredientes.append(pedido)
print("Sua pizza contém os seguintes ingredientes:")
for ingrediente in ingredientes:
    print(f"{ingrediente.title()}")
# %%
# 7.8 - Lanchonete
sandwich_orders = ['s1', 's2', 'pastrami', 's3', 's4', 'pastrami', 's5', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Seu lanche {current_sandwich.title()} está pronto")
    finished_sandwiches.append(current_sandwich)

print("Foram servidos os seguintes lanches:")

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")

# %%
# 7.9 - Sem pastrami
sandwich_orders = ['s1', 's2', 'Pastrami', 's3', 's4', 'pAstrami', 's5', 'PASTRAMI']

sandwich_orders_lower = []

finished_sandwiches = []

for item in sandwich_orders:
    sandwich_orders_lower.append(item.lower())

print("Lanchonete está sem 'pastrami'")

while 'pastrami' in sandwich_orders_lower:
    sandwich_orders_lower.remove('pastrami')

while sandwich_orders_lower:
    current_sandwich = sandwich_orders_lower.pop()
    print(f"Seu lanche {current_sandwich.title()} está pronto")
    finished_sandwiches.append(current_sandwich)

print("Foram servidos os seguintes lanches:")

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")

# %%
# 7.10 - Férias tão sonhadas
active = True
dict = {}

while active:
    name = input("Qual seu nome?")
    place = input("Se pudesse visitar qualquer lugar do mundo, para onde iria?")
    dict[name] = place
    answer = input("Deseja continuar com a pesquisa? Yes/No")
    if answer == 'No':
        active = False

for k, v in dict.items():
    print(f"O sonho de {k.title()} é visitar {v.title()}")