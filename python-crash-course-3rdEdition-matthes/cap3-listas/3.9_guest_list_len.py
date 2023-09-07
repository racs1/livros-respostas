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
