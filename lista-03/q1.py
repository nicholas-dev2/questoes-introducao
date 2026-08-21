conta = int(input())
amigos = int(input())
pergunta = input("Pagar taxa de serviço? ")

total_amigo = (conta / amigos) * 1.10 if pergunta == "sim" else (conta/amigos)

print(f"Cada amigo vai pagar {total_amigo:.2f}R$")
