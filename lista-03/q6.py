velocidade = int(input("Velocidade do veículo: "))

if velocidade <= 60:
    print("Velocidade permitida. Boa viagem!")
elif velocidade > 70:
    print("Infração Gravíssima! Multa de R$ 293,47 e perda de pontos na CNH.")
else:
    print("Infração Média! Multa de R$ 130,16.")