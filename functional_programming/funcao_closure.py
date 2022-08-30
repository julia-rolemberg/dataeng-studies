# Funções que podem ser aninhadas e ter acesso ao escopo da função na qual foi definida, 
# inclusive impedindo o Garbage Colector de libera-las.


def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular # aqui só está definindo a função calcular, por isso eu nao passo parâmetro

dobro = multiplicar(2)
triplo =  multiplicar(3)
print(dobro) # só mostra a referência de memória das funçoes definidas
print(triplo)
print(dobro(7))
print(triplo(3))