print("Programa que acepta dos numeros y determina cual es el mayor")
n1 = int(input("igrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))


if n2 < n1:
    print("El primer numero es mayor",n1)
elif n1 < n2:
    print("El segundo numero es mayor",n2)


input("Precione Enter Para Salir")