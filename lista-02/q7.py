ganho = float(input("Ganho por hora (R$): "))
horas = int(input("Horas trabalhadas: "))
bruto = ganho * horas
renda = ganho * 0.11
inss = ganho * 0.08
sindicato = ganho * 0.05
liquido = ganho - renda - inss - sindicato 

print(f"Valor do imposto de renda: R${renda:.2f}")
print(f"Valor do inss: R${inss:.2f}")
print(f"Valor do sindicato: R${sindicato:.2f}")
print(f"Valor do salário líquido: R${liquido:.2f}")