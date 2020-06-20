print("Leer dos numeros entero y mostrar todos los multiplos de 5 comprendidos entre menor y mayor\n")
num1=int(input("Digite Primer Numero"))
num2=int(input("Digite Segundo Numero"))
if(num1>num2):
    print("El primer numero debe ser menor al segundo numero digitado")
for i in range(num1+1,num2):
  if(num2>num1):
    if(i%5==0):
      print(i)
input()