# %%
#2.1 - Simple Message
mensagem = "Mensagem simples - exercício 1"
print(mensagem)
# %%
#2.2 - Simple Messages
mensagem = "mensagem original"
print(mensagem)
mensagem = "mensagem alterada"
print(mensagem)
# %%
# 2.3 - Personal Message
nome = "Rodolfo"
print(f"Olá {nome}, gostaria de aprender um pouco de Python hoje?")
# %%
# 2.4 - Upper Lower
nome = "roDolFo"
print(f"{nome}\n{nome.lower()}\n{nome.upper()}\n{nome.title()}")
# %%
# 2.5 - Famous Quote
print('Albert Einstein disse uma vez "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"')
# %%
# 2.6 - Famous Quote 2
famous_person = "Albert Einstein"
message = "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"
print(f'{famous_person}: "{message}" ')
# %%
# 2.7 - Remove Names
nome = "  Rodolfo   "
print(f"{nome}\n{nome.lstrip()}\n{nome.strip()}\n{nome.rstrip()}")
# %%
# 2.8 - Remove Prefix
filename = "python_notes.txt"
new_filename = filename.removesuffix('.txt')
print(f"{filename}\n{new_filename}")
# %%
# 2.9 - Number 8
adicao = 5+3
subtracao = 10-2
multiplicacao = 4*2
divisao = 16/2
print(f"{adicao}\n{subtracao}\n{multiplicacao}\n{divisao}")
# %%
# 2.10 - Favorite Number
number = 10
print(f"Meu número favorito é o {number}")
# %%
# 2.11 - Comments
#rodolfo 17-07-2023
#o programa abaixo apresenta a string "nome" em letras todas minúsculas, todas maiúsculas e a primeira letra maiúscula 
nome = "roDolFo"
print(f"{nome}\n{nome.lower()}\n{nome.upper()}\n{nome.title()}")

#rodolfo 17-07-2023
#o programa abaixo remove o sufixo da variável "filename" (remove a extensão do nome do arquivo)
filename = "python_notes.txt"
new_filename = filename.removesuffix('.txt')
print(f"{filename}\n{new_filename}")
# %%
# 2.12 - Zen Python
import this



