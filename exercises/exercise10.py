"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_01 is true 


variable_01 = 5 and 1

resultado = variable_01 and A

print(resultado)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = "calle san juan"

variable_02 = "" and 2

resultado = Domicilio and variable_02

print(resultado)



# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"  #true

variable_03 = "mendoza 5000" or "maipu 800" #true

resultado = Domicilio and variable_03

print(resultado)
# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"] #true
variable_04 = "comprar " and ["Pan", "Aceite", "Sal"]  #true

resultado = lista_de_compras and variable_04

print(resultado)
# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534] #false
variable_05 = 5 and []  #false

resultado = lista_de_ids or variable_05

print(resultado)

# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}  #false
variable_06 = 0 or {}   #false

resultado = diccionario or variable_06

print(resultado)

# COMPLETAR - INICIO

# COMPLETAR - FIN

#assert variable_06 is False