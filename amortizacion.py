import math

print("\tAmortizacion mediante el sistema frances.\n")

mt = int(input("Cantidad del monto: "))
ct = int(input("Numero de cuotas a pagar: "))
ia = int(input("iteres anual: "))

cp = float(mt*(1 + ia) ** ct * 1 / (1 + ia)** ct - 1) 


print("La cuota mensual es: "+ str(cp))