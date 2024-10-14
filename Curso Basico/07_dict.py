# OBJETO / Json

my_dict1 = dict()
my_dict2 = {}

my_dict = {
  # "Clave": "Valor"
  "Nombre": "Nicolas Pasino",
  "Edad": 25,
  "Altura": 1.85,
  "Casado": False,
  "Lenguajes": {"JavaScript", "C#", "Python"}
}

print(my_dict["Nombre"]) # Obtener Valor
my_dict["Nombre"] = "Brais" # Modificar
my_dict["Pais"] = "Argentina" # Añadir una clave y valor
del my_dict["Pais"] # Borrar una clave y valor
print("Clave" in my_dict) # Buscar clave

# metodos
print(my_dict.items()) # lista de items
print(my_dict.keys()) # lista de claves
print(my_dict.values()) # lista de valores
my_new_dict = my_dict.fromkeys(my_dict) # nuevo dicc(sin valores) con claves de otros dicts


print("__________________")
print(my_new_dict)
