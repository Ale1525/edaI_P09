from collections import namedtuple


planeta = namedtuple('planeta',['nombre','numero'])

Mercurio = planeta('Mercurio', 1)
Venus = planeta('Venus',2)
Tierra = planeta('Tierra', 3)
Marte = planeta('Marte',4)

print(Mercurio.nombre)
print(Mercurio.numero)
print(Venus[0])
print(Venus[1])

print("Campos de la tupla: {}".format(Tierra._fields))
