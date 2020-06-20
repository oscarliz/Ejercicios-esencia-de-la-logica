print("Leer dos numeros y mostrar todos los numeros terminados en 4 comprendidos entre ellos\n")
num = int(input("ingrese el divino numero: "))
num2 = int(input("ingrese su seguno divino numero: "))

for i in range(num,num2):
  num = str(i)

  if num[-1] == "4":
    print(i)
    pass

input()
