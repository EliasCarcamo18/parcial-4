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
