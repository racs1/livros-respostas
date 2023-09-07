# %%
# 6.1 - Pessoa
dict_pessoa = {
    'first_name': 'rodolfo',
    'last_name': 'silva',
    'age': 30,
    'city': 'recife',
}
print(f"{dict_pessoa['first_name']}, {dict_pessoa['last_name']}, {dict_pessoa['age']}, {dict_pessoa['city']}")

# %%
# 6.2 - Números favoritos
dict_num = {
    'rodolfo': 10,
    'thais': 28,
    'pedro': 13,
    'luiza': 25,
    'rinaldo': 5,
}
print(f"{dict_num.keys()}, {dict_num.values()}")

# %%
# 6.3 - Glossário
dict_glossario = {
    'if': '',

}

# %%
# 6.5 - Rios
dict_rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtze': 'china',
}

for k,v in dict_rios.items():
    print(f"O {k} atravessa o {v}")

for k in dict_rios.keys():
    print(f"Nome do Rio: {k}")

for v in dict_rios.values():
    print(f"País: {v}")

# %%
# 6.6 - Pesquisa
dict_linguagens = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

pessoas = ['rodolfo', 'pedro', 'jen', 'edward', 'phil', 'thais']

for pessoa in pessoas:
    if pessoa in dict_linguagens.keys():
        print(f"{pessoa.title()}, obrigado pela resposta!")
    else:
        print(f"{pessoa.title()}, poderia participar da pesquisa?")

# %%
# 6.7 - Pessoas 2
dict_pessoa = {
    'first_name': 'rodolfo',
    'last_name': 'silva',
    'age': 30,
    'city': 'recife',
}

dict_pessoa1 = {
    'first_name': 'thais',
    'last_name': 'torres',
    'age': 20,
    'city': 'recife',
}

dict_pessoa2 = {
    'first_name': 'pedro',
    'last_name': 'torres',
    'age': 00,
    'city': 'recife',
}

people = [dict_pessoa, dict_pessoa1, dict_pessoa2]

for pessoa in people:
    print(pessoa)

# %%
# 6.8 - Pets
dict_cachorro = {
    'tipo': 'cachorro',
    'dono': 'antonio',
}

dict_gato = {
    'tipo': 'gato',
    'dono': 'fabiana',
}
pets = [dict_cachorro, dict_gato]

for pet in pets:
    print(pet)

# %%
# 6.9 - Lugares Favoritos
favorite_places = {
    'rodolfo': ['berlim', 'moscou'],
    'thais': ['londres', 'toquio'],
    'pedro': ['oslo'],
}

for pessoas,lugares in favorite_places.items():
    print(f"\n{pessoas.title()}'s favorite places:")
    for lugar in lugares:
        print(f"{lugar.title()}")

# %%
# 6.10 - Números Favoritos 2
dict_num = {
    'rodolfo': [10, 20, 30],
    'thais': [28, 3, 13],
    'pedro': [13, 2, 23],
    'luiza': [25, 5],
    'rinaldo': [5, 3],
}

for pessoa, numero in dict_num.items():
    print(f"\n{pessoa.title()}'s favorite numbers:")
    for num in numero:
        print(num)

# %%
# 6.11 - Cidades
cities = {
    'recife': {
        'país': 'brasil',
        'população': '1M5',
        'fato': 'capital de PE',
    },
    'olinda': {
        'país': 'brasil',
        'população': '400K',
        'fato': 'terra do carnaval',
    },
    'paulista': {
        'país': 'brasil',
        'população': '330K',
        'fato': 'gil do vigor',
    },
}

for cidades, infos in cities.items():
    print(f"\nDados de {cidades.title()}:")
    for info, descricao in infos.items():
        print(f"{info.title()}: {descricao.title()}")

