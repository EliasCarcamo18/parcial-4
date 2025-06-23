#haga un programa que permita generar un menu de gestion de entradas para el concierto de noche de brujas el menu prncipal debe permitir mostrar 4 opciones
# menu principal
#1. comprar entradas
#2. consultar comprador
#3. cancelar compra
#4. continuar ingresando compradores o cerrar programa
#todas las opciones del menu deben estar implemtadas mediante funciones separadas del codigo principal (main) .
#
#intruciones opcion 1
#comprar entradas , se debe permitir ingresar el nombre del comprador , numero de indetificacin del comprador , direccion , tipo de entrada , dentro del tipo de entrada se moestrara las siguientes opciones
#tipo de entradas
#1. gradas : 10.000 cpl
#2. laterales : 12.000 cpl
#3. central : 14.000 cpl
#4. vip : 50.000 cpl
#el codigo de confirmacion de cada entrada , debe ser mayor a 6 digitos y menor a 9 digitos
# debe contener una letra mayuscula como minimo una letra MINUSCULA COMO MINIMO Y LOS NUMERO QUE UTE CONSIDERE NECESARIO sin espacios en blanco    

# isntruccines de opcion 2
#consultar compradores , el menu debe permitir buscar toda aquellas personas que realizaron su compra medainte su nombre o numero de identificacion ,
# el comprador asistente debe mostarse en pantalla , se debe moestrar por pantalla con todas sus datos y con el numero de identifiacion de entrada
#al no encotrarse de moestrara el siguiente mensaje "no existe comprador" de locontrario la entrada se registro exitosamente

#instruciones opcion3
# el mneu debe permitir eliminar las comprar y toda la informacion del cliente , al final debe generar el mensaje " Compra cancelada "


# #instruciones opcion 4
# debe mostrar por pantalla al presionar el numero 4 desea continuar realizando las compras de las entradas o desea salir  .

# Lista global para almacenar los compradores

# Lista global para almacenar los compradores
compradores = []

def entradas():
    print("\n--- Compra de Entradas ---")

    nombre = input("Ingrese su nombre: ").strip()
    if not nombre.replace(" ", "").isalpha():
        print("Nombre inválido, ingrese solo letras.")
        return

    identificacion = input("Ingrese su número de identificación: ").strip()

    direccion = input("Ingrese su dirección: ").strip()

    print("\nTipos de entrada:")
    print("1. Gradas - $10.000")
    print("2. Laterales - $12.000")
    print("3. Central - $14.000")
    print("4. VIP - $50.000")

    tipos = {
        "1": ("Gradas", 10000),
        "2": ("Laterales", 12000),
        "3": ("Central", 14000),
        "4": ("VIP", 50000)
    }

    op = input("Ingrese una opción (1-4): ")

    if op not in tipos:
        print("Opción no válida.")
        return

    tipo_entrada, precio = tipos[op]

    codigo = input("Ingrese un código de confirmación [7-8 caracteres], con mayúsculas, minúsculas y números: ").strip()

    if not (6 < len(codigo) < 9):
        print("Código inválido. Debe tener entre 7 y 8 caracteres.")
        return
    if not any(c.isupper() for c in codigo):
        print("Debe contener al menos una letra mayúscula.")
        return
    if not any(c.islower() for c in codigo):
        print("Debe contener al menos una letra minúscula.")
        return
    if not any(c.isdigit() for c in codigo):
        print("Debe contener al menos un número.")
        return
    if " " in codigo:
        print("El código no debe contener espacios.")
        return

    comprador = {
        "Nombre": nombre,
        "id": identificacion,
        "Direccion": direccion,
        "tipo": tipo_entrada,
        "precio": precio,
        "codigo": codigo
    }

    compradores.append(comprador)
    print(f"\n✅ Compra realizada exitosamente para {nombre}.")

def consulta_entradas():
    print("\n--- Consulta de Entradas ---")
    buscar = input("Ingrese el nombre o número de identificación del comprador: ").strip()

    encontrado = False
    for c in compradores:
        if c["Nombre"] == buscar or c["id"] == buscar:
            print("\n🎫 Datos del comprador:")
            print(f"Nombre: {c['Nombre']}")
            print(f"ID: {c['id']}")
            print(f"Dirección: {c['Direccion']}")
            print(f"Tipo de entrada: {c['tipo']} - ${c['precio']}")
            print(f"Código de confirmación: {c['codigo']}")
            encontrado = True
            break

    if not encontrado:
        print("✖️ No existe este comprador ✖️")

def cancelar_compra():
    print("\n--- Cancelar Compra ---")
    busqueda = input("Ingrese el nombre o número de identificación para cancelar: ").strip()

    for i, c in enumerate(compradores):
        if c["Nombre"] == busqueda or c["id"] == busqueda:
            compradores.pop(i)
            print("🗑️ Compra cancelada.")
            return

    print("✖️ No existe comprador para cancelar.")

def continuar_salir():
    op1 = input("¿Desea continuar ingresando compradores? (s/n): ").strip().lower()
    if op1 == "s":
        return True
    else:
        print("Gracias por usar el sistema. Hasta pronto.")
        return False

# Menú principal
while True:
    print("\n--- Menú Principal - Concierto Noche de Brujas ---")
    print("1. Comprar entradas")
    print("2. Consultar comprador")
    print("3. Cancelar compra")
    print("4. Continuar o salir del programa")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        entradas()
    elif opcion == "2":
        consulta_entradas()
    elif opcion == "3":
        cancelar_compra()
    elif opcion == "4":
        if not continuar_salir():
            break
    else:
        print("Opción inválida. Intente de nuevo.")
