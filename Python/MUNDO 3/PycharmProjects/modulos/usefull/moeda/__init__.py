def aumentar(n, p=10, formatar=False):
    """
    :param n: valor para calcular o aumento
    :param p: percentual para aplicar. Se não informado é assumido 10%
    :return: valor final com o aumento
    """
    a = ((n*p)/100)+n
    return a if formatar is False else moeda(a)


def diminuir(n, p=10, formatar=False):
    """
    :param n: valor para calcular o desconto em %
    :param p: percentual para aplicar. Se não informado é assumido 10%
    :return: valor final de desconto
    """
    d = n-((n*p)/100)
    return d if formatar is False else moeda(d)

def dobro(n, formatar=False):
    d = n*2
    return d if formatar is False else moeda(d)

def metade(n, formatar=False):
    m = n/2
    return m if formatar is False else moeda(m)

def moeda(n, moeda='R$'):
    """
    -> format o valor na moeda local
    :param n: valor para formatar
    :param moeda: cifrão da moeda
    :return: retorna o valor formatado com cifrão e casas decimais por ','
    """
    f = (f'{moeda} {n:.2f}').replace('.',',')
    return f

def textoAlinhado(texto):
    texto = ' '+texto+' '
    print('-'*(len(texto)))
    print(f'{texto}')
    print('-'*(len(texto)))

def resumo (n=0,a=10,d=5):
    textoAlinhado('       RESUMO DO VALOR       ')
    print (f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, formatar=True)}')
    print(f'Metade do preço: \t{metade(n, formatar=True)}')
    print(f'{a}% de aumento: \t{aumentar(n, p=a, formatar=True)}')
    print(f'{d}% de redução: \t{diminuir(n, p=d, formatar=True)}')
    print('-'*31)