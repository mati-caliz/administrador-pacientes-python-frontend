# Módulo que será utilizado para desarrollar el login del programa.

def verificar_cuenta(existe_usuario, existe_contraseña, nombre_usuario):
    """
    Verifica con los booleanos retornados de las funciones 'ingresar_contraseña' y 'ingresar_usuario' si
    la cuenta existe. Si es asi retorna un booleano asociado a la existencia de la cuenta. Además toma como parametro
    el nombre de usuario ingresado para imprimirlo si la cuenta ingresada es correcta.
    """
    
    print()
    existe_cuenta = False
    if existe_usuario and existe_contraseña:
        print(f"|| Bienvenido/a {nombre_usuario} || \n")
        existe_cuenta = True
    else:
        print("| - Error, alguno o ambos datos ingresados no es válido - | \n")
    return existe_cuenta

def ingresar_contraseña(lista_cuentas):
    """ Pide contraseña y la compara con el diccionario, devuelve un boolean asociado a la existencia de la contraseña"""
    
    existe_contraseña = False
    contraseña_usuario = input("Ingrese su contraseña para continuar: ")
    for i in range(len(lista_cuentas)):
        if contraseña_usuario == lista_cuentas[i].get("contraseña"):
            existe_contraseña = True
    return existe_contraseña

def ingresar_usuario(lista_cuentas):
    """
    Pide nombre de usuario y lo compara con el diccionario, devuelve un boolean asociado a la existencia del usuario y
    el nombre de usuario ingresado.
    """
    existe_usuario = False
    nombre_usuario = input("Ingrese su nombre de usuario para iniciar sesión: ")
    for i in range(len(lista_cuentas)):
        if nombre_usuario == lista_cuentas[i].get("usuario"):
            existe_usuario = True
    return existe_usuario, nombre_usuario

def iniciar_sesion():
    hay_cuenta = False
    cuentas = [{"usuario": "admin", "contraseña": "1234"},{"usuario": "alfonsina1996", "contraseña": "alfo1996"}]
    intentos = 1
    while intentos < 4 and hay_cuenta == False:
        print("-"*100)
        print(f" --- Intento número {intentos}, el limite de intentos es 3 --- \n")
        hay_usuario, n_usuario = ingresar_usuario(cuentas)
        hay_contraseña = ingresar_contraseña(cuentas)
        hay_cuenta = verificar_cuenta(hay_usuario, hay_contraseña, n_usuario)
        intentos += 1
    if intentos == 4:
        print("-"*100)
        print("|| - Ha llegado al limite de intentos permitido, se cerrara el programa... - ||".center(100))
        print("-"*100)
    return hay_cuenta


def main():
    cuentas = [{"usuario": "admin", "contraseña": "1234"},{"usuario": "alfonsina1996", "contraseña": "alfo1996"}]
    hay_usuario, n_usuario = ingresar_usuario(cuentas)
    hay_contraseña = ingresar_contraseña(cuentas)
    hay_cuenta = verificar_cuenta(hay_usuario, hay_contraseña, n_usuario)
    
if __name__ == "__main__":
    main()