print("Leer 10 números enteros, almacenarlos en un vector y determinar cuántos de los números leídos son números primos terminados en 3. ")

count=1
lista=[]

while count<11:                
  numero=int(input("Introduzca su %d numero:" %(count)))
  lista.append(numero)
  count=count+1
contador=0
lista2 = []
listanueva=[]
s= ','
for x in lista:
  x1 = str(x)
  if x1[-1] == "3":

    lista2.append(x) 
                                  
print("los primos terminados en 3", lista2)


input("presiona enter para cerrar")