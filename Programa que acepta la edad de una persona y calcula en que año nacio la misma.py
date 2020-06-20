from datetime import datetime, date, time, timedelta
print("Programa que acepta la edad de una persona y calcula en que año nacio la misma")
n2 = date.today()
n1=int(input("Introduze tu edad actual: "))


print("naciste en {}" .format(n2.year - n1))
input("Preciona Enter Para Salir")