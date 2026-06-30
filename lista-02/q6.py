numero = int(input("Digite os números: "))

centenas = numero // 100
dezenas = (numero // 10) % 10
unidades = numero % 10

print(f"{unidades}{dezenas}{centenas}")