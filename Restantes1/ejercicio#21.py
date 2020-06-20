print("Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el menor número primo. ")

count=1
lista=[]

while count<11:
  num=int(input("Introduzca su %d numero:" %(count)))
  lista.append(num)
  count=count+1
listprimo=[]

for x in lista:             
  cousin=0
  for num in range(1,x):
    if x%num==0:
      cousin+=1
    if cousin==1:
      listprimo.append(x)

pivot=listprimo[0]

for element in listprimo:
  if element < pivot:
    pivot= element

print("El mayor numero primo leido esta en la posicion %d " %(lista.index(pivot)))
input()