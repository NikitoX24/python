### strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

# cantidad
print(len(my_string)) 

# concatenar
print(my_string + " " + my_other_string) 


print("Este es un String\ncon salto de línea") # \n  (salto de linea)
print("\tEste es un String con tabulación") # \t     (tabulación)
print("\\tEste es un String \\n escapado") # \\      (barra invertida)

# Formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
print(language[1:3])
print(language[1:])
print(language[-2])
print(language[0:6:2])

# Reverse
print(language[::-1])

# Funciones del lenguaje
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo