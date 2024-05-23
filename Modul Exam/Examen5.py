
alumnos_desordenados = []
alumnos_ordenados = []


def buscar_alumno_desordenado(nombre):
    for alumno in alumnos_desordenados:
        if alumno['nombre'] == nombre:
            return alumno['promedio'], alumno['materias_aprobadas']
    return None


def buscar_alumno_ordenado(nombre):
    inicio = 0
    fin = len(alumnos_ordenados) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if alumnos_ordenados[medio]['nombre'] == nombre:
            return alumnos_ordenados[medio]['promedio'], alumnos_ordenados[medio]['materias_aprobadas']
        elif alumnos_ordenados[medio]['nombre'] < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ").strip()
    promedio = float(input("Ingrese el promedio del alumno: ").strip())
    materias_aprobadas = int(input("Ingrese el número de materias aprobadas: ").strip())

    nuevo_alumno = {'nombre': nombre, 'promedio': promedio, 'materias_aprobadas': materias_aprobadas}
    alumnos_desordenados.append(nuevo_alumno)
    alumnos_ordenados.append(nuevo_alumno)
    alumnos_ordenados.sort(key=lambda x: x['nombre'])
    print("Alumno agregado exitosamente.")

def interactuar():
    while True:
        print("\nOpciones:")
        print("1. Agregar un nuevo alumno")
        print("2. Buscar un alumno")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            tipo_arreglo = input("Ingrese el tipo de arreglo (desordenado/ordenado): ").strip().lower()
            if tipo_arreglo not in ["desordenado", "ordenado"]:
                print("El alumno no esta registrado.")
                continue

            nombre_buscar = input("Ingrese el nombre del alumno: ").strip()
            if tipo_arreglo == "desordenado":
                resultado = buscar_alumno_desordenado(nombre_buscar)
            elif tipo_arreglo == "ordenado":
                resultado = buscar_alumno_ordenado(nombre_buscar)

            if resultado:
                promedio, materias_aprobadas = resultado
                print(f"Alumno: {nombre_buscar}, Promedio: {promedio}, Materias Aprobadas: {materias_aprobadas}")
            else:
                print("Alumno no encontrado.")
        elif opcion == '3':
            print("Terminando el programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

interactuar()
