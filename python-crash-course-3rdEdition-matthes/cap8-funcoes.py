# %%
# 8.1 - Mensagem

def display_message():
    print("Capítulo 8 - Funções em Python")

display_message()

# %%
# 8.2 - Livro favorito

def favorite_book(title):
    print(f"Um dos meus livros favoritos é {title.title()}")

favorite_book("alice no pais das maravilhas")

# %%
# 8.3 - Camiseta

def make_shirt(tam, text):
    print(f"Tamanho da Camiseta: {tam.title()}\nTexto da Camiseta: {text.title()}\n")

make_shirt("m", "pelo sport tudo")
make_shirt(text='chegando na ilha do retiro', tam='p')

# %%
# 8.4 - Camisetas Grandes

def make_shirt2(tam='g', text='eu amo python'):
    print(f"Tamanho da Camiseta: {tam.title()}\nTexto da Camiseta: {text.title()}\n")

make_shirt2()
make_shirt2(tam='m')
make_shirt2('p', 'python é top')

# %%
# 8.5 - Cidades
"""docstring"""
def describe_city(cidade, país='brasil'):
    print(f"{cidade.title()} fica no {país.title()}.")

describe_city('recife')
describe_city('roma', 'itália')
describe_city('curitiba')

# %%
# 8.6 - Nome de cidades

def city_country(cidade, país):
    mensagem = f"{cidade.title()}, {país.title()}"
    return mensagem

ex1 = city_country('santiago', 'chile')
ex2 = city_country('recife', 'brasil')
ex3 = city_country('madrid', 'espanha')

print(ex1)
print(ex2)
print(ex3)

# %%
# 8.7 - Álbum

def make_album(artista, título):
    dict = {'Artista': {artista.title()}, 'Álbum': {título.title()}}
    return dict

d1 = make_album('offspring','americana')
d2 = make_album('legião urbana','quatro estações')
d3 = make_album('barão vermelho','acústico')

print(d1.values(), d2.values(), d3.values())

# %%
# 8.7 - Álbum (v2)

def make_album(artista, título, tracks=None):
    dict = {'Artista': {artista.title()}, 'Álbum': {título.title()}}
    if tracks:
        dict['tracks'] = tracks
    return dict

d4 = make_album('alceu valença', 'anunciação', tracks=10)
print(d4)

# %%
# 8.8 - Álbuns de usuários

def make_album(artista, título, tracks=None):
    dict = {'Artista': {artista.title()}, 'Álbum': {título.title()}}
    if tracks:
        dict['tracks'] = tracks
    return dict

while True:
    print("Favor inserir os dados abaixo")
    print("(entre com 'q', a qualquer tempo, para sair)")
    art1 = input("Insira o artista:")
    if art1 == 'q':
        break
    tit1 = input("Insira o título do álbum:")
    if tit1 == 'q':
        break
    album_formatado = make_album(art1, tit1)
    print(f"\nRegistro: {album_formatado}\n")

# %%
# 8.9 - Mágicos

def show_magicians(lista):
    for item in lista:
        msg = "Olá, " + item.title() + "!"
        print(msg)

magicos = ['igor', 'rodrigo', 'rodolfo']
show_magicians(magicos)

# %%
# 8.10 - Grandes Mágicos

def show_magicians(lista):
    for item in lista:
        msg = "Olá, " + item.title() + "!"
        print(msg)
        
magicos = ['igor', 'rodrigo', 'rodolfo']
show_magicians(magicos)

def make_great(lista1, lista2):
    while lista1:
        temp = lista1.pop()
        item = "O Grande " + temp.title()
        lista2.append(item)

magicos_rev1 = []
make_great(magicos, magicos_rev1)
print("\n")
show_magicians(magicos)
print("\n")
show_magicians(magicos_rev1)

# %%
# 8.11 - Mágicos inalterados

def show_magicians(lista):
    for item in lista:
        msg = "Olá, " + item.title() + "!"
        print(msg)
        
magicos = ['igor', 'rodrigo', 'rodolfo']
show_magicians(magicos)

def make_great(lista1, lista2):
    while lista1:
        temp = lista1.pop()
        item = "O Grande " + temp.title()
        lista2.append(item)

magicos_rev1 = []
make_great(magicos[:], magicos_rev1) # cópia da lista original. Lista original não será alterada
print("\n")
show_magicians(magicos)
print("\n")
show_magicians(magicos_rev1)

# %%
