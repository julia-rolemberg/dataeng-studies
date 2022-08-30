pessoas = [
    {'nome': 'Ze', 'idade':11},
    {'nome': 'Julia', 'idade':19},
    {'nome': 'Ana', 'idade':10},
    {'nome': 'Caio', 'idade':35},
]

lista_maior = []

# imperativo
for pessoa in pessoas:
    if pessoa['idade'] > 17:
        lista_maior.append(pessoa)
print(lista_maior)


maior = filter(lambda p: p['idade'] > 17, lista_maior)

print(list(maior))


