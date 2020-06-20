print("Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números negativos hay. ")



count=1
lista=[]
while count<11:                
  numero=int(input("Introduzca su %d numero:" %(count)))
  lista.append(numero)
  count=count+1
contador=0
  
for x in lista:
  if x < 0:
    contador+=1
    
print("En esta lista hay %d numeros negativos" %(contador))

input("presiona enter para cerrar")