peso = int(input("Peso do açaí: "))

bruto = peso * 0.05

if peso > 500:
    valor = bruto * 0.85
    print(f"Você ganhou 15% de desconto! Valor final: R$ {valor:.2f}")
else:
    print(f"Valor da compra: R$ {bruto}")