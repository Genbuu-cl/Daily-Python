inventario = 0
opcion = 0
venderproductos = 0
agregarproducto = 0
print("===== GESTIÓN DE INVENTARIO =====")

while opcion != 4:
    print ("1. Agregar Productos")
    print("2. Vender Productos")
    print("3. Consultar Productos")
    print("4. Salir")

    opcion = int(input("Ingresa una opcion: "))

    match opcion:
        case 1:
            try:
                agregarproducto = int(input("Cuantos productos quieres agregar a tu inventario?: "))
                if agregarproducto <= 0:
                    print ("No se pueden agregar ceros o productos en numeros negativos al inventario")
                elif agregarproducto > 0:
                    inventario = inventario + agregarproducto
                    print("Productos agregados con exito")
            except ValueError:
             print("Solo se aceptan numeros")
        case 2:
            try:
                venderproductos = int(input("Cuantos productos quieres vender?: "))
                if venderproductos < 0:
                    print("no se pueden vender productos en numeros negativos")
                elif venderproductos <= inventario and venderproductos > 0:
                        inventario = inventario - venderproductos
                        print("Productos vendidos con exito")
                        if inventario == 0:
                             print("Inventario Agotado")
                elif venderproductos > inventario:
                        print("No puedes vender mas productos de los que tienes")
                elif venderproductos == 0:
                        print("No puedes vende cero objetos")
            except ValueError:
                print("Solo se aceptan numeros")
        case 3:
            print("Tienes en tu inventario", inventario, "objetos")
        case 4:
            print("Muchas gracias, vuelva pronto")
        case _:
            print("opcion invalida")