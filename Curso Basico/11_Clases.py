class MyPerson:
  pass # ejecutar aunque no tenga nada

print(MyPerson()) # parentesis opcional


# clase
class Person:
  def __init__(self, name, surname, alias = "Sin alias"):
    self.__name = name # __Privado
    self.__surname = surname # __Privado
    self.full_name = f"{name} {surname} ({alias})"
    self.alias = alias
  
  # (Funcion dentro de la clase)
  def walk(self): 
    print(f"({self.alias}) está caminando..")

  # Funcion => return fullname
  def get_fullname(self):
    return self.full_name

my_person = Person("nicolas", "pasino")
print("Nombre Completo: " + my_person.full_name)
my_person.alias = "Nikito"
my_person.walk()