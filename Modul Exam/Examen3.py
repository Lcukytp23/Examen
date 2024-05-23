import json

empleados = [
    {"nombre": "Ana", "estado_civil": "Soltera", "antiguedad": 5, "categoria": "A", "sueldo": 3000},
    {"nombre": "Carlos", "estado_civil": "Casado", "antiguedad": 10, "categoria": "B", "sueldo": 3500},
    {"nombre": "Beatriz", "estado_civil": "Soltera", "antiguedad": 3, "categoria": "A", "sueldo": 3200},
    {"nombre": "David", "estado_civil": "Casado", "antiguedad": 15, "categoria": "C", "sueldo": 4000},
    {"nombre": "Elena", "estado_civil": "Soltera", "antiguedad": 1, "categoria": "A", "sueldo": 3100},
    {"nombre": "Fernando", "estado_civil": "Casado", "antiguedad": 8, "categoria": "B", "sueldo": 3300},
    {"nombre": "Gabriela", "estado_civil": "Soltera", "antiguedad": 2, "categoria": "A", "sueldo": 3050},
    {"nombre": "Hugo", "estado_civil": "Casado", "antiguedad": 7, "categoria": "B", "sueldo": 3450},
    {"nombre": "Isabel", "estado_civil": "Soltera", "antiguedad": 4, "categoria": "A", "sueldo": 3250},
    {"nombre": "Juan", "estado_civil": "Casado", "antiguedad": 9, "categoria": "C", "sueldo": 3600},
    {"nombre": "Karla", "estado_civil": "Soltera", "antiguedad": 6, "categoria": "A", "sueldo": 3150},
    {"nombre": "Luis", "estado_civil": "Casado", "antiguedad": 12, "categoria": "B", "sueldo": 3700},
    {"nombre": "Maria", "estado_civil": "Soltera", "antiguedad": 5, "categoria": "A", "sueldo": 3000},
    {"nombre": "Nicolas", "estado_civil": "Casado", "antiguedad": 10, "categoria": "B", "sueldo": 3500},
    {"nombre": "Oscar", "estado_civil": "Soltera", "antiguedad": 3, "categoria": "A", "sueldo": 3200},
    {"nombre": "Patricia", "estado_civil": "Casado", "antiguedad": 15, "categoria": "C", "sueldo": 4000},
    {"nombre": "Quentin", "estado_civil": "Soltera", "antiguedad": 1, "categoria": "A", "sueldo": 3100},
    {"nombre": "Raquel", "estado_civil": "Casado", "antiguedad": 8, "categoria": "B", "sueldo": 3300},
    {"nombre": "Samuel", "estado_civil": "Soltera", "antiguedad": 2, "categoria": "A", "sueldo": 3050},
    {"nombre": "Teresa", "estado_civil": "Casado", "antiguedad": 7, "categoria": "B", "sueldo": 3450}
]

with open('empleados.txt', 'w') as f:
    for empleado in empleados:
        f.write(json.dumps(empleado) + '\n')


def leer_empleados(file_path):
    empleados = []
    with open(file_path, 'r') as file:
        for line in file:
            empleados.append(json.loads(line.strip()))
    return empleados

def escribir_empleados(file_path, empleados):
    with open(file_path, 'w') as file:
        for empleado in empleados:
            file.write(json.dumps(empleado) + '\n')

def merge_sort(empleados):
    if len(empleados) <= 1:
        return empleados
    mid = len(empleados) // 2
    left_half = merge_sort(empleados[:mid])
    right_half = merge_sort(empleados[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0]['nombre'] < right[0]['nombre']:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

def distribuir(empleados, temp1, temp2):
    switch = True
    for i in range(0, len(empleados), 2):
        if switch:
            temp1.extend(empleados[i:i+2])
        else:
            temp2.extend(empleados[i:i+2])
        switch = not switch

def fusionar(temp1, temp2):
    resultado = []
    while temp1 and temp2:
        if temp1[0]['nombre'] < temp2[0]['nombre']:
            resultado.append(temp1.pop(0))
        else:
            resultado.append(temp2.pop(0))
    resultado.extend(temp1 or temp2)
    return resultado

def mezcla_equilibrada(empleados):
    if len(empleados) <= 1:
        return empleados
    temp1, temp2 = [], []
    distribuir(empleados, temp1, temp2)
    temp1 = sorted(temp1, key=lambda x: x['nombre'])
    temp2 = sorted(temp2, key=lambda x: x['nombre'])
    return fusionar(temp1, temp2)

empleados = leer_empleados('empleados.txt')
empleados_ordenados_md = merge_sort(empleados)
escribir_empleados('empleados_ordenados_mezcla_directa.txt', empleados_ordenados_md)

empleados = leer_empleados('empleados.txt')
empleados_ordenados_me = mezcla_equilibrada(empleados)
escribir_empleados('empleados_ordenados_mezcla_equilibrada.txt', empleados_ordenados_me)

def imprimir_empleados(empleados, metodo):
    print(f"Empleados ordenados por {metodo}:")
    for empleado in empleados:
        print(empleado)
    print("\n")

print("Resultado de la mezcla directa:")
empleados_ordenados_md = leer_empleados('empleados_ordenados_mezcla_directa.txt')
imprimir_empleados(empleados_ordenados_md, "Mezcla Directa")

print("Resultado de la mezcla equilibrada:")
empleados_ordenados_me = leer_empleados('empleados_ordenados_mezcla_equilibrada.txt')
imprimir_empleados(empleados_ordenados_me, "Mezcla Equilibrada")