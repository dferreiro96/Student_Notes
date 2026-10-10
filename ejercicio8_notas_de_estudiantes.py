"""Ejercicio 8: Notas de estudiantes. Pide nombres y notas hasta "salir". 
Al final, muestra:
Todos los estudiantes con su nota
El promedio
El mejor estudiante
El peor estudiantes

"""
dicc={}
nombre=""
mayor= 0
menor= 0
notas= 0
while nombre not in ("salir", "Salir", "S", "SALIR"):
    nombre=input("\nIntroduzca el nombre de un estudiante o la palabra 'salir' para salir del programa: \n") .capitalize() .strip()
    while nombre not in ("salir", "Salir", "S", "SALIR"):
        try:
            notas= float(input(f"Introduzca la nota de {nombre}: \n"))
                
        except ValueError:
            print("\nIntroduzca un valor de notas válido")
            continue
        break
    dicc[nombre]= notas
del dicc["Salir"]
if dicc!= {}:
    print("\nLa relación de los estudiantes con sus notas fueron: \n")
    for i, (nombre, notas) in enumerate (dicc.items(), start=1):
        print(f"{i}. {nombre}: {notas}")
        
    mayor = float('-inf')
    menor = float('inf')    
    for notas in dicc.values():
        if notas > mayor:
            mayor = notas
        if notas < menor:
            menor = notas
        

    print(f"\nLa mayor nota fue: {mayor}")
    print(f"La menor nota fue: {menor}")
else:
    print("\nNo se introdujo ningún dato. Adiós")
