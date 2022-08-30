#1. No paradigma funcional usando map retorne frases '<Nome> tem <idade> anos.' para o list a seguir

lista = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26}
]


final = map(lambda pessoa : f'{pessoa["nome"]}, tem {pessoa["idade"]} anos', lista)
print(list(final))