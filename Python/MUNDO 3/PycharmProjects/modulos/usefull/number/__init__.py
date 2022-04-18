# by geanclm in 17/04/2022

def fatorial(n=0):
    """
    -> Função para retornar o fatorial de um número
    """
    f=1
    for i in range(1, n+1):
        f *= i
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3