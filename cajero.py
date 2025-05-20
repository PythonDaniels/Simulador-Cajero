passw = 8388


# Solicitud y verificacion del pin ingresado

while True:
    pas = int(input("Ingrese su pin: "))   
    if pas == passw:
        break
    else:
        print("ERROR: Pin incorrecto")


#  // Sistema de conteo de valores

# arch = open("valores.txt","r")
## añadir sistema de open para poder actualizar cuenta del usuario en el momento y registrar sus datos ##
     # SOLUCIONAR ERROR
cuenta_bancaria = 20300

print("// Menu de finanzas //") 
print("")
print("1 - Consultar saldo")    
print("2 - Retirar dinero")    
print("3 - Cargar dinero")   
print("4 - Ayuda")   
print("5- Salir del menu")      
    
print("")
opcion = int(input("Ingrese una opcion: "))

while True:
    try:
        if opcion == 1:
            print(f" ${cuenta_bancaria}")
            break
        elif opcion == 2:
            retirar = int(input("Ingrese el monto a retirar "))
            if retirar < cuenta_bancaria:
                print(f"Dinero retirado: $ {retirar}")
                cuenta_bancaria -= retirar
                print(f"Saldo actual: $ {cuenta_bancaria}")
                break
            elif retirar > cuenta_bancaria:
                print("ERROR: No tienes saldo suficiente")
                
        elif opcion == 3:
            carga = int(input("Ingrese el monto a cargar: "))
            cuenta_bancaria += carga
            print(f"Dinero cargado a su cuenta: {carga}")
            print(f"Saldo total actual {cuenta_bancaria}")
            break
        elif opcion == 4:
            print("")
            print("Menu de ayuda")
            print("1 - cambiar pin")  # AGREGAR LA OPCION DE CAMBIAR PIN CON EL OPEN
            print("2 - Salir del menu")
            print("Contacto: moreiradanix@gmail.com")
            ayuda = int(input("Seleccione opcion: "))

        elif opcion == 5:
            print("Operacion cancelada")
            break
    except ValueError:
        print("Ingrese una opcion correcta")


        
        
