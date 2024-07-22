#variables
import math
import cmath

precio_suscripcion = float(input("ingrese el precio de la suscripcion solo con numeros y en CLP:\n>"))
numero_usuarios = float(input("ingrese el numero de usuarios con numero entero: \n>"))
gastos_totales = float(input("ingrese los gastos totales solo con numeros y en CLP: \n>"))
uanterior = float(input("ingrese las utilidades del año anterior :\n>"))
uactual = ((precio_suscripcion * numero_usuarios) - gastos_totales)
uactual = math.ceil(uactual)

print (f"Las utilidades actuales son {uactual} CLP")
print(f"Las utilidades anterires son {uanterior} CLP")

razon = (uactual / uanterior)
razon = ("%.2f" % razon)

print (f"La razon entre las utilidades actuales y las utilidades anteriores es {razon}")