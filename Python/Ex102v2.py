def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
