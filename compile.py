import random

numero = random.randint(0,100)

#parte 1
print("Introduzca el número a adivinar")

while True:
    numero = input("Introduzca un número entre 0 y 99: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
            break

#parte 2
print("intente adivinar el número")

while True: #bucle 1
    while True: #bucle 2
        intento = input("Introduzca un número entre 0 y 99: " )

        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break #bucle 2
    if intento < numero:
        print("Demaciado pequeño")
    elif intento > numero:
        print("Demaciado grande")
    else:
        print("ha ganado")
        break