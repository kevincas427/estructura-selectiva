nota = float(input("Igrese el valor de su nota: "))
if nota >= 4.6 and nota <= 5.0:
    print("Su nota es EXELENTE, felicitaciones")
elif nota >= 3.6 and nota < 4.6:
    print("su nota es BUENA, ero puedes mejorar ")
elif nota >= 3.0 and nota < 3.6:
    print("su nota es aceptable, pero hay que trabajar mas")
elif nota >= 2.0 and nota <3.0 :
    print("su nota es insuficiente")
elif nota < 2.0 :
    print("su nota es deficiente")
    