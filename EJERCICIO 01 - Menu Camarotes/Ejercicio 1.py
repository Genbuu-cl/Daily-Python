camarotesDisponibles = 120
opcion = 0
camarotesReservados = 0
camarotesElegidos = 0
cancelarCamarotes = 0
totalReservas= 0
reservas = 0
cancelacion = 0
print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")
while opcion != 5:
    print("1. Camarotes Disponibles")
    print("2. Reservar Camarote")
    print("3. Cancelar Camarote")
    print("4. Historial De Reservas")
    print("5. Salir Del Sistema")

    opcion = int(input("Elige una opcion del menu: "))

    match opcion:
        case 1:
            print("Quedan", camarotesDisponibles, " camarotes disponibles para reservar")
        case 2:
            camarotesElegidos = int(input("Eliga cuantos camarotes quiere reservar: "))
            if camarotesElegidos <= camarotesDisponibles and camarotesElegidos > 0:
                camarotesReservados = camarotesReservados + camarotesElegidos
                camarotesDisponibles = camarotesDisponibles - camarotesElegidos
                reservas = reservas + 1
                print("camarote reservado con exito")
            elif camarotesElegidos > camarotesDisponibles:
                print("no se pueden elegir mas camarotes de los disponibles")
            elif camarotesElegidos <= 0:
                print("no se pueden elegir numeros negativos ni tampoco ceros")
        case 3:
            cancelarCamarotes = int(input("ingresa la cantidad de camarotes que quieres cancelar: "))
            if cancelarCamarotes <= camarotesReservados and cancelarCamarotes > 0:
                camarotesDisponibles = camarotesDisponibles + cancelarCamarotes
                camarotesReservados = camarotesReservados - cancelarCamarotes
                cancelacion = cancelacion + 1
                print ("camarote cancelado con exito")
            elif cancelarCamarotes > camarotesReservados:
                print("no se pueden elegir mas camarotes de los disponibles")
            elif cancelarCamarotes <= 0:
                print("no se pueden elegir numeros negativos ni tampoco ceros")
            else:
                print("no hay camarotes disponibles para cancelar")
        case 4:
            totalReservas = reservas - cancelacion
            print ("La cantidad total de reservas es de", totalReservas, "realizada durante el dia")
        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")