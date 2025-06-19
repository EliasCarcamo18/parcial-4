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


def registro_paciente():
    
    nombre = input("Ingrese el nombre del paciente: ")
    if not nombre.isalpha():                                             #<-- el isalpha solo devuelve True si todos los caracteres son letras 
        print("Error , el nombre solo debe contener letras.")  
        
    apellido = input("Ingrese el apellido del paciente ")
    if not apellido.isalpha():
        print("Error, el apellido solo debe contener letras.")
    while True    
      rut = input("Ingrese el rut del paciente, (ejem. 123456789-k): ")    
      
        if validar_rut(rut):
            print("Rut valido ✔️")
            break 
        else:
            print("Intente nuevamente.") 
                                                                            
        
   
def validar_rut(rut): 
    
    rut = rut.strip().lower()                                       #<-- el lower hace que todo sea minuscula y que haci el codigo no genere error con la (K,k)
                                                                    #<-- el strip elimina los espacios de los datos ingresados
    if "-" in rut :
        cuerpo , dgv = rut.split("-")
    else:
        cuerpo[:-1]
        dgv[-1]  
     
    if not cuerpo.isdigit():
        print("✖️ El cuerpo del RUT solo debe contener numeros")
    elif len(cuerpo) != 8 :
        print("✖️ El Rut debe tener solo 8 digitos antes del verificador ")  
        
    if not (dgv.isdigit() or dgv == "k"):
        print("El digito verificador tiene que ser un numero o la letra K ")   