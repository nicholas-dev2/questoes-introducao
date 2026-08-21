saldo = int(input("Insira seus V-Bucks: "))
preço = int(input("Insira o preço da skin: "))

if saldo >= preço:
    print("Compra realizada! Aproveite sua skin!")

else:
    print(f"Você não possui saldo suficiente, faltam {preço - saldo} V-Bucks")