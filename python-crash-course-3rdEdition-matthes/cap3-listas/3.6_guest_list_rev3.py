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

