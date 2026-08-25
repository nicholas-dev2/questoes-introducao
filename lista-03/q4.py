mensagem = input("Digite uma mensagem: ")

if len(mensagem) < 3 or len(mensagem) > 140:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
    print("Mensagem enviada com sucesso!")