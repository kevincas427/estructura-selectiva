print(" programa para resolver eciaciones")
print("\nla ecuacion en este caso es P=(R-2)**")
R=int(input("ingrese un valor para R: "))
P = 0
if R != 2:
    P=(R-2)**3
    print(f"El resultado de la ecuacion es: {P}")
else:
    P=1
    print(f"El resultado de la ecuacion es: {P}")
