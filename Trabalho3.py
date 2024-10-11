preco_combustivel = 6.00

inicio_odometro = float(
    input("Digite a marcação do odômetro no início do dia (em km): "))
fim_odometro = float(
    input("Digite a marcação do odômetro no final do dia (em km): "))
litros_gastos = float(
    input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(
    input("Digite o valor total recebido dos passageiros (em R$): "))

distancia = fim_odometro - inicio_odometro

med_consumo = distancia / litros_gastos

custo_combustivel = litros_gastos * preco_combustivel

lucro = valor_recebido - custo_combustivel

print(f"Média de consumo: {med_consumo:} km/L")
print(f"Lucro (liquido) do dia: R$ {lucro:}")
