edad = int(input("ingrese la edad de la persona que desea ingresar al parque de diversiones: "))
if edad >= 1 and edad <= 4:
    print("la persona puede ingresar gratis ")
elif edad > 4 and edad <= 8:
    print("\nEl tickete para esta persona tiene un costo de:")
    print("\n2 Dolares")
    print("8600 en pesos colombianos")
elif edad > 9 and edad <= 16:
    print("\nEl tickete para esta persona es de:")
    print("\n5 Dolares")
    print("21978 pesos colombianos")
elif edad > 17 and edad <= 35:
    print("\nEl tickete para esta persona es de:")
    print("\n6 Dolares")
    print("26334 pesos colombianos")
elif edad > 36:
    print("\nEl tickete para esta persona es de:")
    print("\n10 Dolares")
    print("43956 pesos colombianos")