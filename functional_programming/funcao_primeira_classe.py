def dobro(x):
    return x*2

def quadrado(x):
    return x ** 2

if __name__ == '__main__':
# conceito de primeira classe/ first class: encapsula uma função dentro de um variável
    d = dobro
    d2 = dobro
    print(d(3))
    print(d2(4)) # poderia isso para deixar separar diferentes usos da mesma função

    q = quadrado
    print(q(3))
    print(q(d(6)))


