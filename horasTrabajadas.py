# empleado tiene cedula nombre apellido y telefono
#sueldo 40 horas, sueldo normal
#mayor que 40 y = a 48 es un 20% mas
#49 o mas valen 40% mas
def pagos (pagoTotal):
    print("Digite cuantas horas trabajo",datos[0])
    horasTrabajadas=int(input())
    print("Digite cuanto se le paga la hora")
    pagoHora=int(input())
    print(pagoHora, pagoHora+1)
    if horasTrabajadas > 48 :
        for _ in range (horasTrabajadas-48) :
            pagoTotal = pagoHora + pagoTotal + (pagoHora*0.4)
            horasTrabajadas -= 1
    if horasTrabajadas > 40 : 
        for _ in range (horasTrabajadas-40) :
            pagoTotal = pagoTotal + pagoHora+(pagoHora*0.2)
            horasTrabajadas -= 1
    pagoTotal = pagoTotal + (horasTrabajadas*pagoHora)  
    pagoTotalizado = pagoTotal
    return pagoTotal                 
def registro():
    datos.append(input(" ingrese el nombre de el empleado\n"))
    datos.append(input(" ingrese el apellido de el empleado\n"))
    datos.append(input(" ingrese el telefono de el empleado\n"))
    datos.append(input(" ingrese la cedula de el empleado\n"))
    return  datos

def imprimir():
    print("|  ",datos)
    print("|")
    print("|   genero factura por:",generarpagos)
    print("|")
  


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
