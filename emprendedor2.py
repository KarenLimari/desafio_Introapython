#𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
#Donde:
#P: Precio de Suscripción
#U: Número de Usuarios
#GT: Gastos Totales

#Si pensamos, que ingrese los siguientes datos,para usuarios normales en el año 2022 fue:
#precio de suscripción normal: 5000, número de usuarios:100

#Y si tenemos los siguientes datos para los usuarios premium:
#precio de suscripcion premium: 10000, numero de usuarios: 100. Suponiendo que el gasto total aumenta a el doble: 500000


#variables


import math
import cmath

precio_suscripcion_normal = float(input("ingrese el precio de la suscripcion normal solo con numeros y en CLP:\n>"))
precio_suscripcion_premium = float(input("ingrese el precio de la suscripcion premium solo con numeros y en CLP:\n>"))
numero_usuarios_normales= float(input("ingrese el numero de usuarios normales con numero entero: \n>"))
numero_usuarios_premium= float(input("ingrese el numero de usuarios premium con numero entero: \n>"))
gastos_totales = float(input("ingrese los gastos totales solo con numeros y en CLP: \n>"))
utilidades = ((precio_suscripcion_normal * numero_usuarios_normales)+(precio_suscripcion_premium * numero_usuarios_premium) - gastos_totales)
utilidades = math.ceil(utilidades)

print (f"Las utilidades con el aumento del 50% de la suscripcion premium son {utilidades} CLP")