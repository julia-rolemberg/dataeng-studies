# redução de dimensão
from functools import reduce

pessoas = [
    {'nome': 'Carlos', 'idade':11},
    {'nome': 'Julia', 'idade':19},
    {'nome': 'Ana', 'idade':10},
    {'nome': 'Bakery', 'idade':35},
]

total = 0
for i in pessoas:
    total += i['idade']

print(total)

## forma funcional de fazer a mesma coisa
soma_idades = reduce(lambda idade, pessoa: idade + pessoa['idade'], pessoas, 0)
# na função reduce, o lambda sempre vai ter esse formato (lambda totalizador, iterable: retorno do totalizador)

print(soma_idades)