

class usuarios:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

usuarioX = input("Escribir nombre de usuario: ")
passwordX = input("Escribir password: ")
user1 = usuarios(usuarioX, passwordX)
print(f"El nuevo usuario {user1.nombre} escribio el password {user1.password} ")

