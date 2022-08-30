def fatorial_imperativo(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado


def fatorial_recursivo(n):
    return n * (fatorial_recursivo(n-1) if(n-1) > 1 else 1)


if __name__ == "__main__":
    print(fatorial_imperativo(5))
    print(fatorial_recursivo(5))
    