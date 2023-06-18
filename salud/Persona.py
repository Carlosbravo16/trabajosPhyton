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

    def __pedirDatos(self):
        self.__tipoDoc=input("Ingrese el tipo de documento ")
        self.__documento=int(input("Ingrese el documento "))
        self.__nombre=input("Ingrese el nombre ")
        self.__apellido=input("Ingrese el apellido ")
        self.__peso=int(input("Ingrese su peso actual "))
        self.__estatura=float(input("Ingrese su estatura "))
        self.__edad=int(input("Ingrese su edad "))
        self.__sexo=input("Ingrese el genero al que pertenece ")

    def __mostrarPersona(self):
        print("El tipo de documento es ", self.__tipoDoc,"su numero de documento es", self.__documento, "su nombre es", self.__nombre, " de apellido", self.__apellido, "tiene un peso ", self.__peso, "con una estatura ", self.__estatura, "tiene una edad de ", self.__edad, "años", "de sexo ", self.__sexo)

    def __calcularlmc(self,):
        pesoActual=self.__peso / self.__estatura**2
        if pesoActual<20:
            print("El peso esta por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <=25:
            print ("El peso es ideal ")
        else:
            print("Tiene sobrepeso")
        return pesoActual
    
    def __mayorEdad(self):
        if self.__edad <18:
            print("Es menor de edad")
        else:
            print("Es mayor de edad")
