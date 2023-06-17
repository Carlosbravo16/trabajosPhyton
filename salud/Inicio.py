from Persona import Persona

from Empleado import Empleado
# persona1=Persona("CC", 1022375976, "Carlos", "Bravo", 77, 1.80, 31, "masculino")


# persona1.mostrarPersona()
persona1= Empleado()
persona1.pedirDatos()
persona1.calcularHonorarios()
persona1.mostrarPersona()


persona2=Persona()
persona2.pedirDatos()
persona2.mostrarPersona()
persona2.calcularlmc()
persona2.mayorEdad()
