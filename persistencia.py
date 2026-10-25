import json


def guardar_datos(datos_de_estudiantes):
    
    with open("datos_de_estudiantes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos_de_estudiantes, archivo, indent= 4, ensure_ascii= False)
        
        
def cargar_datos():
    try:
        with open("datos_de_estudiantes.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                print("\nSe han recuperado los datos correctamente")
                return datos
    except FileNotFoundError:
        print("\nNo se encontraron datos guardados. Se creará una nueva hoja de cálculo.")
        return []
    except json.JSONDecodeError:
        print("\nLos datos estaban corruptos. Se creará una nueva hoja de cálculo.")
        return []