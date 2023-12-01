def pot ():    
 base = float(input("Ingrese la base: "))
 exponente = int(input("Ingrese el exponente: "))

 # Inicializar el resultado a 1
 resultado = 1

 # Calcular la potencia usando un bucle
 if exponente >= 0:
    for _ in range(exponente):
        resultado *= base
 else:
    for _ in range(abs(exponente)):
        resultado /= base       
 print("la respuesta es:",resultado)

rep = int
while rep != 2:
    print("que quiere hacer \n1.sacar potencia\n2.salir")
    rep= int(input())
    if rep == 1:
        pot()
