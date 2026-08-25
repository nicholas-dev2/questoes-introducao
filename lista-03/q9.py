idade = int(input("Qual a sua idade: "))
if idade >= 60:
    print("Gratuidade concedida por lei!")
else:
    if idade < 18:
        print("Meia-entrada autorizada!")
    else:
        carteira = input("Você possui carteira de estudante? ")
        if carteira == "Sim":
            print("Meia-entrada autorizada!")
        else:
            print("Passagem inteira.")