from logica import calcular_max, calcular_min, calcular_promedio, mostrar_resultados
from menu import menu
from utilidades import escoer_opcion
from validaciones import pedir_estudiante, pedir_notas


def main():
    print("""\nEjercicio 5. Notas de estudiantes con funciones.
- Pedir nombres y notas.
- Mostrar promedio, mejor, peor nota.
- Funciones: pedir_estudiante, calcular_promedio, mostrar_resultados.""")
    datos_de_estudiantes = []
    while True:
        menu()
        opcion = escoer_opcion("\nTeclee una opción: ", ["1", "2", "3", "4", "5"])
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
                mostrar_resultados(
                    datos_de_estudiantes
                )
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
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")

                elif ordenar_por == "2":
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nota"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")

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

        else:
            break

    print("\nHa salido satisfactoriamente.\n")


if __name__ == "__main__":
    main()

