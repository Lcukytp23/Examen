import os

def crear_archivo_ejemplo(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(datos)

ruta_archivos = 'c:/Users/manue/OneDrive/Documentos/Estructura de datos/Unidad 5/Modul Exam' 
datos_A3 = [
    "Orquesta1, 2, 2023-05-01, 2023-05-02\n",
    "Orquesta3, 1, 2023-06-01\n"
]


crear_archivo_ejemplo(os.path.join(ruta_archivos, 'A3.txt'), datos_A3)

print("Archivo A3.txt creado con el siguiente contenido:")
print("Nombre del cantante u orquesta, Número de presentaciones, Fechas de las presentaciones")
for linea in datos_A3:
    print(linea.strip())

print("\nArchivo A3.txt creado exitosamente.")
