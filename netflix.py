# ejercicio 2 

# La empresa internacional de entretenimiento netflix  requiere de nuestro servicios profesionales para realizar su última interfaz de selección y catálogo de películas 
# 1. nombre de la película obligatoria

# 2. lista de categorías
#    1. ciencia ficción 
#    2 acción
#    3 terror
#    4 cómicas
#    5 salir al menú anterior  

# 3 tiempo de duración de la película 
# 4 salir o añadir otra película 

def registro_de_peliculas():
    
    nombre = input("Ingrese el nombre de la pelicula")
    if nombre.replace(" ","").isalpha():
        print()
    else:
        print("Carater ingresado no permitido , porfavor ingrese solo letras")   
        return 
    duracion = input("Ingrese da duracion de la pelicula ")
    if duracion.isdigit and int(duracion) >0:
        print(F"la pelicula dura {duracion} minutos ")
    else:
        print("error, ingrese numeros enteros mayores a 0 ")    
        return
   
def categorias():
    
    print("\n Seleccione una categoria")
    print("1. Ciencia Ficcion")
    print("2. accion")
    print("3. terror")
    print("4. comicas")
    print("5. volver al menu principal")
    
    opcion = input("Ingrese una opcion (1-5): ")
    
    categorias ={
        "1":"Ciencia Ficcion",
        "2":"Accion",
        "3":"Terror",
        "4":"Comicas"
    }
    
    if opcion in categorias:
        print(f"Categoria seleccionada {categorias[opcion]}")
    elif opcion =="5":
        print("Volviendo al menu principal...")
    else:
        print("Opcion invalida , ingrese nuevamente su opcion ")        

peliculas =[] 
def registro_peliculas():
    
    pelicula ={
        "nombre":nombre,
        "categorias":categorias,
        "duracion": int(duracion)
    }    
    
    peliculas.append(pelicula)
     
while True:
    
    print("\n Bienvenido a Netflix ")
    print("1. registrar Pelicula")
    print("2. Selecionar la categoria ")
    print("3. salir")
    
    op = input("Ingrese una opcion (1-3): ")
    
    if op =="1":
        registro_de_peliculas()
    elif op =="2":
        categorias()
    elif op =="3":
        salir = input("Desea ingresar otra pelicula ?(s/n): ")
        
        if salir.lower()== "s":
            print("volviendo al menu principal")
        else:
            print("Gracias por regitrar tu pelicula en Netflix") 
            break      
                            