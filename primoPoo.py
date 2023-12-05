#determina si un numero digitado es primo, poo, crear primo, determina atributos de primo,metodo retorno de dato 
        #1 digite dato, enviar dato a const clase, metodo determina si es primo o no y retorna aprograma principal
        #2 imprimir numeros
        #guarda en la lista los primos que se den 
        #3 salir
class VerificadorPrimos:
    def es_primo(self,numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
class GuardarPrimos :
  def cargaPrimo (self,numero):
      return prims.append(numero)    
# Ejemplo de uso
comprobante = VerificadorPrimos()
guardado= GuardarPrimos ()
rep=int
prims=[]
while rep != 3:
    print("Digite\n1. verificar si su numero es primo\n2.imprimir los numeros primos\n3.salir")
    rep=int(input())  
    if rep == 1:  
        numero = int(input("\nIngrese un número para verificar si es primo: "))
        if comprobante.es_primo(numero)== True :
            guardado.cargaPrimo(numero)
    if rep == 2:
        print(prims)
         
      