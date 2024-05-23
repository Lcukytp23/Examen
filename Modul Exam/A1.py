import os

def crear_archivo_ejemplo(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(datos)

ruta_archivos = 'c:/Users/manue/OneDrive/Documentos/Estructura de datos/Unidad 5/Modul Exam' 


datos_A1 = [
    "Orquesta1, 5, 2023-01-01, 2023-01-02, 2023-01-03, 2023-01-04, 2023-01-05\n",
    "Orquesta3, 3, 2023-02-01, 2023-02-02, 2023-02-03\n"
]

crear_archivo_ejemplo(os.path.join(ruta_archivos, 'A1.txt'), datos_A1)
print("Archivo A1.txt creado con el siguiente contenido:")
print("Nombre del cantante u orquesta, Número de presentaciones, Fechas de las presentaciones")
for linea in datos_A1:
    print(linea.strip())

print("\nArchivo A1.txt creado exitosamente.")
