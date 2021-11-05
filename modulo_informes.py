# Este módulo se utilizará para mostrar los informes pedidos en pantalla
from cola import Cola
from funciones_utiles import lista2cola
import modulo_pacientes as mp



def informe_pacientes_mayores_a_edad_determinada(lista_pacientes):
    """
    Imprime un informe con las fichas de los pacientes que tengan una edad mayor a la ingresada por el teclado.
    """
    print("Se mostraran los pacientes que sean mayores a la edad ingresada")
    edad_de_partida = mp.validar_edad()
    print()
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][3] > edad_de_partida:
            print("Nombre Completo:", "%14s" %lista_pacientes[i][0].center(14), "%21s" %lista_pacientes[i][1].center(21) , "|", "DNI:",
                  "%8s" %lista_pacientes[i][2], "|", "Edad:", "%2s" %lista_pacientes[i][3], "|", "Turno - ", end="")
            if len(lista_pacientes[i]) == 7:
                print("Día:", "%2s" %lista_pacientes[i][5], "Mes:", "%2s" %lista_pacientes[i][6],"Hora:", "%2s" %lista_pacientes[i][4], "Hs.")
            else:
                print("Este Paciente no tiene turno asociado")
    print()

def informe_segun_nombre_o_edad(lista_pacientes):
    """
    Imprime informes con las fichas de los pacientes a partir de listas que se ordenan según nombre (ordenadas a partir del código ASCII)
    o edad (de menor a mayor)
    """
    while True:
        try:
            opcion = input("Ingrese según el orden por el cual recibir el informe (nombre o edad): ")
            break
        except ValueError:
            print("Ingreso un valor erróneo. Intente nuevamente")
        except:
            print("ERROR INESPERADO. Intente nuevamente")
    print()
    if opcion.casefold() == "nombre":
        lista_pacientes.sort(key = lambda x: x[0])
        for i in range(len(lista_pacientes)):
            print("Nombre Completo:", "%14s" %lista_pacientes[i][0].center(14), "%21s" %lista_pacientes[i][1].center(21) , "|", "DNI:",
                  "%8s" %lista_pacientes[i][2], "|", "Edad:", "%2s" %lista_pacientes[i][3], "|", "Turno - ", end="")
            if len(lista_pacientes[i]) == 7:
                print("Día:", "%2s" %lista_pacientes[i][5], "Mes:", "%2s" %lista_pacientes[i][6],"Hora:", "%2s" %lista_pacientes[i][4], "Hs.")
            else:
                print("Este Paciente no tiene turno asociado")
    elif opcion.casefold() == "edad":
        lista_pacientes.sort(key = lambda x: x[3])
        for i in range(len(lista_pacientes)):
            print("Nombre Completo:", "%14s" %lista_pacientes[i][0].center(14), "%21s" %lista_pacientes[i][1].center(21) , "|", "DNI:",
                  "%8s" %lista_pacientes[i][2], "|", "Edad:", "%2s" %lista_pacientes[i][3], "|", "Turno - ", end="")
            if len(lista_pacientes[i]) == 7:
                print("Día:", "%2s" %lista_pacientes[i][5], "Mes:", "%2s" %lista_pacientes[i][6],"Hora:", "%2s" %lista_pacientes[i][4], "Hs.")
            else:
                print("Este Paciente no tiene turno asociado")
    else:
        print("Error, ha ingresado una opción no existente.")
    print()
        

# Las funciones de abajo se relacionan con el informe de los turnos por mes y dia
def informe_turnos(cola_turnos):
    """
    Recibe la cola de los turnos y verifica si esta vacía, si no lo esta imprime la ficha del paciente, desacola y luego llama a la misma función
    para que se produzca la recursividad
    """
    
    if cola_turnos.esta_vacia():
        print("Los turnos asociados a su día y mes ingresados se encuentran arriba. Si no hay nada, significa que no existen turnos",
                "asociados a los mismos")
        print()
    else:
