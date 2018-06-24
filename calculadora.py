ciclo = 'y'

while ciclo == 'y':
    numero1 = float(input("Ingrese un valor numerico entero: "))
    numero2 = float(input("Ingrese un segundo valor numerico entero: "))
    opcion = input("""" Ingrese la opcion numerica
    1.- Sumar
    2.- Restar
    3.- Multiplicar
    4.- Dividir 
    5.- Modulo o residuo""")

    if opcion == 1:
        print('{} + {} = {}'.format(numero1, numero2, numero1+numero2,))
        ciclo = input('Desea hacer otra operacion nueva? y/n')

    elif opcion == 2:
        print('{} - {} = {}'.format(numero1, numero2, numero1 - numero2))
        ciclo = input('Desea hacer otra operacion nueva? y/n')

    elif opcion == 3:
        print('{} * {} = {}'.format(numero1, numero2, numero1 * numero2))
        ciclo = input('Desea hacer otra operacion nueva? y/n')

    elif opcion == 4:
        print('{} / {} = {}'.format(numero1, numero2, numero1 / numero2))
        ciclo = input('Desea hacer otra operacion nueva? y/n')

    elif opcion == 5:
        print('{} % {} = {}'.format(numero1, numero2, numero1 % numero2))
        ciclo = input('Desea hacer otra operacion nueva? y/n')

    else:
        print('No es una opcion valida.')





