###ATIVIDADE###
# Crie um código que seja capaz de ler e armazenar
# uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto
# de números.


#variaveis para criar a lista
pares=[]
impares=[]
contador=0

# num=int(input("Digite um numero"))

#Contador para limitar a 20 numeros 
while len(pares) < 3 or len(impares) < 3: 
    num=int(input("Digite um numero"))
   


if num % 2 == 0: 
    if len(pares) < 20:
        pares.append(num)
    else: print("A lista de pares já está cheia")

else:
    if len(impares) < 20:
        impares.append(num)
    else: print("A lista de impares já está cheia")

