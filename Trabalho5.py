nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: ")
optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

if optativa != -1:
    menor_nota = min(nota1, nota2)
    if optativa > menor_nota:
        if menor_nota == nota1:
            nota1 = optativa
        else:
            nota2 = optativa

media = (nota1 + nota2) / 2

print(f"Média do semestre: {media:.2f}")

if media >= 6.0:
    print("Aluno: Aprovado")
elif media < 3.0:
    print("Aluno: Reprovado")
else:
    print("Situação: Exame")
