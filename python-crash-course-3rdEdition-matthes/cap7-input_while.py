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
