contador = 0
suma = 0
temperaturaAlta = 0
for contador in range(5):
    temperatura = int(input("Ingrese una temperatura: "))
    suma = temperatura + suma
    if temperatura > 20:
        temperaturaAlta = temperaturaAlta + 1

totaltemperatura = suma/5
print ("El total de la temperatura es de", suma, ", que tiene un promedio de", totaltemperatura, "grados celsius")
print("la temperatura supero los 20°C", temperaturaAlta, "veces")



