a = int(input("ingrese el valor para A: "))
b = int(input("ingrese el valor para B: "))
if a<b:
    print(a)
    print(b)
elif a>b:
    print(b)
    print(a)
else:
    print("los numeros son iguales no se pueden ordenar de menor a mayor")
    print(f"\nlos numeros ingresados: A:{a} , B:{b}")
    