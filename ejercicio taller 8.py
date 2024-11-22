A = float(input("ingrese el valor del lado A: "))
B = float(input("ingrese el valor del lado B: "))
C = float(input("ingrese el valor del lado C: "))
if A<(B+C) and B<(A+C) and C<(A+B):
    if A == B and B == C:
        print(f"El triangulo formado con estas medidas es un Equilatero")
    else:
        print(f"El triangulo formado con estas medidas es un Escaleno")
else:
    print("Las medidas insertadas con coinciden con las de un triangulo ")
