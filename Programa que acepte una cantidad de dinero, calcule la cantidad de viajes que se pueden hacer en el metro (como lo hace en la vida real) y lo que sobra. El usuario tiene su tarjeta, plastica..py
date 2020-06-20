
dinero = int(input("Introduzca una cantidad de dinero: "))
metro = 20

if dinero < 20:
	print("Dinero insuficiente")
	pass

if dinero == 20:
	print("Ha recargado un viaje")
	pass

if dinero == 40:
	print("Ha recargado un viaje de ida y vuelta")
	pass

if  dinero > 20 and dinero != 40:
	
	n1 = int(input("Introduzca la cantidad de viajes que desee por favor: "))
	viaje2 = metro * n1 
	sobra = dinero - viaje2
	if viaje2 > dinero:
		print("Su monto no alcaza para esta cantidad de viajes")

		
	else:
		if n1 == 10 :
			sobra = sobra + 15
			pass
		if n1 == 20:
			sobra = sobra + 40
			pass
		print("Ha recargado",n1,"viajes")
		print("Le sobran", sobra)

	pass
	pass


input()
		
