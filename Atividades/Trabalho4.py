codigo = int(input("Digite o código de origem do produto (1 a 11): "))

if codigo == 1:
    print("Região de procedência: Sul")
elif codigo == 2:
    print("Região de procedência: Norte")
elif codigo == 3:
    print("Região de procedência: Leste")
elif codigo == 4:
    print("Região de procedência: Oeste")
elif codigo == 5 or codigo == 6:
    print("Região de procedência: Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print("Região de procedência: Sudeste")
elif codigo == 10:
    print("Região de procedência: Centro-oeste")
elif codigo == 11:
    print("Região de procedência: Noroeste")
else:
    print("Produto importado")
