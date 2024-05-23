import os

def crear_archivo_ejemplo(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(datos)

ruta_archivos = 'c:/Users/manue/OneDrive/Documentos/Estructura de datos/Unidad 5/Modul Exam'
datos_A2 = [
    "Orquesta4, 2, 2023-03-01, 2023-03-02\n",
    "Orquesta2, 4, 2023-04-01, 2023-04-02, 2023-04-03, 2023-04-04\n"
]

crear_archivo_ejemplo(os.path.join(ruta_archivos, 'A2.txt'), datos_A2)

print("Archivo A2.txt creado con el siguiente contenido:")
print("Nombre del cantante u orquesta, Número de presentaciones, Fechas de las presentaciones")
for linea in datos_A2:
    print(linea.strip())

print("\nArchivo A2.txt creado exitosamente.")
