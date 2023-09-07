#rodolfo 17-07-2023
#o programa abaixo apresenta a string "nome" em letras todas minúsculas, todas maiúsculas e a primeira letra maiúscula 
nome = "roDolFo"
print(f"{nome}\n{nome.lower()}\n{nome.upper()}\n{nome.title()}")

#rodolfo 17-07-2023
#o programa abaixo remove o sufixo da variável "filename" (remove a extensão do nome do arquivo)
filename = "python_notes.txt"
new_filename = filename.removesuffix('.txt')
print(f"{filename}\n{new_filename}")
