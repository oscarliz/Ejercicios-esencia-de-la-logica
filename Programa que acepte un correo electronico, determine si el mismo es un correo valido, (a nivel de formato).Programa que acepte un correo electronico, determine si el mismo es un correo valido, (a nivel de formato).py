n1 = input("ingrese su correo electronico: ")

if n1.find("@") == -1 or n1.find(".") == -1:
	print("no es valido este formato")
else:
	print("es valido el formato")
	pass

input()