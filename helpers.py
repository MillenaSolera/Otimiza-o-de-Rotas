import math

def calcular_distancia(coord1, coord2):

    coord1 = list(map(float, coord1.split(', ')))  
    coord2 = list(map(float, coord2.split(', ')))

    # Converter as coordenadas para radianos
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    
    # Fórmula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    raio_terra = 6371  # Raio médio da Terra em km
    distancia = raio_terra * c
    
    return distancia

def rotate_array_until_string(arr, target):
    while arr[0] != target:
        arr.append(arr.pop(0))  
    return arr

