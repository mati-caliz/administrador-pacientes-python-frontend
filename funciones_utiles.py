# Funciones que nos van a servir para todos los módulos
from cola import Cola

def lista2txt(lista, archivo):
    """Transforma una matriz (lista de listas) con elementos de cualquier tipo a un archivo.
    Cada renglón del archivo debe tener la forma: 'elemento;elemento;elemento;...\n'.
    La matriz tiene que ser de la forma [['elemento','elemento',...],['elemento','elemento',...],...].
    IMPORTANTE: La funcion no elimina lo que ya contiene el archivo, si se desea es necesario usar limpiar_txt().
    """
    try:
        txt = open(archivo, 'a')
    except IOError:
        print("Error. No se pudo leer el archivo.")
    except:
        print("Error inesperado...")
    for elemento in range(len(lista)):
        pregrabado = ';'.join([str(subelemento) for subelemento in lista[elemento]])
        txt.write(pregrabado + '\n')
    txt.close()

def int_lista(lista):
    """Transforma los strings de elementos de una matriz (o lista de listas) en enteros int() siempre que se pueda."""
    for elemento in range(len(lista)):
        for subelemento in range(len(lista[elemento])):
            try:    
                lista[elemento][subelemento] = int(lista[elemento][subelemento])
            except ValueError:
                pass
    return lista

def txt2lista(archivo):
    """Abre un archivo que se ingresa como parámetro y guarda en una matriz (lista de listas) con todos los renglones 
    como distintos elementos dentro de una gran lista.
    La matriz tiene la forma [['elemento','elemento',...],['elemento','elemento',...],...]
    """
    try:       
        txt = open(archivo, 'r')
    except IOError:
        print("Error. No se pudo leer el archivo.")
    except:
        print("Error inesperado...")
    lista = [linea.replace('\n', '').title().split(';') for linea in txt]
    txt.close()
    lista = int_lista(lista)
    return lista

def limpiar_txt(archivo):
    """Elimina todos los elementos de un archivo .txt que se ingresa como parametro."""
    try:
        txt = open(archivo,'w')
    except IOError:
        print("Error, no se pudo escribir el archivo.")
    except:
        print("Error inesperado...")
    txt.close()

def validar_entero(valor):
    """Valida si un valor ingresado es entero retorna True, o string retorna False."""
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def buscar_elemento_en_lista(lista,elemento):
    """Busca un elemento que se ingresa como parametro en una matriz (lista de listas) que se ingresa como parametro.
    y devuelve la posicion en la que se encuentra el elemento, o -1 si no se encuentra el elemento en la matriz.
    """
    posicion = None
    for item in range(len(lista)):
        if elemento in lista[item]:
            posicion = item
    return posicion

def eliminar_elemento_en_lista(lista,elemento_ingresado):
    """Busca un elemento que se ingresa como parametro en una matriz (lista de listas) que se ingresa como parametro.
    y si el elemento se encuentra en la lista lo elimina.
    """
    validez = False
    for elemento in range(len(lista)-1,-1,-1): #Se recorre la lista desde el final hasta el principio.
        if elemento_ingresado in lista[elemento]:
            lista.pop(elemento)
            validez = True
    return lista,validez

def lista2cola(lista):
    cola = Cola()
    for i in range(len(lista)):
        cola.acolar(lista[i])
    return cola

def main():
    pass

if __name__ == "__main__":
    main()
