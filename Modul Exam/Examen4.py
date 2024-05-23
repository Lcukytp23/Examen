import os

def leer_archivo(nombre_archivo):
    registros = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(', ')
                nombre = partes[0].strip()
                num_presentaciones = int(partes[1].strip())
                fechas = [fecha.strip() for fecha in partes[2:]]
                registros.append((nombre, num_presentaciones, fechas))
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
        exit(1)
    registros.sort(key=lambda x: x[0])
    return registros

def escribir_archivo(nombre_archivo, registros):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Nombre del cantante u orquesta           | Número de presentaciones | Fechas de las presentaciones\n")
        archivo.write("-" * 90 + "\n")
        for registro in registros:
            nombre = registro[0]
            num_presentaciones = str(registro[1])
            fechas = ", ".join(registro[2])
            linea = f"{nombre.ljust(40)} | {num_presentaciones.center(25)} | {fechas}\n"
            archivo.write(linea)

ruta_archivos = 'c:/Users/manue/OneDrive/Documentos/Estructura de datos/Unidad 5/Modul Exam' 

registros_A1 = leer_archivo(os.path.join(ruta_archivos, 'A1.txt'))
registros_A2 = leer_archivo(os.path.join(ruta_archivos, 'A2.txt'))
registros_A3 = leer_archivo(os.path.join(ruta_archivos, 'A3.txt'))

registros_totales = registros_A1 + registros_A2 + registros_A3

registros_totales.sort(key=lambda x: x[0])

escribir_archivo(os.path.join(ruta_archivos, 'RECITALES.txt'), registros_totales)

print("El archivo RECITALES.txt ha sido creado con éxito.")
