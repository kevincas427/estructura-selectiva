A = float(input("ingrese el valor del lado A: "))
B = float(input("ingrese el valor del lado B: "))
C = float(input("ingrese el valor del lado C: "))
suma1 = 0
suma2 = 0
suma3 = 0
if A + B > C:
    suma1 = B + C
else:
    print("Los datos ingresados no pertenecen a los de un triangulo")
    if B + C > A:
        suma2 = A + C
    else:
        print("Los datos ingresados no pertenecen a los de un triangulo")
        if A + C > B:
            print("La medida de los ingresados SI pertenecen a las de un triangulo")
        else:
            print("Los datos ingresados no pertenecen a los de un triangulo")
            print("\ncon los datos ingresados no podemos calcular el tipo de triangulo.")
            if A == B and B == C:
                print("Las medidas pertenecen a un triangulo equilatero")
            elif A != B and B != C:
                print("Las medidas ingresadas pertenenes a las de un triangulo Isosceles ")