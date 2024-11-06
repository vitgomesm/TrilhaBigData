comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

area_parede = 2 * (comprimento * altura) + 2 * (largura * altura)

area_piso = 1.5

qtd_cx = (area_parede / area_piso)

print(f"Quantidade de caixas de azulejos necessárias: {qtd_cx:}")
