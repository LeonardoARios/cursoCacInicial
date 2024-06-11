#Desafío 1: Diccionario de datos personales
#Desarrollar un diccionario que contenga datos no reales de una persona. El
#diccionario debe tener los tipos de datos vistos (enteros, ﬂotantes, cadenas,
#lógicos, listas). Luego mostrar esos datos en formato de tarjeta, utilizando
#métodos de cadenas y f-strings para concatenar datos, convertir a mayúsculas y
#inúsculas, etc.

#Creo mi diccionario
datosPersonales = {"nombre":"laura graciela","edad":32,"estatura":1.64,"jubilada":False,"hijos":["geronimo","german","theodoro"]}
print(datosPersonales)
print(type(datosPersonales))
print(len(datosPersonales))

#Para acceder al diccionario
print("="*70)
for item,valor in datosPersonales.items():
    if item == "hijos":
        continue
    print(f'{item.capitalize()}: {valor} \n'.capitalize())
for sons, value in datosPersonales.items():
    if sons == "hijos":
        print("Hijos: ", end="")
        for v in valor: 
            print(f'{v};'.capitalize(), end=" ")
print()
print("="*70)
