def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x['ciudad'] < pivot['ciudad']]
    middle = [x for x in arr if x['ciudad'] == pivot['ciudad']]
    right = [x for x in arr if x['ciudad'] > pivot['ciudad']]
    
    middle.sort(key=lambda x: x['nombre'])
    
    return quicksort(left) + middle + quicksort(right)

hoteles = [
    {'nombre': 'Paradisus', 'ciudad': 'Cancun', 'estrellas': 4, 'cuartos': 150},
    {'nombre': 'Safi Royal', 'ciudad': 'Monterey', 'estrellas': 5, 'cuartos': 250},
    {'nombre': 'Mar y tierra', 'ciudad': 'Veracruz', 'estrellas': 4, 'cuartos': 175},
    {'nombre': 'Acuario', 'ciudad': 'Veracruz', 'estrellas': 4, 'cuartos': 200},
    {'nombre': 'Krystal', 'ciudad': 'Cancun', 'estrellas': 5, 'cuartos': 100},
    {'nombre': 'Country', 'ciudad': 'Guadalajara', 'estrellas': 5, 'cuartos': 125},
]

hoteles_ordenados = quicksort(hoteles)
for hotel in hoteles_ordenados:
    print(hotel)
