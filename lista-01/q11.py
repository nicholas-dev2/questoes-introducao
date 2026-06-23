consumo = float(input("Valor total da conta: "))
pessoas = int(input("Pessoas na mesa: "))

consumo += consumo * 0.1

divisao = consumo / pessoas

print("Cada amigo deverá pagar R$", divisao)
