# Funções de alta ordem
# Capacidade de uma função de receber como parâmetro e/ou retornar outras funções.

from funcao_primeira_classe import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, ' => ', funcao(i))

# coloco esse mais pra ele começar a execução por onde eu mando, senão ele roda o arquivo como um script
if __name__ == '__main__':
    processar('Dobros de 1 a 10 ', range(1,11), dobro)