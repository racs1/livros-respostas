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

