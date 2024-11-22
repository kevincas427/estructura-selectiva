partido1 = int(input("ingrese los goles anotados por el jugador el primer partido: "))
partido2 = int(input("ingrese los goles anotados por el jugador el segundo partido: "))
partido3 = int(input("ingrese los goles anotados por el jugador el tercer partido: "))
partido4 = int(input("ingrese los goles anotados por el jugador el tercer partido: "))
goles=partido1+partido2+partido3+partido4
if goles > 10:
    goles = goles/ 4
    print(f"\nEl promedio de goles anotados por el jugador es: {goles}")
else:
    print("No se puede determinar el promedio, falta de talento viejo :(")
