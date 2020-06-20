print("Leer 10 números enteros, almacenarlos en un vector y determinar cuántos datos almacenados son múltiplos de 3.")



count=1
lista=[]
while count<11:                
  numero=int(input("Introduzca su %d numero:" %(count)))
  lista.append(numero)
  count=count+1
contador=0
  
for x in lista:
  if x % 3 == 0:
    contador+=1
    
print("En esta lista hay %d multiplos de 3" %(contador))

input("presiona enter para cerrar")