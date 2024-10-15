### Operadores Aritméticos ###

# Operaciones con ints
print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicación
print(3 / 4) # divicion (float)
print(20 // 3) # divicion (entero)
print(10 % 3) # resto
print(2 ** 3) # exponente

print(2 ** 3 + 3 - 7 / 1 // 4) # varios

# Operaciones con strings (concatenar)
print("Hola " + "Python " + "¿Qué tal?")

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))
print("Hola " * int(2.5 * 2))



# Operadores Comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operadores Lógicos
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))