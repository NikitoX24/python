num1 = 5
num2 = "1"

try:
  print(num1 + num2)
except:
  print("Se ha producido un error")
else: # opcional
  print("Sigue el codigo...") # si no hay error, se imprime
finally: # opcional
  print("el final de la excepcion") # se imprime siempre




# Tipos de errores
try:
  print(num1 + num2)
except ValueError:
  print("Se ha producido un ValueError")
except TypeError:
  print("Se ha producido un TypeError")





# info del error
try:
  print(num1 + num2)
except Exception as error:
  print(error)