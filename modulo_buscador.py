# Módulo utilizado para desarrollar la parte del buscador del programa.
import funciones_utiles as fu
import modulo_pacientes as mp
import modulo_turnos as mt



def buscador_dni(lista):
    """
    Buscar en una lista de todos los pacientes según un DNI dado, a partir del siguiente formato
    NombrePaciente;ApellidoPaciente;DNI;edad;HoraTurno;DiaTurno;MesTurno
    """
    dni_ingresado = mp.validar_dni()
    existe_dni = False
    print()
    for i in range(len(lista)):
        if dni_ingresado == lista[i][2]:
            existe_dni = True
            print("Nombre Completo:", "%14s" %lista[i][0].center(14), "%21s" %lista[i][1].center(21) , "|", "DNI:", "%8s" %lista[i][2], "|",
                  "Edad:", "%2s" %lista[i][3], "|", "Turno - ", end="")
            if len(lista[i]) == 7:
                print("Dia:", "%2s" %lista[i][5], "Mes:", "%2s" %lista[i][6], "Hora:", "%2s" %lista[i][4], "Hs.")
            else:
                print("Este Paciente no tiene turno asociado")
                
    if not existe_dni:
         print(f"No se ha encontrado ningún paciente con el DNI {dni_ingresado}")
    print()
         

def buscador_edad(lista):
    """
    Buscar en una lista de todos los pacientes según una edad dada, a partir del siguiente formato
    NombrePaciente;DNI;edad;HoraTurno;DiaTurno;MesTurno
    """
    existe_edad = False
    edad_solicitada = mp.validar_edad()
    print()
    for i in range(len(lista)):
        if edad_solicitada == lista[i][3]:
            existe_edad = True
            print("Nombre Completo:", "%14s" %lista[i][0].center(14), "%21s" %lista[i][1].center(21) , "|", "DNI:", "%8s" %lista[i][2], "|",
                  "Edad:", "%2s" %lista[i][3], "|", "Turno - ", end="")
            if len(lista[i]) == 7:
                print("Dia:", "%2s" %lista[i][5], "Mes:", "%2s" %lista[i][6], "Hora:", "%2s" %lista[i][4], "Hs.")
            else:
                print("Este Paciente no tiene turno asociado")
            
    if not existe_edad:
        print(f"No se ha encontrado ningún paciente con la edad {edad_solicitada}")
    print()

def buscador(pacientes):
    while True:
        try:
            seleccion = input("Ingrese según lo que usted quiera buscar (DNI o EDAD): ").casefold()
            break
        except ValueError:
            print("Error ha ingresado un texto inválido. Intente nuevamente.")
        except:
            print("Error inesperado. Intente nuevamente.")
    if seleccion == 'edad':
        buscador_edad(pacientes)
    elif seleccion == 'dni':
        buscador_dni(pacientes)
    else:
        print()
        print("Error, el valor ingresado no corresponde a ninguna opción, volviendo al menu principal...")

def main():
    lista_pacientes = fu.txt2lista("pacientes.txt")
    buscador_dni(lista_pacientes)
    buscador_edad(lista_pacientes)

if __name__ == "__main__":
    main()