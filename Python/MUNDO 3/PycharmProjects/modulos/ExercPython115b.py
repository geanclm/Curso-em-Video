# Exercício Python 115b: Vamos ver como fazer acesso
# a arquivos usando o Python.
# ---
# by geanclm in 20/04/2022
# ---

from time import sleep
from  usefull.moeda import menu
from usefull.number import leiaInt
from usefull.color import textoAmarelo, textoVerde, textoVermelho
from usefull.dado import escreverArquivo, lerArquivo, arquivo, criarArquivo

# ---
# verificação inicial
arq = 'dados.txt'
if not arquivo(arq):
    criarArquivo(arq)
# ---

menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])

while True:
    op = int(leiaInt(f'{textoAmarelo("Digite uma opção: ")}'))
    if op == 3:
        print(f'{textoVerde("SAINDO DO SISTEMA...Até mais!")}')
        sleep(2)
        break
    if 1 != op != 2:
        print(f'{textoVermelho("Digite uma opção válida do MENU")}')
    if op == 1:
        lerArquivo(arq)
    if op == 2:
        escreverArquivo(arq)
    sleep(2)