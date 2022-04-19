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

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31m ERRO: O dado informado não é um número inteiro válido. \033[0;0m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m O dado não foi informado \033[0;0m')
            return 0
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31m ERRO: O dado informado não é um número real válido. \033[0;0m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m O dado não foi informado \033[0;0m')
            return 0
        else:
            return n