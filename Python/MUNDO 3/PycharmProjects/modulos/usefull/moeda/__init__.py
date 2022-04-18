def aumentar(n,p=10):
    """
    :param n: valor para calcular o aumento
    :param p: percentual para aplicar. Se não informado é assumido 10%
    :return: valor final com o aumento
    """
    a = ((n*p)/100)+n
    return a

def diminuir(n,p=10):
    """
    :param n: valor para calcular o desconto em %
    :param p: percentual para aplicar. Se não informado é assumido 10%
    :return: valor final de desconto
    """
    d = n-((n*p)/100)
    return d

def dobro(n):
    d = n*2
    return d

def metade(n):
    m = n/2
    return m

def moeda(n, moeda='R$'):
    """
    -> format o valor na moeda local
    :param n: valor para formatar
    :param moeda: cifrão da moeda
    :return: retorna o valor formatado com cifrão e casas decimais por ','
    """
    f = (f'{moeda} {n:.2f}').replace('.',',')
    return f