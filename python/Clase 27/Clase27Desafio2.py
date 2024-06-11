#Desafío 2: ABM de datos personales
#Teniendo en cuenta el diccionario del desafío anterior, desarrollar un programa
#que permita, a través de la carga de datos por teclado las siguientes acciones:
#● Cargar un nuevo dato personal al diccionario.
#● Modiﬁcar una clave y su correspondiente valor, ingresados por teclado.
#● Eliminar una clave
#Para realizar estas acciones realice un menú en el programa principal o utilice
#funciones para gestionar estas operaciones. Recuerde colocar el diccionario
#como parámetro en la declaración y como argumento en la llamada.

def modificaKey(dicc):
    print("Los items que puede cambiar son: ")
    print()
    for clave,valor in dicc.items():
        print(f'{clave}: {valor}')

    respo = input("Que items quiere modificar? ".lower())
    for clave, valor in dicc.items():
        if clave == respo:
            print(f'{clave} coincide con el items que quiere buscar')
            valor = input("Porque valor lo quiere modificar?  ")
            dicc[respo]= valor
            print(dicc[respo])
        else:
            continue
    print(dicc)
    print("termino el bucle")

def agregarKey(dicc):

    clave = input("Que item quiere agregar?: ")
    valor = input("Que valor quiere agregar al mismo?: ")

    dicc[clave]=valor

    print(dicc)

def eliminarKey(dicc):
    print("Los items que puede elimiar son: ")
    print("="*70)
    for clave,valor in dicc.items():
        print(f'{clave}: {valor}')
    print("="*70)
    clave = input("Que items desea eliminar?:  ")
    dicc.pop(clave)
    print()
    print("Los items quedaron de esta manera")
    print("="*70)
    for clave,valor in dicc.items():
        print(f'{clave}: {valor}')
    
#PROGRAMA PRINCIPAL
#Creo mi diccionario
datosPersonales = {"nombre":"laura graciela","edad":32,"estatura":1.64,"jubilada":False,"hijos":["geronimo","german","theodoro"]}
#Se ejecutan las funciones
#Modificar items
modificaKey(datosPersonales)
#Agregar items
agregarKey(datosPersonales)
#Eliminar items
eliminarKey(datosPersonales)
