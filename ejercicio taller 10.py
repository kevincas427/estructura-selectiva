name = input("ingrese su nombre: ")
edad= int(input("ingrese su edad: "))
sexo = input("ingrese su sexo : Masculino(M), femenino (F):")
sexo1  = sexo.upper()
estadoCivil = input("ingrese su estadoCivil: ")
estadoCivil1 = estadoCivil.upper()
if edad < 18:
    print("Edad no requerida para las votaciones, lo siento no puedes votar")
elif edad >= 18 and estadoCivil1 == "CASADA" and sexo1 == "F":
    print(f"{name} votas en la Mesa #1")
elif edad >= 18 and estadoCivil1 == "SOLTERA" and sexo1 == "F":
    print(f"{name} votas en la MESA #2")
elif edad >= 18 and estadoCivil1 == "SEPARADA" and sexo1 == "F":
    print(f"{name} votas en la MESA #3")
elif edad >= 18 and estadoCivil1 == "OTRO" and sexo1 == "F":
    print(f"{name} votas en la MESA #4")
elif edad >= 18 and estadoCivil1 == "CASADO" and sexo1 =="M":
    print(f"{name} votas en la MESA #5")
elif edad >= 18 and estadoCivil1 == "SOLTERO" and sexo1 =="M":
    print(f"{name} votas en la MESA #6")
elif edad >= 18 and estadoCivil1 == "SEPARADO" and sexo1 =="M":
    print(f"{name} votas en la MESA #7")
elif edad >= 18 and estadoCivil1 == "OTRO" and sexo1 =="M":
    print(f"{name} votas en la MESA #8")






