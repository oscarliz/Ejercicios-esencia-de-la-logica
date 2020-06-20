print("Programa que acepta una frase y determine la cantidad de letras al igual que de la palabras que tiene la misma")
text = input("Escriba una frase para comenzar el conteo:")
text2 = len(text.split(" "))
text3 = len(text) 

if text2 > 1:
	text2 = len(text) - len(text.split(" "))
	print("Numero de letras:",text2 + 1)
else:
    print("Numero de letras:",text3)

print("Numero de palabras:",len(text.split(" ")))

input("Precione Enter para salir")


