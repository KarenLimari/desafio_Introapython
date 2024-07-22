#𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
#Donde:
#P: Precio de Suscripción
#U: Número de Usuarios
#GT: Gastos Totales

#Si pensamos, que ingrese los siguientes datos, precio de suscripción: 5000, número de usuarios:100, gastos totales: 250000
#variables
import math
import cmath

precio_suscripcion = float(input("ingrese el precio de la suscripcion solo con numeros y en CLP:\n>"))
numero_usuarios = float(input("ingrese el numero de usuarios con numero entero: \n>"))
gastos_totales = float(input("ingrese los gastos totales solo con numeros y en CLP: \n>"))
utilidades = ((precio_suscripcion * numero_usuarios) - gastos_totales)
utilidades = math.ceil(utilidades)

print (f"Las utilidades son {utilidades} CLP")