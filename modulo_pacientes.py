#Registra los pacientes y filtra según distintos parámetros.
import funciones_utiles as fu
from datetime import datetime

def validar_nombre(nombre_apellido):
    """Se ingresa el nombre y valida los pacientes que tienen nombres con más de 2 palabras."""
    while True:
        try:
            nombre = str(input(f"ingrese su {nombre_apellido} completo: ")).title()
            largo_nombre = len(nombre.split())
            while largo_nombre > 2:
                print("Advertencia, ha introducido un valor inválido.")
                nombre = str(input(f"vuelve a introducir su"+nombre_apellido+': '))
                largo_nombre = len(nombre.split())
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return nombre

def validar_edad():
    """Filtra los pacientes que tienen menos de 17 años y mas de 120 años."""
    while True:
        try:
            edad = int(input("ingrese su edad: "))
            while edad < 17 or edad > 120:
                print("Advertencia, ha introducido una edad inválida.")
                edad = int(input("vuelve a introducir su edad: "))
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return edad

def validar_dni():
    """Filtra los DNI ingresados menores que 1 millón y mayores que 70 millones."""
    while True:
        try:
            dni = int(input("Ingrese el DNI: "))
            while (dni < (10**6) or dni > (7*10**7)):
                print("Advertencia, ha introducido un DNI inválido.")
                dni = int(input("vuelve a introducir su DNI: "))
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return dni

def validar_dni_repetido(pacientes):
    """"Filtra los DNI ingresados si ya se encuentran repetidos"""
    dni = validar_dni()
    valor = fu.buscar_elemento_en_lista(pacientes,dni)
    while valor != None:
        print("El paciente ya se encuentra registrado. Vuelve a intentarlo.")
        dni = validar_dni()
        valor = fu.buscar_elemento_en_lista(pacientes,dni)

    return dni

def alta_paciente(pacientes):
    """Funcion semiprincipal que organiza el alta de pacientes"""
    dni = validar_dni_repetido(pacientes)
    nombre = validar_nombre('nombre')
    apellido = validar_nombre('apellido')
    edad = validar_edad()
    pacientes.append([nombre,apellido,dni,edad])
    print("Se ha registrado correctamente.")
    return pacientes

def baja_paciente(pacientes):
    """Funcion semiprincipal que organiza la baja de pacientes"""
    dni_ingresado = validar_dni()
    pacientes_eliminado,encontrado = fu.eliminar_elemento_en_lista(pacientes,dni_ingresado)
    if encontrado == True:
        print("Se dio de baja correctamente.")
    elif encontrado == False:
        print("No se encontro el paciente con el dni ingresado")
    return pacientes

def modificar_paciente(pacientes):
    """Funcion semiprincipal que organiza la modificacion de pacientes"""
    dni_ingresado = validar_dni()
    paciente = fu.buscar_elemento_en_lista(pacientes,dni_ingresado)
    if paciente == None:
        print("El DNI ingresado no coincide con ninguno en el sistema.")
    
    else:
        modificar = input("¿Desea modificar el nombre, apellido, dni, o edad?: ").casefold()
        if modificar == "nombre":
            nombre_ingresado = validar_nombre("nombre")
            pacientes[paciente][0] = nombre_ingresado
            print("Se ha modificado el valor correctamente")
        elif modificar == "apellido":
            apellido_ingresado = validar_nombre("apellido")
            pacientes[paciente][1] = apellido_ingresado
            print("Se ha modificado el valor correctamente")
        elif modificar == "dni":
            dni_existente = False
            dni_ingresado = validar_dni()
            for i in range(len(pacientes)):
                if dni_ingresado == pacientes[i][2]:
                    dni_existente = True
            if dni_existente:
                print("Error. El DNI ingresado ya existe.")
            else:
                pacientes[paciente][2] = dni_ingresado
                print("Se ha modificado el valor correctamente")
        elif modificar == "edad":
            edad_ingresada = validar_edad()
            pacientes[paciente][3] = edad_ingresada
            print("Se ha modificado el valor correctamente")
        elif modificar != "nombre" and modificar != "apellido" and modificar != "dni" and modificar != "edad":
            print("Ha ingresado un valor incorrecto, vuelve a intentarlo")
    return pacientes

def __main__():
    pacientes = fu.txt2lista('pacientes.txt')
    seleccion_paciente = str(input("Desea dar de alta, baja, o modificar (con ENTER termina): ")).casefold()
    while seleccion_paciente != '':
        if seleccion_paciente == "alta":
            pacientes = alta_paciente(pacientes)
        elif seleccion_paciente == "baja":
            pacientes = baja_paciente(pacientes)
        elif seleccion_paciente == "modificar":
            pacientes = modificar_paciente(pacientes)
        elif (seleccion_paciente != "alta" and seleccion_paciente != "baja" and seleccion_paciente != "modificar"):
            print("ha ingresado un valor incorrecto, vuelve a intentarlo")
        seleccion_paciente = str(input("Desea dar de alta, baja, o modificar (con ENTER termina): ")).casefold()
    fu.limpiar_txt('pacientes.txt')
    fu.lista2txt(pacientes, 'pacientes.txt')

if __name__ == "__main__":
    __main__()

