capacidade = float(input("Capacidade do tanque (L): "))
consumo = float(input("Consumo do carro (km/L): "))
preco = float(input("Preço da gasolina: "))

distancia = capacidade * consumo
valor = capacidade * preco

print("Distância total com o tanque cheio:", distancia, "km")
print("Valor para encher o tanque: R$", valor)
