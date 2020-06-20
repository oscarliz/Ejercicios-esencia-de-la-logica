

print("Leer 10 números enteros, almacenarlos en un vector y determinar si existe al menos un número repetido. ")


n = input("intruduzca 10 numeros separados por coma: ")
n = n.split(",")

total = 0 
d = {}

for letra in n:
	if letra in d:
		d[letra]=d[letra]+1

	else:
		d[letra]=1

print(d)


    



input()