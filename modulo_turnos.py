# Modulo utilizado dar o alta de baja turnos.
import funciones_utiles as fu
from modulo_pacientes import validar_dni
from datetime import datetime

def validar_hora():
    """Valida los pacientes que ingresaron una hora no permitida. Las horas no permitidas son antes que las 10am y después de las 2pm."""
    while True:
        try:
            hora = int(input("Ingrese la hora del turno: "))
            while (hora < 10 or hora > 14):
                print("Advertencia, ha introducido una hora inválida. Las horas válidas son de 10am a 14pm.")
                hora = int(input("Vuelve a introducir la hora del turno: "))
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return hora

def validar_dia():
    """Valida los dias no permitidos. Los dias no permitidos son: 2,8,15,22. Y tambien validas las fechas invalidas."""
    while True:
        try:
            dia = int(input("Ingrese el dia del turno: "))
            while (dia == 2 or dia == 8 or dia == 15 or dia == 22 or dia < 1 or dia > 31):
                print("Advertencia, ha introducido un dia inválido o incorrecto. Los dias inválidos son 2,8,15,22.")
                dia = int(input("Vuelve a introducir el dia del turno: "))
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return dia
    
def validar_mes():
    """Valida los meses no permitidos."""
    while True:
        try:
            mes = int(input("Ingrese el mes del turno: "))
            while (mes < 1 or mes > 12):
                print("Advertencia, ha introducido un mes incorrecto.")
                mes = int(input("Vuelve a introducir el mes del turno: "))
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return mes
    
def eliminar_elemento_vacio():
    lista.remove()

def validar_fecha():
    """Valida las fechas inválidas que no existen. Corrobora si es válido mediante el módulo datetime."""
    while True:
        dia, mes, año = validar_dia(), validar_mes(), 2021
        fecha = f"{dia}-{mes}-{año}"
        try:
            datetime.strptime(fecha, '%d-%m-%Y')
            break
        except ValueError:
            print("Advertencia, ha introducido una fecha incorrecta.")
    return dia,mes

def validar_turno_asignado(pacientes, dni):
    """Valida que no se ingrese un turno un paciente que ya tiene asignado algun turno. Si tiene un turno retorna True, sino False."""
    validez = False
    paciente = fu.buscar_elemento_en_lista(pacientes, dni)
    if paciente != None:
        if len(pacientes[paciente]) == 7:
            validez = True
        elif len(pacientes[paciente]) == 4:
            validez = False
    return validez

def validar_turno_tomado_otro_paciente(pacientes,fecha):
    """Valida si algun otro paciente tiene un turno en la misma fecha (hora, dia, mes)."""
    hora_ingresada, dia_ingresado, mes_ingresado = fecha[:]
    asignado = False
    for paciente in range(len(pacientes)):
        dni = pacientes[paciente][2]
        #Verifica primero que tenga turno asignado.
        tiene_turno = validar_turno_asignado(pacientes, dni)
        if tiene_turno == True:
            #Luego verifica si coincide la fecha.
            hora_paciente,dia_paciente,mes_paciente = pacientes[paciente][4:]
            if hora_paciente == hora_ingresada and dia_paciente == dia_ingresado and mes_paciente == mes_ingresado:
                asignado = True
    return asignado

def buscar_hora(pacientes,dni):
    paciente = fu.buscar_elemento_en_lista(pacientes,dni)
    hora = pacientes[paciente][4]
    return hora

def buscar_dia_mes(pacientes,dni):
    paciente = fu.buscar_elemento_en_lista(pacientes,dni)
    dia,mes = pacientes[paciente][5:]
    return dia,mes

def eliminar_turno(pacientes,dni):
    """Busca en la lista de pacientes el dni que coincide (si lo hay) y elimina su turno (3 elemento en adelante)."""
    while True:
        try:
            posicion = fu.buscar_elemento_en_lista(pacientes,dni)
            if posicion != None:
                pacientes[posicion][4:] = []
            else:
                print("No se encuentra el paciente solicitado.")
            break
        except:
            print("Se ha producido un error inesperado, vuelve a intentar.")
    return pacientes

def alta_turno(pacientes):
    """Funcion semiprincipal que organiza el alta de turnos"""
    dni = validar_dni()
    turno_repetido = validar_turno_asignado(pacientes, dni)
    paciente = fu.buscar_elemento_en_lista(pacientes,dni)
    if turno_repetido == False:
        hora = validar_hora()
        dia, mes = validar_fecha()
        fecha = [hora,dia,mes]
        turno_tomado = validar_turno_tomado_otro_paciente(pacientes,fecha)
        if turno_tomado == False:
        #Se agrega al paciente ingresado la fecha del turno.
            pacientes[paciente].extend(fecha)
            print("Se registro el turno correctamente.")
        elif turno_tomado == True:
            print("Advertencia, la fecha del turno ya esta tomada")
    elif turno_repetido == True:
        print("Advertencia, ya tiene un turno asignado.")
    return pacientes

def baja_turno(pacientes):
    """Funcion semiprincipal que organiza la baja de turnos"""
    dni = validar_dni()
    turno_repetido = validar_turno_asignado(pacientes, dni)
    if turno_repetido == True:
        pacientes = eliminar_turno(pacientes, dni)
        print("Se dio de baja el turno correctamente.")
    elif turno_repetido == False:
        print("No tiene ningun turno asignado.")
    return pacientes

def modificar_turno(pacientes):
    """Funcion semiprincipal que organiza la modificacion de turnos"""
    dni = validar_dni()
    tiene_turno = validar_turno_asignado(pacientes, dni)
    paciente = fu.buscar_elemento_en_lista(pacientes,dni)
    if tiene_turno == True:
        hora = validar_hora()
        dia, mes = validar_fecha()
        fecha = [hora,dia,mes]
        turno_tomado = validar_turno_tomado_otro_paciente(pacientes,fecha)
        if turno_tomado == False:
        #Se agrega al paciente ingresado la fecha del turno.
            pacientes[paciente][4:] = fecha[:]
            print("se ha modificado el valor correctamente")
        elif turno_tomado == True:
            print("Advertencia, la fecha del turno ya esta tomada")
    elif tiene_turno == False:
        print("Advertencia, no tiene un turno asignado.")
    return pacientes

def __main__():
    #pacientes = fu.txt2lista('pacientes.txt')
    seleccion_turno = str(input("Desea dar de alta, baja, o modificar el turno (con ENTER termina): ")).casefold()
    while seleccion_turno != "":
        if seleccion_turno == "alta":
            pacientes = alta_turno(pacientes)
        elif seleccion_turno == "baja":
            pacientes = baja_turno(pacientes)
        elif seleccion_turno == "modificar":
            pacientes = modificar_turno(pacientes)
        seleccion_turno = str(input("Desea dar de alta, baja, o modificar el turno (con ENTER termina): ")).casefold()
        fu.limpiar_txt('pacientes.txt')
        fu.lista2txt(pacientes, 'pacientes.txt')

if __name__ == "__main__":
    __main__()