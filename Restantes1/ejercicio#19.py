print("Leer 10 números enteros, almacenarlos en un vector y determinar cuál es el número menor.")

count=1
lista=[]
while count<11:                
    num=int(input("Introduzca su %d numero:" %(count)))
    lista.append(num)
    count=count+1

pivot=lista[0]
for element in lista:            
  if element < pivot:
  	pivot= element

print("El numero menor es ",pivot)
input()