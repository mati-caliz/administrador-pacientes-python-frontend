# En este archivo se desarrollara el programa principal.
import modulo_login as login
import modulo_turnos as turnos
import modulo_pacientes as mp
import modulo_buscador as buscador
import funciones_utiles as fu
import modulo_informes as informes
import time

def gui_menu():
    print("-"*100)
    print("Bienvenido/a al menú principal del programa, elija una de las siguientes opciones para continuar.".center(100))
    print("-"*100)
    print("Alta Paciente".center(100), "Baja Paciente".center(100), "Modificar paciente".center(100), "Alta Turno".center(100),
                      "Baja Turno".center(100), "Modificar Turno".center(100), "Buscador".center(100), "Informes".center(100), sep="\n")
    print("-"*100 + "\n")

def menu(valor,pacientes):
    if valor == "alta paciente":
        pacientes = mp.alta_paciente(pacientes)
    elif valor == "baja paciente":
        pacientes = mp.baja_paciente(pacientes)
    elif valor == "modificar paciente":
        pacientes = mp.modificar_paciente(pacientes)
    elif valor == "alta turno":
        pacientes = turnos.alta_turno(pacientes)
    elif valor == "baja turno":
        pacientes = turnos.baja_turno(pacientes)
    elif valor == "modificar turno":
        pacientes = turnos.modificar_turno(pacientes)
    elif valor == "buscador":
        buscador.buscador(pacientes)
    elif valor == "informes":
        informes.informes(pacientes)
    else:
        print("\n" + "--- Lo que ha ingresado no corresponde a ninguna opción, intentelo nuevamente. ---" + "\n")

#LISTA DE USUARIOS: 
#Usuario: admin ||| Contraseña: 1234
#Usuario: alfonsina1996 ||| Contraseña: alfo1996

def main():
    hay_cuenta = login.iniciar_sesion()
    pacientes = fu.txt2lista('pacientes.txt')
    if hay_cuenta == True:
        gui_menu()
        seleccion = input("Escriba con el teclado la opción a la que quiera acceder (O presione Enter para cerrar el programa): ").casefold()
        while seleccion != "":
            menu(seleccion,pacientes)
            print()
            print("Regresando al menu principal...")
            time.sleep(2)
            gui_menu()
            seleccion = input("Escriba con el teclado la opción a la que quiera acceder (O presione Enter para cerrar el programa): ").casefold()
        fu.limpiar_txt('pacientes.txt')
        fu.lista2txt(pacientes, 'pacientes.txt')
   
if __name__ == "__main__":
    main()


