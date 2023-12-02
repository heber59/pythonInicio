# empleado tiene cedula nombre apellido y telefono
#sueldo 40 horas, sueldo normal
#mayor que 40 y = a 48 es un 20% mas
#49 o mas valen 40% mas
def pagos (normal,extra,extraDobles):
    print("hola")

def extra():
    print("extra")

def extraDobles():
    print("extradobles")

def normal():
    print("normal")


def registro():
    datos = []
    datos.append(input(" ingrese el nombre de el empleado\n"))
    datos.append(input(" ingrese el apellido de el empleado\n"))
    datos.append(input(" ingrese el telefono de el empleado\n"))
    datos.append(input(" ingrese la cedula de el empleado\n"))
    print(datos)
    datosConfirmar = int
    while datosConfirmar != "n" :
        datosConfirmar=int(input(" Desea modificar datos s/n "))
        if datosConfirmar == "s":
            print("ingrese el dato que va a modificar")
            cambio= input()
            if cambio in datos:
                print("cual es el nuevo dato que desea")
                nuevoDato=input()
                

        





def imprimir():
    print("imprime")


repBucle = int
while  repBucle  != 4 :
    repBucle=int(input("1.registar empleado\n2.registrar horas trabajadas y pago\n3.imprimir datos\n4.salir\n"))
    if repBucle == 1 :
        registro()
    elif repBucle == 2:
        pagos(normal(),extra(),extraDobles())
    elif repBucle == 3:
        imprimir()