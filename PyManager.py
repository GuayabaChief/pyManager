import pyfiglet
import pandas as pd

acsiiTitle = pyfiglet.figlet_format("Py Manager",font='univers')
print(acsiiTitle)
print("\n Created with <3 by Gerardo Suarez. \nTotally free for all \n")

print("Primero que nada, escribe la ruta de tu archivo: \n")
path = input()

file = pd.read_csv(path)

print("\n Tu archivo es: " + path)

