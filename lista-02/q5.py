x1, y1 = map(int, input("Coordenadas do primeiro drone: ").split())

x2, y2 = map(int, input("Coordenadas do segundo drone: ").split())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"A distancia dos drones é de {distancia:.2f}")