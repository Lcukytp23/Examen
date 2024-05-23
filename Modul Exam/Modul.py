import subprocess
import os

ruta_base = r'C:\Users\manue\OneDrive\Documentos\Estructura de datos\Unidad 5\Modul Exam'

def ejecutar_Examen(Examen):
    try:
        subprocess.run(Examen, shell=True)
    except Exception as e:
        print(f"Error al ejecutar {Examen}: {e}")

def ejecutar_Examen_seleccionado():
    while True:
        print("Ejecutar Programa:")
        print("1. Examen1")
        print("2. Examen 2")
        print("3. Examen 3")
        print("4. Examen 4")
        print("5. Examen 5")
        print("6. Salir")

        opcion = input("Selecciona el programa que deseas ejecutar (1-5): ")

        if opcion == "6":
            break 
        if opcion in {"1", "2", "3", "4", "5"}:
            examen = os.path.join(ruta_base, f'Examen{opcion}.py')
            ejecutar_Examen(f"python \"{examen}\"")
        else:
            print("Opción no válida.")

ejecutar_Examen_seleccionado()



