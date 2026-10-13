def main():
    codigo = input("Insira o código que deseja rodar: ")

    def notas():
        notas = list(map(float, input("Insira as notas: ").split()))
        media = sum(notas) / len(notas)

        print(f"Maior nota: {max(notas)}")
        print(f"Menor nota: {min(notas)}")
        print(f"Média: {media:.2f}")

        mudar = input("Mudar alguma nota? S/N ")

        if mudar.upper() == "S":
            posição = int(input("Qual nota mudar? "))
            correção = float(input("Insira a nota corrigida: "))
            notas[posição - 1] = correção

        print("Notas: ", *notas)

    def coordenada():
        coordenada = tuple(map(int, input("Insira as coordenadas: ").split()))
        x, y = coordenada

        if x > 0 and y > 0:
            quadrante = "no primeiro quadrante"
        elif x < 0 and y < 0:
            quadrante = "no terceiro quadrante"
        elif x > 0 and y < 0:
            quadrante = "no quarto quadrante"
        elif x < 0 and y > 0:
            quadrante = "no segundo quadrante"
        elif x == 0 and y != 0:
            quadrante = "sobre o eixo y"
        elif x != 0 and y == 0:
            quadrante = "sobre o eixo x"
        else:
            quadrante = "na origem do plano"

        print(f"O ponto que correspode às coordenadas está {quadrante}.")

    def inscrições():
        nomes = list(map(str, input("Nomes dos inscritos: ").split()))

        zero_duplicados = set(nomes)

        print(f"Inscrições feitas: {len(nomes)}")
        print(f"Participantes: {len(zero_duplicados)}")

        alfabetico = sorted(zero_duplicados)

        print("Nome dos participantes:", *alfabetico)

    def playlist():
        músicas = ["unhappy", "afraid", "elephant cage", "can't have you", "rises the moon", "it's like i'm not even here"]

        while True:
            print("MENU")
            print("1 - Adicionar faixa")
            print("2 - Remover faixa")
            print('3 - Exibir playlist')
            print("4 - Sair")

            opção = int(input("Escolha uma opção: "))

            if opção == 1:
                faixa = input("Nome da música: ")
                músicas.append(faixa)

            elif opção == 2:
                removida = input("Música removida: ")
                músicas.remove(removida)

            elif opção == 3:
                for i in range(len(músicas)):
                    print(f"Música {i + 1}: {músicas[i]}")

            elif opção == 4:
                break

            else:
                print("Opção inválida")

    def cores():
        cor = tuple(map(int, input("Cor rgb: ").split()))

        red, green, blue = cor

        if red < 0 or red > 255 or green < 0 or green > 255 or blue < 0 or blue > 255:
            print("Cor inválida.")

        else:
            print(f"Cor: RGB({red}, {green}, {blue})")

    def clubes():
        grupo1 = set(map(str, input("Grupo 1: ").split()))
        grupo2 = set(map(str, input("Grupo 2: ").split()))

        participam_dois = grupo1 & grupo2
        participam_pelo_menos_um = grupo1 | grupo2
        exclusivos_robotica = grupo1 - grupo2
        exclusivos_programação = grupo2 - grupo1
        somente_um = grupo1 ^ grupo2

        print("Alunos que participam dos dois clubes: ", *participam_dois)
        print("Alunos que participam de pelo menos um dos clubes: ", *participam_pelo_menos_um)
        print("Alunos que participam só de robótica: ", *exclusivos_robotica)
        print("Alunos que participam só de programação: ", *exclusivos_programação)
        print("Alunos que participam somente de um clube: ", *somente_um)

    locals()[codigo]()

if __name__ == "__main__":
    main()
