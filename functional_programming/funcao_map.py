# Map: A função map é muito usada em liguagens funcionais como Haskell e Lisp.
# Executa uma função em cada elemento de uma lista ou de um conjunto de listas.

lista_1 = [1,2,3,4]

# imperativo
lista_resul =[]
for i in lista_1: 
    lista_resul.append(i*2)
print(lista_resul)

# funcional + lambda
# map é como um forEach
dobro = map(lambda x: x*2, lista_1) 
print(list(dobro))

