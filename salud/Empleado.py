class Empleado():

    cargo=""
    valorHora= 0
    horastrabajadas= 0
    departamento=""

    def pedirDatos(self):
        self.nombre=input("Ingrese el nombre ")
        self.apellido=input("Ingrese el apellido ")
        self.tipoDoc=input("Ingrese el tipo de documento ")
        self.documento=int(input("Ingrese el documento "))
        self.cargo=input("Ingrese el cargo : ")
        self.valorHora=int(input("Ingrese el valor de hora de labor "))
        self.departamento = input("ingrese el area en la que trabaja")
        
    def calcularHonorarios(self):
        self.horastrabajadas =int(input("Ingrese las horas trabajadas"))
        honorarios =(self.valorHora * self.horastrabajadas) -0.966
        print("sus honorarios correspondientes son ", honorarios)

    def mostrarPersona(self):
        print("Nombre", self.nombre, "\n Apellido", self.apellido, "\n Tipo de documento ", self.tipoDoc, "horas trabajadas ", self.horastrabajadas )
