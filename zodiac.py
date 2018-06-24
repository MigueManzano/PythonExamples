import os
from datetime import date

password = input("Escibe la contraseña\n ")
loop = 'y'
artists =['\nAntoine Griezman', 'Messi', 'Pikachu', 'Kamisama', 'Peña bb']

if password == 'miguel':
    while loop == 'y' or loop == 'Y':
        Year = int(input("año de cumpleaños: " ))
        Month = input("mes de cumpleaños: " ).lower()
        Day = int(input("dia de cumpleaños: " ))
        Date_of_Birth = (str(Day) + "/" + Month + "/" + str(Year))
        d = date.today()
        y = d.year
        os.system("cls")
        age = y - Year
        print('Tu cumpleaños es el: ' + Date_of_Birth)
        print ('Este año tendras ' + str(age) + ' años')

        if ((Month == 'december' and Day >= 22) or (Month == 'january' and Day<= 19)):
            print("\nCapricorn")
            for name in artists:
                print(name)

        elif ((Month == 'january' and Day >= 20) or (Month == 'february' and Day<= 17)):
            print("\nAquarium")
            for name in artists:
                print(name)

        elif ((Month == 'february' and Day >= 18) or (Month == 'march' and Day<= 19)):
            print("\nPices")
            for name in artists:
                print(name)

        elif ((Month == 'march' and Day >= 20) or (Month == 'april' and Day<= 19)):
            print("\nAries")
            for name in artists:
                print(name)

        elif ((Month == 'april' and Day >= 20) or (Month == 'may' and Day<= 20)):
            print("\nTaurus")
            for name in artists:
                print(name)

        elif ((Month == 'may' and Day >= 21) or (Month == 'june' and Day<= 20)):
            print("\nGemini")
            for name in artists:
                print(name)

        elif ((Month == 'june' and Day >= 21) or (Month == 'july' and Day<= 22)):
            print("\nCancer")
            for name in artists:
                print(name)

        elif ((Month == 'july' and Day >= 23) or (Month == 'august' and Day<= 22)):
            print("\nLeo")
            for name in artists:
                print(name)

        elif ((Month == 'august' and Day >= 23) or (Month == 'september' and Day<= 22)):
            print("\nVirgo")
            for name in artists:
                print(name)

        elif ((Month == 'september' and Day >= 23) or (Month == 'october' and Day<= 22)):
            print("\nLibra")
            for name in artists:
                print(name)

        elif ((Month == 'october' and Day >= 23) or (Month == 'november' and Day<= 21)):
            print("\nScorpio")
            for name in artists:
                print(name)

        elif ((Month == 'november' and Day >= 22) or (Month == 'december' and Day<= 21)):
            print("\nSagittarius as:\n")
            for name in artists:
                print(name)

        loop = input('¿Quieres probar de nuevo?\n')
        os.system("cls")

    else:
        print ('Adios! :D')

else:
    print ('Perdón, contraseña incorrecta')