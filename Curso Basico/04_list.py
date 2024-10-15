my_list1 = list()
my_list2 = []

my_list = [23, 24, 85, 44, 26, 26, "nico"]

my_list[4] = 88    # cambiar un valor.
my_list.append(0)  # Agregar al ultimo.
my_list.insert(1, "insert") # Agregar en un index.
my_list.remove(44) # eliminar un elemento.
del my_list[2]     # eliminar un index.
my_list.pop()      # eliminar o extraer el último.
my_list1.clear()   # eliminar todo.
my_list[1:3]       # extraer una parte.
my_list.index("nico") # index de un elemento (el primero q encuentra).