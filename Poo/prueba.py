#Crear objetos desde otros archivos, ojo importacion 

from Animal import Animal
from Ave import Ave

panda=Animal()
condorito=Ave()


panda.registrarAnimal()
panda.mostrarAnimal()
panda.cambiarNombre
panda.duplicarEdad(panda.edad)
print("la edad duplicada es ", panda.duplicarEdad(panda.edad))