# %%
# 1 - Restaurante

class Restaurante:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Informação 1: {self.name}\nInformação 2: {self.cuisine_type}")

    def open_restaurant(self):
        print("O restaurante está aberto!")
    
r = Restaurante('Outback', 'Comida Urbana')

print(f"O nome do Restaurante é: {r.name}")
print(f"O tipo da comida é: {r.cuisine_type}\n")

r.describe_restaurant()
r.open_restaurant()

# %%
# 2 - Três Restaurantes

class Restaurante:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Informação 1: {self.name}\nInformação 2: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("O restaurante está aberto!")

r1 = Restaurante('Redbake', 'Comida Saudável')
r2 = Restaurante('Méqui', 'Fast Food')
r3 = Restaurante('Laça Burguer', 'Lanches e Refeições')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

# %%
# 3 - Usuários

class User:
    """Representação de um Usuário"""
    def __init__(self, first_name, last_name, email, id):
        """Inicializa os atributos para descrever um usuário"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id

    def describe_user(self):
        """Retorna um descritivo resumido de um usuário"""
        print(f"\nNome: {self.first_name.title() + self.last_name.title()}\nE-mail: {self.email}\nID: {self.id}")
    
    def greet_user(self):
        """Retorna cumprimento personalizado ao usuário"""
        print(f"Bem vindo {self.first_name}!")

u1 = User('Peter', 'Jack', 'pj@gmail.com', '88888')
u1.greet_user()    
u1.describe_user()

# %%
# 4 - Pessoas atendidas

class Restaurante:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Informação 1: {self.name}\nInformação 2: {self.cuisine_type}")

    def open_restaurant(self):
        print("O restaurante está aberto!")
    
    def set_number_served(self, clientes):
        self.number_served = clientes

    def increment_number_served(self, incremento):
        self.number_served += incremento
    
restaurant = Restaurante('La Pausa', 'Prato Feito')

print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.set_number_served(101)
print(restaurant.number_served)
restaurant.increment_number_served(14)
print(restaurant.number_served)

# %%
# 5 - Tentativas de login

class User:
    """Representação de um Usuário"""
    def __init__(self, first_name, last_name, email, id):
        """Inicializa os atributos para descrever um usuário"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id
        self.login_attempts = 0 

    def describe_user(self):
        """Retorna um descritivo resumido de um usuário"""
        print(f"\nNome: {self.first_name.title() + self.last_name.title()}\nE-mail: {self.email}\nID: {self.id}")
    
    def greet_user(self):
        """Retorna cumprimento personalizado ao usuário"""
        print(f"Bem vindo {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

u1 = User('Diego', 'Souza', 'diego@gmail', '87')
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.login_attempts
u1.reset_login_attempts()
u1.login_attempts
