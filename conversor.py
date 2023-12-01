def cambioMenor(tipo):
 bin = []
 print("que numero desea convertir:")
 number = int(input())
 while number != 0:
        numberCambiado = number //tipo
        bin.append(number-(numberCambiado*tipo))
        number = numberCambiado
 bin.reverse()       
 print("su numero es",bin)    

def cambioMayor(tipo):
    bin = []
    representacion={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    print("que numero desea convertir:")
    number = int(input())
    numberCambiado = number
    while number != 0:
      if number <tipo:
        if number in representacion:
          bin.append(representacion[number])
          return print("su numero es",bin)
        else :         
         bin.append(number)
         return print("su numero es",bin)
      if numberCambiado < tipo:
        if numberCambiado in representacion:
          bin.append(representacion[numberCambiado])
          return print("su numero es",bin)
      numberCambiado = number-((number//tipo)*tipo)
      number= number //tipo
      if number in representacion:
        bin.append(representacion[number])
        number=numberCambiado
      else: bin.append(number)       
    print("su numero es",bin) 
        
    
    
      
repBucle = int
while repBucle != 2:
 print("digite \n 1.convertir numero\n 2.salir")
 repBucle=int(input())
 if repBucle == 1:
     print ("Digite a que base desea convertir maximo 16")
     tipo = int(input())
     if tipo <= 10:
      cambioMenor(tipo)
     else :
      cambioMayor(tipo)
         
             
     
     
     
 







