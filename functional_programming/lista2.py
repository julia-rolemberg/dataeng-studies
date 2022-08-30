from functools import reduce

#2. Para a lista Utilizando apenas função lambda e as funções map , reduce e filter .
#  Crie um script que some todas as idades das pessoas com menos de 18 anos:

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]
 
print(reduce(lambda idade, pessoa: idade + pessoa['idade'], filter(lambda p: p['idade'] < 17, pessoas), 0))


