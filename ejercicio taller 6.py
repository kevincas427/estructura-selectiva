bonificacion = float(input("ingrese el valor de su bonificacion para hallar el producto a compara: "))
if bonificacion < 50000:
    print("su productoarecibir es una Camara WEB, felicitaciones")
elif bonificacion > 50000 and bonificacion <= 200000:
    print("El producto que puede comprar es un SubWoofer")
elif bonificacion > 200000 and bonificacion <= 500000:
    print("El producto que puede comprar es un Disco duro externo ")
elif bonificacion > 500000 and bonificacion <= 1000000:
    print("El producto que puede comprar es una Impresora Funcional")
elif bonificacion > 1000000:
    print("El producto que puede comprar es un¨royector")