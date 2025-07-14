# Diccionarios base

catalogo = {
    'A52S': ['Samsung', 6.5, '6GB', 'Interno', '128GB', 'Snapdragon 778G', 'Triple'],
    'IP12': ['Apple', 6.1, '4GB', 'Interno', '64GB', 'A14 Bionic', 'Dual'],
    'M13': ['Xiaomi', 6.5, '6GB', 'Interno', '128GB', 'MediaTek G80', 'Triple'],
    'NOKG21': ['Nokia', 6.5, '4GB', 'Interno', '64GB', 'Unisoc T606', 'Doble']
}

inventario = {
    'A52S': [259990, 15],
    'IP12': [599990, 3],
    'M13': [199990, 0],
    'NOKG21': [149990, 20]
}

# Función 1: Ver stock por marca
def stock_marca(marca):
    total = 0
    for modelo, datos in catalogo.items():
        if datos[0].lower() == marca.lower():
            total += inventario[modelo][1]
    print(f"El stock es: {total}")

# Función 2: Buscar celulares por precio
def buscar_precio(p_min, p_max):
    disponibles = []
    for modelo, datos in inventario.items():
        precio, stock = datos
        if p_min <= precio <= p_max and stock > 0:
            marca = catalogo[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
    if disponibles:
        disponibles.sort()
        print("Los celulares disponibles son:", disponibles)
    else:
        print("No hay celulares en ese rango de precios.")

# Función 3: Actualizar precio
def actualizar_precio(modelo, precio):
    if modelo in inventario:
        inventario[modelo][0] = precio
        return True
    else:
        return False

# Función menú principal
def menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Ver stock por marca.")
        print("2. Buscar celulares por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            buscar_precio(p_min, p_max)

        elif opcion == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                    exito = actualizar_precio(modelo, nuevo_precio)
                    if exito:
                        print("¡Precio actualizado!")
                    else:
                        print("¡El modelo no existe!")
                except ValueError:
                    print("Debe ingresar un valor entero.")
                
                continuar = input("Desea actualizar otro precio (s/n)?: ").lower()
                if continuar != "s":
                    break

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

# Punto de entrada del programa
def main():
    menu()

# Ejecutar el programa
if __name__ == "__main__":
    main()
