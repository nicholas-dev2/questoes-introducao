preco = float(input("Preço: "))
desconto = float(input("Desconto: "))

preco -= preco * (desconto / 100)

print("Preço com desconto:", preco)
