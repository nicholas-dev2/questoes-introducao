cigarros = int(input("Cigarros por dia: "))
anos = int(input("Anos que fumou: "))
reducao = (((anos * 365) * cigarros) * 10) / 1440

print("Perdeu", reducao, "dias de vida")
