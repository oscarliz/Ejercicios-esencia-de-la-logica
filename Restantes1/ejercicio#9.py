print("Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor. ")




count=1
lista=[]
while count<11:                
    num=int(input("Introduzca su %d numero:" %(count)))
    lista.append(num)
    count=count+1

pivot=lista[0]
for element in lista:            
  if element > pivot:
    pivot= element   
contador = 0
for x in lista:
  if x == pivot:
    contador+=1
    
p =  contador

print("El mayor se repite ",p ,"veces")    



input()