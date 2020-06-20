n1 = 0
while True:
	print("EQ de notas")
	n1 = int(input("digite la nota: "))
	
	formul = (n1)/1
	print("su promedio es: "+ str(formul))
	if formul >=90:
		print("su nota es A")

	elif formul >=80:
		print("su nota es B")

	elif formul >=70:
		print("su nota es C")

	elif formul <=60:
		print("su nota es F")


	input()





