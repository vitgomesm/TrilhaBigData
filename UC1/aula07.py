#ESTRUTURAS DE ARMAZENAMENTO (listas:continuação)

# lista1=[2,4,6,8,10]
# lista1.remove(6) #removeu o elemento '6' da minha lista pelo próprio elemento.
# lista1.remove(lista1[2]) #removeu o elemento de 'índice 2' da minha lista pelo índice.
# print(lista1) #[2,4,10]

# lista2=lista1.insert(2,1000)
# print(lista2) #vai resultar em 'None', pois eu salvei um comando da lista1 nessa nova lista.
# lista2=lista1.copy()
# print(lista2) #[2, 4, 1000, 10]

# lista3=lista1.copy()
# lista4=lista1.copy()
# lista3.clear() #limpa todo o conteúdo da lista, deixando-a vazia.
# print(lista3) #[]
# lista4.pop(0) #estou removendo o elemento de 'índice zero' da minha lista.
# print(lista4) #[4, 1000, 10]
# lista4.sort() #coloquei meus elementos da lista em ordem crescente.
# print(lista4) #[4, 10, 1000]
# lista4.reverse() #coloquei meus elementos em ordem inversa.
# print(lista4) #[1000, 10, 4]

# frutas=['uva', 'maçã',2, 4.5, True, 'carambola', 'melancia']
# frutas.sort() #o coando também funciona para elementos do tipo 'string'.
# print(frutas)

#TUPLAS #são imutáveis: podemos cosultar e reodernar tuplas, nunca adcionar ou remover itens

# frutas2=tuple(frutas)
# print(frutas2.index('uva')) #eu consultei em qual índice se encontra o elemento uva
# print(frutas2.count('uva')) #eu comsultei quantas vezes o elemento 'uva'


#DICIONÁRIOS: estruturas que salvam as 

estados={ 'RJ':'Rio de Janeiro',
          'SP':'São Paulo',
          'MG':'Minas Gerais',
          'ES':'Espírito Santo'}

print(estados)

print(estados.keys())
print(estados.values())

candidatos={'Larissa':28,
            'Anna':20
}

