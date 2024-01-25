import pyfiglet
import pandas as pd

acsiiTitle = pyfiglet.figlet_format("Py Manager",font='univers', width=100)
print(acsiiTitle)
print("\nCreated with <3 by Gerardo Suarez. \nTotally free for all \n")

print("Primero que nada, escribe la ruta de tu archivo: \n")

path = input()

print("\n Tu archivo es: " + path + "\n")
print("Archivo valido! \n")

def agregar_registro(path, nuevo_registro):
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        # El archivo está vacío, se crearán las columnas
        df = pd.DataFrame(columns=nuevo_registro.keys())

    nuevo_df = pd.DataFrame([nuevo_registro])
    df = pd.concat([df, nuevo_df], ignore_index=True)
    df.to_csv(path, index=False)

def eliminar_registro(path, columna, valor):
    df = pd.read_csv(path)
    df = df[df[columna] != valor]
    df.to_csv(path, index=False)

def cambiar_registro(path, columna, valor_a_cambiar, nuevos_datos):
    df = pd.read_csv(path)
    df.loc[df[columna] == valor_a_cambiar, :] = nuevos_datos
    df.to_csv(path, index=False)

def realizar_consulta(path, columna, criterio):
    df = pd.read_csv(path)
    resultado = df[df[columna].apply(criterio)]
    return resultado.values.tolist()

archivo_csv = path
try:
    df = pd.read_csv(archivo_csv, nrows=1)
    columnas = df.columns.tolist()
except pd.errors.EmptyDataError:
    columnas = []

while True:
    print("\nSelecciona una operación:")
    print("1. Agregar registro")
    print("2. Eliminar registro")
    print("3. Cambiar registro")
    print("4. Realizar consulta")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion == '1':
        nuevo_registro = {}
        for columna in columnas:
            nuevo_valor = input(f"Ingrese el valor para la columna {columna}: ")
            nuevo_registro[columna] = nuevo_valor
        agregar_registro(archivo_csv, nuevo_registro, columnas)
        print("Registro agregado exitosamente.")
    elif opcion == '2':
        try:
            df = pd.read_csv(archivo_csv, nrows=1)
            nuevas_columnas = df.columns.tolist()
        except pd.errors.EmptyDataError:
            nuevas_columnas = []
        
        columna_a_eliminar = input("Ingrese el nombre de la columna a eliminar: ")
        valor_a_eliminar = input("Ingrese el valor a eliminar: ")
        eliminar_registro(archivo_csv, columna_a_eliminar, valor_a_eliminar)
        print("Registro eliminado exitosamente.")
    elif opcion == '3':
        try:
            df = pd.read_csv(archivo_csv, nrows=1)
            nuevas_columnas = df.columns.tolist()
        except pd.errors.EmptyDataError:
            nuevas_columnas = []

        columna_a_cambiar = input("Ingrese el nombre de la columna a cambiar: ")
        valor_a_cambiar = input("Ingrese el valor a cambiar: ")
        nuevos_datos = {}
        for columna in nuevas_columnas:
            nuevo_valor = input(f"Ingrese el nuevo valor para la columna {columna}: ")
            nuevos_datos[columna] = nuevo_valor
        cambiar_registro(archivo_csv, columna_a_cambiar, valor_a_cambiar, nuevos_datos)
        print("Registro cambiado exitosamente.")
    elif opcion == '4':
        try:
            df = pd.read_csv(archivo_csv, nrows=1)
            nuevas_columnas = df.columns.tolist()
        except pd.errors.EmptyDataError:
            nuevas_columnas = []
        
        columna_a_consultar = input("Ingrese el nombre de la columna para la consulta: ")
        valor_a_consultar = input("Ingrese el valor a consultar: ")
        def criterio_personalizado(valor):
            return valor == valor_a_consultar
        resultados = realizar_consulta(archivo_csv, columna_a_consultar, criterio_personalizado)
        print("Resultados de la consulta:", resultados)
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")