# Sin parametros
def my_funcion():
  print("Esto es una función")

my_funcion()



# con parametros
def my_suma(a, b):
  print(a + b)

my_suma(1, 2)
my_suma(b = 10, a = 5) # especificar



# Valor por defecto
def my_suma(nombre, apellido, edad = "18"):
  print(nombre + apellido + edad)

my_suma("nicolas", "pasino")



# Return
def my_return(a, b):
  return a + b

resultado = my_return(10, 5)



# Parametros infinitos
def my_texts(*texts):
  for text in texts:
    print(text.upper())

my_texts("Hola a", "todo el Mundo", "!")



# Funciones anónimas (lambda)
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25



# Documentacion
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura

area_rectangulo()