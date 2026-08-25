jogador1 = input("Par ou Ímpar? ")
escolha1 = int(input("Escolha do jogador 1: "))
escolha2 = int(input("Escolha do jogador 2: "))

if jogador1 == "Par" and (escolha1 + escolha2) % 2 == 0:
    print("Jogador 1 venceu!")
elif jogador1 == "Ímpar" and (escolha1 + escolha2) % 2 != 0:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")