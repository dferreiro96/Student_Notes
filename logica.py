def calcular_promedio(datos_de_estudiantes):
    suma = 0
    for est in datos_de_estudiantes:
        suma += est["Nota"]
    return suma / len(datos_de_estudiantes)


def calcular_max(datos_de_estudiantes):
    mayor = float('-inf')
    for est in datos_de_estudiantes:
        mayor = max(mayor, est["Nota"])
    return mayor       
    



def calcular_min(datos_de_estudiantes):
    menor = float('inf')
    for est in datos_de_estudiantes:
       menor = min(menor, est["Nota"])
    return menor
           


def mostrar_resultados(datos_de_estudiantes):
    for i, estudiante in enumerate(datos_de_estudiantes, start=1):
        print(f"{i}. {estudiante["Nombre"]}: {estudiante["Nota"]}")
