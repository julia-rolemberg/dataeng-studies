# Na prática são funções anônimas, que nem precisam ter um identificador definido.

def processar(titulo, lista, funcao):
    print(f'Processamento: {titulo}')
    for i in lista:
        print(i, ' => ', funcao(i))

def dobro(x):
    return x * 2 

processar('Dobros de 1 a 10', range(1,11), dobro)

## fazendo do jeito funcional

processar('Dobros de 1 a 10', range(1,11), lambda x : x * 2)
