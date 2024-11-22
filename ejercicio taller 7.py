matematicas = float(input("ingrese el puntaje obtenido en el area dematematicas: "))
lenguaje = float(input("ingrese el puntaje obtenido en el area de lenguaje: "))
if matematicas > lenguaje:
    print(f"\nUsted obtuvo un puntaje mayor en matematicas con: {matematicas} y menor en lenguaje con: {lenguaje}")
elif matematicas < lenguaje:
    print(f"\nUsted obtuvo un puntaje mayor en lenguaje con: {lenguaje} y menor en matematicas con: {matematicas}")