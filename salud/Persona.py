class Persona:
    tipoDoc= ""
    documento=0
    nombre=""
    apellido=""
    peso=0
    estatura=0
    edad=0
    sexo=""


    # def __init__(self):
    #     pass

    # def __init__(self,tD,d,n,a,p,et,e,s):
    #     self.tipoDoc=tD
    #     self.documento=d
    #     self.nombre=n
    #     self.apellido=a
    #     self.peso=p 
    #     self.estatura=et
    #     self.edad=e
    #     self.sexo=s

    def pedirDatos(self):
        self.tipoDoc=input("Ingrese el tipo de documento ")
        self.documento=int(input("Ingrese el documento "))
        self.nombre=input("Ingrese el nombre ")
        self.apellido=input("Ingrese el apellido ")
        self.peso=int(input("Ingrese su peso actual "))
        self.estatura=float(input("Ingrese su estatura "))
        self.edad=int(input("Ingrese su edad "))
        self.sexo=input("Ingrese el genero al que pertenece ")

    def mostrarPersona(self):
        print("El tipo de documento es ", self.tipoDoc,"su numero de documento es", self.documento, "su nombre es", self.nombre, " de apellido", self.apellido, "tiene un peso ", self.peso, "con una estatura ", self.estatura, "tiene una edad de ", self.edad, "años", "de sexo ", self.sexo)

    def calcularlmc(self,):
        pesoActual=self.peso / self.estatura**2
        if pesoActual<20:
            print("El peso esta por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <=25:
            print ("El peso es ideal ")
        else:
            print("Tiene sobrepeso")
        return pesoActual
    
    def mayorEdad(self):
        if self.edad <18:
            print("Es menor de edad")
        else:
            print("Es mayor de edad")
