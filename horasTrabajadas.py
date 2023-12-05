# empleado tiene cedula nombre apellido y telefono
#sueldo 40 horas, sueldo normal
#mayor que 40 y = a 48 es un 20% mas
#49 o mas valen 40% mas
class horas (empleado):
    def pagos (pagoTotal):
        print("Digite cuantas horas trabajo",datos[0])
        numHoras=int(input())
        print("Digite cuanto se le paga la hora")
        pagoHora=int(input())
        print(pagoHora, pagoHora+1)
        if numHoras > 48 :
            for _ in range (numHoras-48) :
                pagoTotal = pagoHora + pagoTotal + (pagoHora*0.4)
                numHoras -= 1
        if numHoras > 40 : 
            for _ in range (numHoras-40) :
                pagoTotal = pagoTotal + pagoHora+(pagoHora*0.2)
                numHoras -= 1
        pagoTotal = pagoTotal + (numHoras*pagoHora)  
        pagoTotalizado = pagoTotal
        return pagoTotal 
class empleado :               
    def registro(self):
        datos.append(input(" ingrese el nombre de el empleado\n"))
        datos.append(input(" ingrese el apellido de el empleado\n"))
        datos.append(input(" ingrese el telefono de el empleado\n"))
        datos.append(input(" ingrese la cedula de el empleado\n"))
        return  datos
class valor_h:
    def imprimir():
        print("|  ",datos)
        print("|")
        print("|   genero factura por:",generarpagos)
        print("|")
  
#Utilizando el programa del sueldo del empleado, diseñar el siguiente programa con el paradigma orientado a objetos
#Crear las siguientes clases:
#1. clase empleado(Cedula, nombre, teléfono)
#2. Clase horas, subclase de empleado(numHoras)
#3. Clase Valorh, subclase de horas(Valor_h)
#Se contara con el siguiente menú de opciones:
#1. Ingresar empleado
#2. Consultar empleado
#3. Eliminar empleado
#4. Listar empleados 
#5. Salir
#Notas:
#El programa contará con una lista para cargar cada uno de los empleados que se ingresen, la cual será creada a partir de la clase Valorh, lo que comprobara que la herencia funciona.
#Se debe tener en cuenta que la cedula del empleado servirá de llave primaria.

pago = 0.0
datos = []
repBucle = int
while  repBucle  != 4 :
    repBucle=int(input("1.registar empleado\n2.registrar horas trabajadas y pago\n3.imprimir datos\n4.salir\n"))
    if repBucle == 1 :
        registro()
    elif repBucle == 2:
        generarpagos= pagos (pago)
    elif repBucle == 3:
        imprimir()
