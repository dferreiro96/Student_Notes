import csv
import json


def guardar_datos(datos_de_estudiantes):

    with open("datos_de_estudiantes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_de_estudiantes, archivo, indent=4, ensure_ascii=False)


def cargar_datos():
    try:
        with open("datos_de_estudiantes.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print("\nSe han recuperado los datos correctamente")
            return datos
    except FileNotFoundError:
        print(
            "\nNo se encontraron datos guardados. Se creará una nueva hoja de cálculo."
        )
        return []
    except json.JSONDecodeError:
        print("\nLos datos estaban corruptos. Se creará una nueva hoja de cálculo.")
        return []


def exportar_datos(datos_de_estudiantes):
    try:
        with open(
            "datos_de_los_estudiantes.csv", "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Nota"])
            escritor.writeheader()
            escritor.writerows(datos_de_estudiantes)
            print("\nSe han exportado los datos de los estudiantes correctamente")
    except PermissionError:
        print(
            "\nNo se ha podido exportar los datos. Otra aplicación está usando el archivo."
        )
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")


def pedir_estudiante(mensaje):
    estudiante = input(mensaje).title().strip()
    return estudiante


def pedir_notas(mensaje):
    while True:
        try:
            notas = float(input(mensaje))
            if notas < 0 or notas > 100:
                print("Introduzca un valor válido de notas.")
                continue
            return notas
        except ValueError:
            print("Introduzca un valor válido de notas.")


def calcular_promedio(datos_de_estudiantes):
    suma = 0
    for est in datos_de_estudiantes:
        suma += est["Nota"]
    return suma / len(datos_de_estudiantes)


def calcular_max(datos_de_estudiantes):
    mayor = float("-inf")
    for est in datos_de_estudiantes:
        mayor = max(mayor, est["Nota"])
    return mayor


def calcular_min(datos_de_estudiantes):
    menor = float("inf")
    for est in datos_de_estudiantes:
        menor = min(menor, est["Nota"])
    return menor


def mostrar_resultados(datos_de_estudiantes):
    for i, estudiante in enumerate(datos_de_estudiantes, start=1):
        print(f"{i}. {estudiante['Nombre']}: {estudiante['Nota']}")


def menu():
    print("\n____MENU____")
    print("1. Añadir datos de estudiante.")
    print("2. Mostrar relación de estudiantes con sus notas.")
    print("3. Ordenar y mostrar relación de estudiantes.")
    print("4. Calcular promedio, mejor y menor nota; mostrar.")
    print("5. Exportar datos a una hoja de cálculos.")
    print("6. Salir.")


def escoer_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion not in opciones:
            print("\nCaracter inálido")
            continue
        else:
            return opcion


def jugar():
    print("\nNotas de estudiantes con funciones.")
    datos_de_estudiantes = cargar_datos()
    while True:
        menu()
        opcion = escoer_opcion("\nTeclee una opción: ", ["1", "2", "3", "4", "5", "6"])
        if opcion == "1":
            estudiante = pedir_estudiante("\nIntroduzca el nombre del estudiante: ")
            if not estudiante.replace(" ", "").isalpha():
                print("\nEl nombre solo puede contener letras y espacios.")
                continue
            existe = False
            for tupla_clave_valor in datos_de_estudiantes:
                if tupla_clave_valor["Nombre"] == estudiante:
                    existe = True
                    break
            if existe:
                print("Ya el estudiante se encuentra registrado.")
                continue
            else:
                print(f"\nSe ha añadido el estudiante {estudiante}.")
                notas = pedir_notas(f"\nIntroduzca la nota de {estudiante}: ")
                datos_de_estudiantes.append({"Nombre": estudiante, "Nota": notas})
                print(f"\nSe ha añadido la nota de {estudiante} correctamente.")

        elif opcion == "2":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
            else:
                mostrar_resultados(datos_de_estudiantes)
        elif opcion == "3":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
                continue
            else:
                print("\n___Orden___")
                print("1. Nombre.")
                print("2. Notas")

                ordenar_por = escoer_opcion(
                    "\nCómo desea ordenar la muestra?: ", ["1", "2"]
                )
                if ordenar_por == "1":
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nombre"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes['Nombre']}: {estudiantes['Nota']}")

                elif ordenar_por == "2":
                    print("\nOrdenando por notas ascendentes:")
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nota"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes['Nombre']}: {estudiantes['Nota']}")

                    print("\nOrdenando por notas descendentes:")
                    ordenados = sorted(
                        datos_de_estudiantes, key=lambda x: x["Nota"], reverse=True
                    )
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes['Nombre']}: {estudiantes['Nota']}")

        elif opcion == "4":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
                continue
            else:
                promedio = calcular_promedio(datos_de_estudiantes)
                maximo = calcular_max(datos_de_estudiantes)
                minimo = calcular_min(datos_de_estudiantes)
                print(
                    f"El promedio es {promedio:.2f}. La mejor y peor notas son {maximo} y {minimo} respectivamente."
                )
        elif opcion == "5":
            exportar_datos(datos_de_estudiantes)

        else:
            break


def main():
    jugar()
    print("\nHa salido satisfactoriamente.\n")


if __name__ == "__main__":
    main()
