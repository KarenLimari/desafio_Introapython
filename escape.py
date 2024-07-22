#Actividad 1 - Velocidad de escape
#1. Se solicita crear un script escape.py que permita calcular la velocidad de escape ingresando como datos de entradas el radio r y la constante g. Los datos de entrada deben ingresarse de manera interactiva utilizando la función input().(2,5 Puntos)
#2. El programa debe especificar claramente el formato en el que se deben entregar los datos de entrada con instrucciones apropiadas.(2,5 Puntos)
#Ejemplo:
#“Ingrese el radio en Kilómetros:”,
#“Ingrese la constante g: ”
#La respuesta del programa también debe mostrarse con un texto apropiado:
#Ejemplo:
#“La velocidad de Escape es 11174.6 [m/s]”
#Para verificar el correcto funcionamiento del programa, se puede verificar con los siguientes datos:g = 9.8 [m/s2] r = 6371 [Km], pero para que me de el resultado convierto el valor del radio de kilometros a metros =6371000 m, ya que el resultado está en m/S
#Se obtiene como resultado: Velocidad de Escape = 11174.6 [m/s]
#variables a utilizar
import math
import cmath
radio = float(input("Ingrese el radio en metros: \n>"))
constante_gravitacional = float(input ("Ingres la constante g: \n>"))
velocidad_escape =math.sqrt(2 * (radio * constante_gravitacional))
velocidad_escape = ("%.1f" % velocidad_escape)

print(f"La velocidad de escape es: {velocidad_escape} m/s")