valor = int(input("Insira o valor: "))

cem = valor // 100
valor = valor % 100

cinquenta = valor // 50
valor = valor % 50

vinte = valor // 20
valor = valor % 20

dez = valor // 10
valor = valor % 10

cinco = valor // 5
valor = valor % 5

dois = valor // 2
valor = valor % 2

um = valor

print(f"Notas de 100: {cem}")
print(f"Notas de 50: {cinquenta}")
print(f"Notas de 20: {vinte}")
print(f"Notas de 10: {dez}")
print(f"Notas de 5: {cinco}")
print(f"Notas de 2: {dois}")
print(f"Notas de 1: {um}")
