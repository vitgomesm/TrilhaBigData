potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

area_comodo = largura * comprimento
potencia_necessaria = area_comodo * 3
num_lampadas = potencia_necessaria / potencia_lampada
num_bocais = area_comodo / 3

num_lampadas = round(numero_lampadas)
num_bocais = round(numero_bocais)


print(f"Potência total necessária: {potencia_necessaria:} watts")
print(f"Número de lâmpadas necessárias: {num_lampadas}")
print(f"Número de bocais necessários: {num_bocais}")
