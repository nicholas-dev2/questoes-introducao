prova1 = float(input("Nota na primeira prova: "))
prova2 = float(input("Nota na segunda prova: "))
prova3 = (70 - (prova1 * 2) - (prova2 * 3)) / 5

if prova3 <= 10:
    print(f"Nota mínima pra passar: {prova3}")
    
else:
    print("O aluno não pode mais passar")