segundos = int(input("Insira a quantidade de segundos: "))

dias = segundos // 86400
segundos = segundos % 86400

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

print(f"Dias: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos restantes: {segundos}")
