chefAprendiz = 0
chefMaestro = 0
contadorchefs = 0

while contadorchefs <= 0:
    try:
        contadorchefs = int(input("agrega la cantidad de chefs a registrar: "))

        if contadorchefs < 0:
        
            print("el numero debe ser positivo y mayor a 0")  
    except ValueError:
        print("Solo se pueden escribir numeros")

for i in range (contadorchefs):
    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("ingresa la experiencia del chef (1 al 10): "))
            if experiencia > 5:
                print("registrado con exito")
                chefMaestro = chefMaestro +  1
            else:
                print("registrado con exito")
                chefAprendiz = chefAprendiz + 1
        except ValueError:
            print("solo se pueden escribir numeros")


    codigoCulinario = ""
    while len(codigoCulinario) < 8:
        codigoCulinario = input("ingrese su codigo culinario(8 digitos como minimo): ").lower().replace()
        if len(codigoCulinario) >= 8:
            print("codigo culineario registrado")
        else:
            print("el codigo culinario debe ser mayor a 8")

print ( "la escuela cuenta con ", chefAprendiz, "chefs aprendices y", chefMaestro, "chefs maestros, !A COCINAR¡")
    


    






    