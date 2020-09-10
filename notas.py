nt1 = int(input("Digita tu nota del 1er examen: "))
nt2 = int(input("Digita tu nota del 2do examen: "))
nt3 = int(input("Digita tu nota del 3er examen: "))
nt4 = int(input("Digita tu nota del examen final: "))

nf = (nt1 + nt2 + nt3 + nt4)/4

if nf >= 90 and nf <= 100:
    print("Su calificacion es A")
elif nf >= 80 and  nf <= 89:
    print("Su calificacion es b")
elif nf >= 70 and nf <= 79:
      print("Su calificacion es c")
elif nf <= 1 and nf <= 69:
      print("Su calificacion es F")