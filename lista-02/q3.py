valor_inicial = float(input("Capital (R$): "))
taxa = float(input("Taxa de juros (%): "))
tempo = int(input("Tempo do investimento (meses): "))

montante = valor_inicial * ((1 + (taxa/100)) ** tempo)

print(f"O valor final foi de R${montante:.2f}")