#         print(cola_turnos.primero())
        print("Nombre Completo:", "%14s" %cola_turnos.primero()[0].center(14), "%21s" %cola_turnos.primero()[1].center(21),
              "|", "DNI:", "%8s" %cola_turnos.primero()[2], "|", "Edad:", "%2s" %cola_turnos.primero()[3], "|", "Turno -",
              "Día:", "%2s" %cola_turnos.primero()[5], "Mes", "%2s" %cola_turnos.primero()[6], "Hora:", "%2s" %cola_turnos.primero()[4], "Hs.")
        cola_turnos.desacolar()
        informe_turnos(cola_turnos)

def cola_turnos_segun_hora(lista_turnos):
    """Ordena una lista de turnos según la hora y luego crea una cola acolando cada elemento de la lista ordenada"""
    
    lista_turnos.sort(key = lambda x: x[4])
    
    cola_turnos = lista2cola(lista_turnos)
    return cola_turnos

def crear_lista_turnos_segun_mes_dia(lista_pacientes):
    """Crea una lista según un mes y un dia ingresados por teclado a partir de la lista de los pacientes."""
    lista_turnos = []
    while True:
        try:
            mes = int(input("Ingrese el número del mes del cual quiera visualizar los turnos: "))
            dia = int(input("Ingrese el día, del mes ingresado, del cual quiera visualizar los turnos: "))
            break
        except ValueError:
            print("Error, datos inválidos. Intente Nuevamente")
        except:
            print("Error inesperado. Intente nuevamente")
    while mes > 12 or mes < 1:
        print()
        mes = int(input("Error, ha ingresado un mes inválido. Intente nuevamente: "))
    while dia < 1 or dia > 31:
        print()
        dia = int(input("Error, ha ingresado un día inválido. Intente nuevamente: "))
    print()
#   lista_turnos = [lista_pacientes[i] for i in range(len(lista_pacientes)) if mes == lista_pacientes[i][6] and dia == lista_pacientes[i][5]]
    for i in range(len(lista_pacientes)):
        if len(lista_pacientes[i]) == 7:
            if mes == lista_pacientes[i][6] and dia == lista_pacientes[i][5]:
                lista_turnos.append(lista_pacientes[i])
    
    return lista_turnos

def informes(lista_pacientes):
    print()
    print("-"*100)
    print("Elija una de las siguientes opciones.")
    print("-"*100, "1. Informe de Turnos por mes y día".center(100), "2. Informe de pacientes ordenados por nombre o edad".center(100),
          "3. Informe de pacientes mayores a una determinada edad".center(100), "-"*100, sep="\n")
    while True:
        try:
            seleccion = int(input("Ingrese por teclado el número asociado a la opción a la que usted quiera ingresar: "))
            break
        except ValueError:
            print("Ha ingresado un valor no númerico. Vuelva a intentarlo")
        except:
            print("Error inesperado. Vuelva a intentarlo...")
    if seleccion == 1:
        turnos = crear_lista_turnos_segun_mes_dia(lista_pacientes)
        turnos_cola = cola_turnos_segun_hora(turnos)
        informe_turnos(turnos_cola)
    elif seleccion == 2:
        informe_segun_nombre_o_edad(lista_pacientes)
    elif seleccion == 3:
        informe_pacientes_mayores_a_edad_determinada(lista_pacientes)
    else:
        print("Error, la opcion no ingresada no existe.")
    print()
    
    
def main():
    """Nombre, Apellido, DNI, Edad, Hora, Dia,  """
    lista = [
                ["Matias","Caliz",49506033,19,10,2,11],
                ["Luciano", "Capasso", 49506043,30,11,4,11],
                ["EL","rute",43724831,70,13,6,11],
                ["Maximo","Fain",44208676,19,10,4,11],
                ["Jorge", "Fernandez",22350897,54,12,2,11]
            ]
    
#     turnos = crear_lista_turnos_segun_mes_dia(lista)
#     turnos_cola = cola_turnos_segun_hora(turnos)
#     informe_turnos(turnos_cola)
#     informe_segun_nombre_o_edad(lista)
    informe_pacientes_mayores_a_edad_determinada(lista)
    
if __name__ == "__main__":
    main()