horas = int(input("Horas livres: "))
materias = int(input("Quantidade de matérias: "))
cada_materia = (horas - 3) / materias

print("Você deve reservar", cada_materia, "horas por matéria")