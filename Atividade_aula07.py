#Variáveis para armazenar as listas
numeros_pares = []
numeros_impares = []


# Loop para coletar 20 números pares e 20 números ímpares
while len(numeros_pares) < 20 or len(numeros_impares) < 20:
    numero = int(input("Digite um número: "))

# Verifica se o número é par e se ainda há espaço para pares
    if numero % 2 == 0 and len(numeros_pares) < 20:
        numeros_pares.append(numero)

# Verifica se o número é ímpar e se ainda há espaço para ímpares
    elif numero % 2 != 0 and len(numeros_impares) < 20:
        numeros_impares.append(numero)

# Exibe os números armazenados
print("\nNúmeros pares armazenados:")
print(numeros_pares)

print("\nNúmeros ímpares armazenados:")
print(numeros_impares)
