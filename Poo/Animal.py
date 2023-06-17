class Animal:
    #Atributos
    nombre="" #Atributo estatico 
    edad=0

    #Metodos

    #Metodos constructor
    def __init__(self,n,e):
        self.nombre=n
        self.edad=e

    #Metodos propios de la clase 
    def registrarAnimal(self):
        self.nombre=input("Ingrese el nombre del animal ")
        self.edad=int(input("Ingrese la edad del animal "))

    def mostrarAnimal(self):
        print("El nombre del animal es ", self.nombre,"y la edad es", self.edad)
        #print(f"El nombre del animal es  {self.nombre}y la edad es {self.edad}")
    def duplicarEdad(self, edad):
        resultado=edad*2
        return resultado
    
    def cambiarNombre(self):
        cambiarNombre = input("ingrese el nombre del animal")
        self.nombre=cambiarNombre
        print("El nuevo nombre es", self.nombre)
    #def cambiarNmobre(self):


#Crear un objeto o instanciar clase
# tigre= Animal()

# tigre.nombre="Tony"
# tigre.edad=5

# print("El nombre del animal es ", tigre.nombre, "y su edad es ", tigre.edad)

# panda=Animal()

# panda.nombre="Antifaz"
# panda.edad=6

# print("El nombre del animal es ", panda.nombre, "y su edad es ", panda.edad)
