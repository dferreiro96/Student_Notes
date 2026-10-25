from exportar_datos import exportar_datos
from logica import calcular_max, calcular_min, calcular_promedio, mostrar_resultados
from menu import menu
from persistencia import cargar_datos, guardar_datos
from utilidades import escoer_opcion
from validaciones import pedir_estudiante, pedir_notas


def main():
    print("\nNotas de estudiantes con funciones")
    
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
                print(f"Se ha añadido el estudiante {estudiante}.")
                notas = pedir_notas(f"\nIntroduzca la nota de {estudiante}: ")
                print(f"Se ha añadido la nota de {estudiante} correctamente.")
                datos_de_estudiantes.append({"Nombre": estudiante, "Nota": notas})
                print(f"\nSe han guardado los datos de {estudiante} correctamente\n")
                guardar_datos(datos_de_estudiantes)
                

        elif opcion == "2":
            if not datos_de_estudiantes:
                print("\nNo se ha introducido ningún dato.")
            else:
                print()
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
                    print("\nOrdenando por nombre:")
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nombre"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")

                elif ordenar_por == "2":
                    print("\nOrdenando por notas ascendentes:")
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nota"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")
                        
                    print("\nOrdenando por notas descendentes:")
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nota"], reverse=True)
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
                    f"\nEl promedio es {promedio:.2f}. La mejor y peor notas fueron {maximo} y {minimo} respectivamente."
                )
        elif opcion == "5":
            if datos_de_estudiantes:
                exportar_datos(datos_de_estudiantes)  
            else:
                print("\nNo hay datos para exportar")          

        else:
            break

    print("\nHa salido satisfactoriamente.\n")


if __name__ == "__main__":
    main()

