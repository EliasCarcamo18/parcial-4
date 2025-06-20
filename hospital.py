# ejercicio 1 

# el hospital central de santiago requiere contratar nuestro servicio como desarrolladores para la administración de su emergencia a continuación solicitud de información de ingreso de cada paciente   
# 1. solicitud de rut o número de identificación  con doble validación (número de rut de 8 caracteres número ,entero , 2 código de verificación y que solo permita k y solo número desde el k al 9)

# 2. nombre y apellido del paciente con validación que no permita ingresar número ni entero ni decimales solo str 

# 3. patologías dentro de patología crear lista y agregar 5 enfermedades
#    1.heridas punzo penetrante 
#    2. virus
#    3.deshidratación
#    4. accidentes automotrices 
#    5.descompensación
#    6. cierre y volver al menú 
# en el menú que estamos principal ingresar otro paciente o salir


def validar_rut(rut): 
    rut = rut.strip().lower()
    if "-" in rut:
        cuerpo, dgv = rut.split("-")
    else:
        cuerpo = rut[:-1]
        dgv = rut[-1]

    if not cuerpo.isdigit():
        print("✖️ El cuerpo del RUT solo debe contener números.")
        return False
    elif len(cuerpo) != 8:
        print("✖️ El RUT debe tener solo 8 dígitos antes del verificador.")
        return False
    if not (dgv.isdigit() or dgv == "k"):
        print("✖️ El dígito verificador debe ser un número o la letra K.")
        return False
    return True

def validar_texto(texto):
    texto = texto.strip()
    return texto.replace(" ", "").isalpha()

def select_patologia():
    lista_patologias = [
        "Heridas punzo penetrante",
        "Virus",
        "Deshidratación",
        "Accidentes automotrices",
        "Descompensación"
    ]

    select = []

    while True:
        print("\nSeleccione una patología:")
        for i, pat in enumerate(lista_patologias, 1):
            print(f"{i}. {pat}")
        print("6. Salir y volver al menú")

        opcion = input("Ingrese una opción (1-6): ")

        if opcion == "6":
            break
        elif opcion in ["1", "2", "3", "4", "5"]:
            select.append(lista_patologias[int(opcion) - 1])
        else:
            print("✖️ Opción no válida. Intente nuevamente.")
    return select

def registro_paciente():
    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if validar_texto(nombre):
            break
        else:
            print("❌ El nombre solo debe contener letras y espacios.")

    while True:
        apellido = input("Ingrese el apellido del paciente: ")
        if validar_texto(apellido):
            break
        else:
            print("❌ El apellido solo debe contener letras y espacios.")

    while True:
        rut = input("Ingrese el RUT del paciente (ejem. 12345678-k): ")
        if validar_rut(rut):
            print("RUT válido ✔️")
            break
        else:
            print("❌ Intente nuevamente.")

    patologias = select_patologia()

    paciente = {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "patologias": patologias
    }

    print("\n✔️ Registrado correctamente")
    print(paciente)
    return paciente

def menu_principal():
    print("\n👌 Bienvenido al sistema de registro del Hospital Central 👌")

    lista_paciente = []

    while True:
        paciente = registro_paciente()
        lista_paciente.append(paciente)

        seguir = input("\n¿Desea registrar otro paciente? (s/n): ").strip().lower()
        if seguir != "s":
            print("👋 Cerrando sistema. Gracias.")
            break

# MAIN MENU
while True:
    print("\n🧾 Bienvenido al registro de pacientes - Hospital Central")
    print("\nMenu:")
    print("1. Registrar paciente")
    print("2. Ver patologías")
    print("3. Salir del sistema")

    op = input("Ingrese una opción (1-3): ")

    if op == "1":
        registro_paciente()
    elif op == "2":
        select_patologia()
    elif op == "3":
        menu_principal()
    else:
        print("❌ Opción inválida. Intente nuevamente.")
