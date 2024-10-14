# No es una estructura ordenada 
# y no se repiten los elementos

my_set1 = set()
my_set2 = {} # diccionario inicialmente

my_set = {"nico", 25} # set

# modificaciones:
# my_set1[1]
my_set.add("pasino")
my_set.remove("pasino")
my_set.clear()

# Comprobar si existe el elemento:
print("nico" in my_set) # true
print("asd" in my_set) # false

my_oter_set = {"maure", "brais"}
my_new_set = my_set.union(my_oter_set) # Unir sets
my_difference_set = my_set.difference(my_oter_set) # Ver diferencias

my_list_of_set = list(my_set) # convertir a lista

