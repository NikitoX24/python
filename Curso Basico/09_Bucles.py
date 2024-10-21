
# FOR
frutas = ["manzana", "banana", "naranja", "pera", "uvas"]

for fruta in frutas:
    if fruta == "naranja": 
       continue # ignorar
    print(fruta)
else:
  print("Fin del bucle")



# While
contador = 0

while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
        break # terminar bucle