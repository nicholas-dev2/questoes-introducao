horas = int(input("Quantas horas você assiste? "))

if horas < 1:
    print("Epectador Casual")
elif horas > 1 and horas <= 3:
    print("Maratonista Iniciante")
elif horas > 3 and horas <= 5:
    print("Maratonista Profissional")
else:
    print("Alerta vermelho! Desligue a tela e vá ver o sol!")