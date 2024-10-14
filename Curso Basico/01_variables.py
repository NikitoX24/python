### Variables ###

string = "My String variable"
int = 5
bool = False
variable = bool # variable como variable
del variable # borrar bariable

# int => string
int_to_str = str(int)

# Concatenación
print("Este es un ej de concatenacion:", bool, string)

# length
print(len(string))

# Variables en una sola línea.
name, surname, age = "Nicolas", "Pasino", 25

# Inputs
name = input('Cual es tu nombre? ')
print(name)

# ¿Forzar el tipo?
address: str = "Mi direccion"

# Cambiar de tipo
address = True

# variables en texto
print(f"{name} {surname}")