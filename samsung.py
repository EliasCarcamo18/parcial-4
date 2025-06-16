# las personas de samsung en busca de un desarrolador en python que sea capaz de hacer la agenda de su ultimo telefono la ceual debe ser capaz de registrar
# nombre apellido ,dirrecion , fecha de cumapleaños , correo , telefono
# ademas debe de ser capaz de ser accesible para poder consultar los contactos ingresados
# eliiminar
# modificar
# actualizar y guardar 


agenda =[]

def registro_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido =input("Ingrese el apellido del usuario: ")
    direccion = input("Ingrese la direccion de el usuario: ")
    nacido = input("Ingrese la fecha de nacimiento del usuario (dd/mm/aaaa): ")
    telefono = input("Ingrese el numero de telefono del usuario: ")
    correo= input("ingrese su correo: ")
    
    contacto ={
        "nombre":nombre,
        "apellido":apellido,
        "direccion":direccion,
        "nacido":nacido,
        "telefono":telefono,
        "correo":correo
    }
    
    agenda.append(contacto)
    print("Contacto registrado con exito✔️")
    
def mostrar_contacto():
    
    if not agenda:  
        print("La agenda se encuentra vacia , porfavor ingrese un usuario")  
        return
    else:
        for i , contacto in enumerate(agenda):
            print(f"{i+1}. {contacto['nombre']}.{contacto['apellido']} - Tel:{contacto['telefono']}.")  
            
def eliminar_contacto():
    
    mostrar_contacto()
    try:
         
        if not agenda:  
            print("La agenda se encuentra vacia , porfavor ingrese un usuario")  
            return
        idx=int(input("Ingrese el numero del contacto que desea eliminar: ")) -1   
        if 0 <= idx < len(agenda):
            eliminado = agenda.pop(idx)
            print(f"contacto {eliminado['nombre']} eliminado.")
        else:
            print("Numero ingresado invalido✖️")        
    except ValueError:
        print("Ingrese un numero valido")
        
        
def modificar_usuario():
    
    mostrar_contacto()
    try:
         
        if not agenda:  
           print("La agenda se encuentra vacia , porfavor ingrese un usuario")  
           return
        idx=int(input("Ingrese el numero a modificar: ")) -1
        if 0 <= idx < len(agenda):
            print("Ingrese los datos que desea modificar , ( deje vacio los datos que quiere que se mantengan )")
            contacto = agenda[idx]  
            nuevo_nombre = input(f"Nombre [{contacto['nombre']}]: ") or contacto['nombre']   
            nuevo_apellido = input(f"Apellido [{contacto['apellido']}]: ") or contacto['apellido'] 
            nuevo_direccion = input(f"Direccion [{contacto['direccion']}]: ") or contacto['direccion'] 
            nuevo_nacido = input(f"Cumpleaños [{contacto['nacido']}]") or contacto['nacido'] 
            nuevo_telefono = input(f"Telefono [{contacto['telefono']}]: ") or contacto['telefono'] 
            nuevo_correo = input(f"Correo [{contacto['correo']}]: ") or contacto['correo']     
            
            agenda[idx] = {
                "nombre":nuevo_nombre,
                "apellido": nuevo_apellido,
                "direccion": nuevo_direccion,
                "nacido":nuevo_nacido,
                "telefono":nuevo_telefono,
                "correo":nuevo_correo
            } 
            
            print("Contacto actualizado con exito ✔️")                       
        else:
            print("Numero invalido")      
    except ValueError:
        print("Ingrese un numero valido ")
    

##main 

while True:
    print("\n Menu de registro ")
    print("1. Registro de usuario")
    print("2. Mostrar usuario ")
    print("3. Eliminar usuario")
    print("4. Modificar usuario")
    print("5. salir o ingresar otro usuario")
    
    op= input("Ingrese una opcion (1-5): ")
    
    if op =="1":
        registro_usuario()
    elif op =="2":
        mostrar_contacto()
    elif op == "3":
        eliminar_contacto()
    elif op == "4":
        modificar_usuario()
    elif op == "5":
        salida = input("desea salir del programa? (S/N): ")
        if salida.upper() == "S":
            print("Saliendo del programa...")
        elif salida.upper() == "N":
            print("Volviendo al menu principal👌")    
    else:
        print("opcion invalida")                  