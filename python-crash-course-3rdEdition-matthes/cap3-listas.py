# %%
#3.1 - Names

nomes = ['flavio', 'milton', 'antonio', 'anderson', 'joao', 'igor']
mensagem = f"{nomes[0].title()}\n{nomes[1].title()}\n{nomes[2].title()}\n{nomes[3].title()}\n{nomes[4].title()}\n{nomes[5].title()}"
print(mensagem)

# %%
#3.2 - Respects

nomes = ['flavio', 'milton', 'antonio', 'anderson', 'joao', 'igor']
mensagem = f"Bem vindo {nomes[0].title()}\nBem vindo {nomes[1].title()}\nBem vindo {nomes[2].title()}\nBem vindo {nomes[3].title()}\nBem vindo {nomes[4].title()}\nBem vindo {nomes[5].title()}\n"
print(mensagem)

# %%
#3.3 - Your List

carros = ['fiat', 'honda', 'toyota', 'volkswagen', 'renault', 'bmw']
mensagem = f"Bem vindo {carros[0].title()}\nBem vindo {carros[1].title()}\nBem vindo {carros[2].title()}\nBem vindo {carros[3].title()}\nBem vindo {carros[4].title()}\nBem vindo {carros[5].title()}\n"
print(mensagem)

# %%
#3.4 - Guest List

guest_list = ['thais', 'pedro', 'luiza']
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar?")

# %%
#3.5 - Guest Lista 2

guest_list = ['thais', 'pedro', 'luiza']
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar?")
print(f"{guest.title()} não irá ao jantar.")
guest_list[2] = 'alice'
guest_list.append('laura')
guest_list.append('luana')
for guest in guest_list[2:]:
    print(f"{guest.title()}, vamos jantar?")


# %%
#3.6 - Guest Lista 3

guest_list = ['thais', 'pedro', 'luiza']
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar?")
print(f"{guest.title()} não irá ao jantar.")
guest_list[2] = 'alice'
guest_list.append('laura')
guest_list.append('luana')
for guest in guest_list[2:]:
    print(f"{guest.title()}, vamos jantar?")
print('Pessoal, encontramos uma mesa maior!')
guest_list.insert(0,'rinaldo')
guest_list.insert(3,'aline')
guest_list.append('esdras')
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar? Encontramos uma mesa maior!")

# %%
#3.7 - Guest Lista 4

guest_list = ['thais', 'pedro', 'luiza']
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar?")
print(f"\n{guest.title()} não irá ao jantar.")
guest_list[2] = 'alice'
guest_list.append('laura')
guest_list.append('luana')
for guest in guest_list[2:]:
    print(f"{guest.title()}, vamos jantar?")
print('\nPessoal, encontramos uma mesa maior!')
guest_list.insert(0,'rinaldo')
guest_list.insert(3,'aline')
guest_list.append('esdras')
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar? Encontramos uma mesa maior!")
print("\nTeremos problemas na entrega da mesa. Só receberemos 02 convidados")
for guest in guest_list[2:]:
    guest_list.pop()
    print(f"{guest.title()}, infelizmente precisaremos cancelar seu convite...")
print(f"\nAtenção {guest_list[0].title()} e {guest_list[1].title()}, vocês continuam convidados!")
del guest_list[0]
del guest_list[0]
guest_list

# %%
#3.8 - Knowing World

lugares = ['portugal', 'dinamarca', 'noruega', 'alemanha','egito']
print(lugares)
print(sorted(lugares))
print(lugares)
print(sorted(lugares,reverse=1))
print(lugares)
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=1)
print(lugares)

# %%
#3.9 - Guest Lista Len

guest_list = ['thais', 'pedro', 'luiza']
for guest in guest_list:
    print(f"{guest.title()}, vamos jantar?")
print(f"{guest.title()} não irá ao jantar.")
guest_list[2] = 'alice'
guest_list.append('laura')
guest_list.append('luana')
for guest in guest_list[2:]:
    print(f"{guest.title()}, vamos jantar?")
len(guest_list)

# %%
#3.10 - Functions

bairros = ['boa viagem', 'pina', 'espinheiro', 'casa amarela', 'varzea']
#função 1: del
#função 2: sorted
#função 3: len
print(bairros)
del bairros[1]
print(bairros)
print(sorted(bairros))
len(bairros)
