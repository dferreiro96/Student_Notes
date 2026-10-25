
import csv


def exportar_datos(datos_de_estudiantes):
    try:
        with open("datos_de_los_estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Nota"])
            escritor.writeheader()
            escritor.writerows(datos_de_estudiantes)
            print("\nSe han exportado los datos de los estudiantes correctamente")
    except PermissionError:
        print("\nNo se ha podido exportar los datos. Otra aplicación está usando el archivo.")
    except Exception as e:  
        print(f"\nOcurrió un error inesperado: {e}")
        