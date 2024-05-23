def seleccion_directa_nombre(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]['Nombre del alumno'] < arr[min_idx]['Nombre del alumno']:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

alumnos = [
    {"Nombre del alumno": "Juan", "Matrícula": "123", "Número de materias aprobadas": 5, "Promedio": 8.5},
    {"Nombre del alumno": "María", "Matrícula": "456", "Número de materias aprobadas": 4, "Promedio": 7.8},
    {"Nombre del alumno": "Pedro", "Matrícula": "789", "Número de materias aprobadas": 6, "Promedio": 9.2},
    {"Nombre del alumno": "Ana", "Matrícula": "101", "Número de materias aprobadas": 7, "Promedio": 8.9},
    {"Nombre del alumno": "Luis", "Matrícula": "202", "Número de materias aprobadas": 3, "Promedio": 6.5},
    {"Nombre del alumno": "Sofía", "Matrícula": "303", "Número de materias aprobadas": 5, "Promedio": 7.2},
    {"Nombre del alumno": "Carlos", "Matrícula": "404", "Número de materias aprobadas": 8, "Promedio": 9.6},
    {"Nombre del alumno": "Elena", "Matrícula": "505", "Número de materias aprobadas": 4, "Promedio": 7.1},
    {"Nombre del alumno": "Pablo", "Matrícula": "606", "Número de materias aprobadas": 6, "Promedio": 8.3},
    {"Nombre del alumno": "Laura", "Matrícula": "707", "Número de materias aprobadas": 5, "Promedio": 8.0},
    {"Nombre del alumno": "Diego", "Matrícula": "808", "Número de materias aprobadas": 7, "Promedio": 8.7},
    {"Nombre del alumno": "Fernanda", "Matrícula": "909", "Número de materias aprobadas": 4, "Promedio": 7.4},
    {"Nombre del alumno": "Roberto", "Matrícula": "010", "Número de materias aprobadas": 6, "Promedio": 8.1},
    {"Nombre del alumno": "Carmen", "Matrícula": "111", "Número de materias aprobadas": 5, "Promedio": 8.2},
    {"Nombre del alumno": "Alejandro", "Matrícula": "212", "Número de materias aprobadas": 8, "Promedio": 9.5},
    {"Nombre del alumno": "Isabel", "Matrícula": "313", "Número de materias aprobadas": 3, "Promedio": 6.8},
    {"Nombre del alumno": "Jorge", "Matrícula": "414", "Número de materias aprobadas": 7, "Promedio": 8.8},
    {"Nombre del alumno": "Valeria", "Matrícula": "515", "Número de materias aprobadas": 4, "Promedio": 7.5},
    {"Nombre del alumno": "Ricardo", "Matrícula": "616", "Número de materias aprobadas": 6, "Promedio": 8.4},
    {"Nombre del alumno": "Lucía", "Matrícula": "717", "Número de materias aprobadas": 5, "Promedio": 7.9}
]

seleccion_directa_nombre(alumnos)

print("Alumnos ordenados por nombre:")
for alumno in alumnos:
    print(alumno)


def quicksort_num_materias(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['Número de materias aprobadas']
    left = [x for x in arr if x['Número de materias aprobadas'] < pivot]
    middle = [x for x in arr if x['Número de materias aprobadas'] == pivot]
    right = [x for x in arr if x['Número de materias aprobadas'] > pivot]
    return quicksort_num_materias(left) + middle + quicksort_num_materias(right)

alumnos = [
    {"Nombre del alumno": "Juan", "Matrícula": "123", "Número de materias aprobadas": 5, "Promedio": 8.5},
    {"Nombre del alumno": "María", "Matrícula": "456", "Número de materias aprobadas": 4, "Promedio": 7.8},
    {"Nombre del alumno": "Pedro", "Matrícula": "789", "Número de materias aprobadas": 6, "Promedio": 9.2},
    {"Nombre del alumno": "Ana", "Matrícula": "101", "Número de materias aprobadas": 7, "Promedio": 8.9},
    {"Nombre del alumno": "Luis", "Matrícula": "202", "Número de materias aprobadas": 3, "Promedio": 6.5},
    {"Nombre del alumno": "Sofía", "Matrícula": "303", "Número de materias aprobadas": 5, "Promedio": 7.2},
    {"Nombre del alumno": "Carlos", "Matrícula": "404", "Número de materias aprobadas": 8, "Promedio": 9.6},
    {"Nombre del alumno": "Elena", "Matrícula": "505", "Número de materias aprobadas": 4, "Promedio": 7.1},
    {"Nombre del alumno": "Pablo", "Matrícula": "606", "Número de materias aprobadas": 6, "Promedio": 8.3},
    {"Nombre del alumno": "Laura", "Matrícula": "707", "Número de materias aprobadas": 5, "Promedio": 8.0},
    {"Nombre del alumno": "Diego", "Matrícula": "808", "Número de materias aprobadas": 7, "Promedio": 8.7},
    {"Nombre del alumno": "Fernanda", "Matrícula": "909", "Número de materias aprobadas": 4, "Promedio": 7.4},
    {"Nombre del alumno": "Roberto", "Matrícula": "010", "Número de materias aprobadas": 6, "Promedio": 8.1},
    {"Nombre del alumno": "Carmen", "Matrícula": "111", "Número de materias aprobadas": 5, "Promedio": 8.2},
    {"Nombre del alumno": "Alejandro", "Matrícula": "212", "Número de materias aprobadas": 8, "Promedio": 9.5},
    {"Nombre del alumno": "Isabel", "Matrícula": "313", "Número de materias aprobadas": 3, "Promedio": 6.8},
    {"Nombre del alumno": "Jorge", "Matrícula": "414", "Número de materias aprobadas": 7, "Promedio": 8.8},
    {"Nombre del alumno": "Valeria", "Matrícula": "515", "Número de materias aprobadas": 4, "Promedio": 7.5},
    {"Nombre del alumno": "Ricardo", "Matrícula": "616", "Número de materias aprobadas": 6, "Promedio": 8.4},
    {"Nombre del alumno": "Lucía", "Matrícula": "717", "Número de materias aprobadas": 5, "Promedio": 7.9}
]

alumnos_ordenados = quicksort_num_materias(alumnos)

print("Alumnos ordenados por número de materias aprobadas:")
for alumno in alumnos_ordenados:
    print(alumno)
