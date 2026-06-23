tamanho = float(input("Tamanho (MB): "))
velocidade_por_bit = float(input("Velocidade (Mbps): "))
velocidade_por_megabyte = velocidade_por_bit * 0.125
velocidade_arquivo_segundos = tamanho / velocidade_por_megabyte
velocidade_arquivo_minutos = velocidade_arquivo_segundos / 60

print("Irá levar", velocidade_arquivo_minutos, "minutos")