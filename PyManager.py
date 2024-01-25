import pyfiglet
import pandas as pd

acsiiTitle = pyfiglet.figlet_format("Py Manager",font='univers', width=100)
print(acsiiTitle)
print("\nCreated with <3 by Gerardo Suarez. \nTotally free for all \n")

print("Primero que nada, escribe la ruta de tu archivo: \n")
path = input()

file = pd.read_csv(path)

print("\n Tu archivo es: " + path + "\n")
print("Archivo valido! \n")

while True:

    def case1():
        return
    def case2():
        return
    def case3():
        return
    def case4():
        return
        
    switch_dict = {
        1: case1,
        2: case2,
        3: case3,
        4: case4
    }

    numero = int(input("Introduce el número de la opcion que quieras realizar: \n1. Alta(Sube algo) \n2. Baja(Elimina) \n3. Cambios (Cambia algo) \n4. Consulta (Busca algo) \n5. Salir\n"))
    

    if numero == 5:
        print("Adios!")
        break
    else:
         print("a")
        
