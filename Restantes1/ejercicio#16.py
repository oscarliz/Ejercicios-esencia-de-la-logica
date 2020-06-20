print("Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los datos almacenados múltiplos de 3. ")



count=1
lista=[]
while count<11:                
  numero=int(input("Introduzca su %d numero:" %(count)))
  lista.append(numero)
  count=count+1
contador=0
lista2 = []
for x in lista:
  if x % 3 == 0:
    lista2.append(x) 
    
print("los multilplo de 3", lista2)

input("presiona enter para cerrar")