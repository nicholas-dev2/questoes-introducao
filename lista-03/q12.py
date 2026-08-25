import math

metros = int(input("Metros para a pintura: "))
latas = math.ceil(metros / 3)
preço = latas * 80

if latas >= 3:
    print(f"Latas necessárias: {latas}, Valor gasto: {preço * 0.9}")

else:
    print(f"Latas necessárias: {latas}, Valor gasto: {preço:.0f}")