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
print("""\
  Esto es un titulo
      esto tiene un tab     con varios espacios en blanco
      y salto de línea que se mantienen..
""") # ""\   mantener tabs y saltos de líneas

# Formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a) # p
print(e) # o

# División
print(language[0])    # p
print(language[-2])   # o
print(language[1:])   # ython
print(language[1:3])  # yt
print(language[0:6:2])# pto
print(language[::-1]) # nohtyp (reverse)

# Metodos de string
print(language.capitalize())  # Python
print(language.upper())       # PYTHON
print(language.count("t"))    # 1
print(language.isnumeric())   # false
print("1".isnumeric())        # true
print(language.lower())       # python
print(language.lower().isupper()) # false
print(language.startswith("Py"))  # false
print(language == "PYthOn")           # false