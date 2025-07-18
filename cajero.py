
# Este programa simulara el funcionamiento de un cajero automatico

# Creamos el usuario en el banco con esta clase
class UsuarioBanco():
    def __init__(self,nombre,num_cuenta,pin):
        self.nombre = nombre
        self.num_cuenta = num_cuenta
        self.pin = pin

# Este objeto seria el usuario, ya con sus parametros
Usuario = UsuarioBanco("Martin",49503212,8388)
saldo_usuario = 0

# Funcion que permite calcular el saldo del usuario
def ConsultarSaldo():
    print("-" * 40)
    print("Consultar saldo")
    IngresarCuenta = int(input("Ingrese su numero de cuenta: "))
    IngresePing = int(input("Ingrese su pin: "))
    if IngresarCuenta == Usuario.num_cuenta and IngresePing == Usuario.pin:
        print(f"Su saldo actual es de ${saldo_usuario}")
    else:
        print("ERROR: Datos incorrectos")

# Funcion que permite cargar saldo
def CargarSaldo():
    global saldo_usuario
    print("-" * 40)
    print("Cargar saldo a una cuenta")
    IngresarCuenta = int(input("Ingrese su numero de cuenta: "))
    if IngresarCuenta == Usuario.num_cuenta:
        SaldoACargar = int(input("¿Cuanto desea cargar? "))
        saldo_usuario = saldo_usuario + SaldoACargar
        print(f"Cargaste correctamente {SaldoACargar} en la cuenta: {Usuario.num_cuenta}")
    else:
        print("ERROR: Datos incorrectos")

# Funcion para retirar dinero de su cuenta 
def RetirarSaldo():
    global saldo_usuario
    print("-" * 40)
    print("Retirar saldo de una cuenta")
    IngresarCuenta = int(input("Ingrese su numero de cuenta: "))
    IngresePing = int(input("Ingrese su pin: "))
    if IngresarCuenta == Usuario.num_cuenta and IngresePing == Usuario.pin:
        RetirarSaldo = int(input("¿Cuanto desea retirar? "))
        if RetirarSaldo > saldo_usuario:
            print("No tiene saldo suficiente")         
        elif RetirarSaldo < saldo_usuario:
            saldo_usuario = saldo_usuario - RetirarSaldo
            print("Saldo retirado con exito")
    else:
        print("Datos incorrectos")
            

# Esta funcion contiene el menu
def Menu():
    while True:
        try:
            print("-" * 40)
            print("Cajero automatico AzuraCash")
            print("1 - Consultar saldo")
            print("2 - Cargar dinero a la cuenta")
            print("3 - Retirar efectivo")
            print("4 - Terminar")
            opcion_menu = int(input("¿Que movimiento deseeas hacer? "))
            if opcion_menu == 4:
                print("Cerrando sesion")
                break
            elif opcion_menu == 1:
                ConsultarSaldo()
            elif opcion_menu == 2:
                CargarSaldo()
            elif opcion_menu == 3:
                RetirarSaldo()

        except ValueError:
            print("Debe ingresar una opcion correcta")

Menu()
