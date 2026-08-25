n1, n2 = map(int, input("Insira as notas: ").split())

if (n1 + n2) / 2 < 20:
    print("REPROVADO direto.")
elif (n1 + n2) / 2 >= 60:
    print("Parabéns, você foi APROVADO!")
else:
    print("Você ficou em RECUPERAÇÃO! Estude para a prova final.")