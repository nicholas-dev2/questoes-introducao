dia = int(input("Dia da semana: "))
espera = int(input("Dias de espera: "))
novo_dia = (dia + espera) % 7

dias = {

    0: "Domingo",
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado"

}

print(f"O dia da semana será {dias[novo_dia]}")