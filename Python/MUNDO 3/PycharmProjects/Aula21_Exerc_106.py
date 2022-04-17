# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
# by geanclm in 17/04/2022 at 14h

from time import sleep

c=('\033[m',            # 0 = sem cor
   '\033[37;41m',       # 1 = vermelho
   '\033[30;42m',       # 2 = verde
   '\033[30;43m',       # 3 = amarelo
   '\033[30;44m',       # 4 = azul
   '\033[30;45m',       # 5 = roxo
   '\033[7;30m',        # 6 = branco
    )


def ajuda(consulta):
    escreva(f'Acessando o manual do comando \'{consulta}\'',4)
    print(c[3], end='')
    help(consulta)
    print(c[0], end='')
    sleep(2)


def escreva(texto, cor=0):
    texto = ' '+texto+' '
    print(c[cor], end='')
    print('-'*(len(texto)))
    print(f'{texto}')
    print('-'*(len(texto)))
    print(c[0], end='')
    sleep(1)


while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    consulta = str(input('Função / biblioteca ["Q" para sair]: '))
    if consulta.upper() == 'Q':
        break
    else:
         ajuda(consulta)


escreva ('QUIT', 1)