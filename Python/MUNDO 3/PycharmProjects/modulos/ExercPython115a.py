# Exercício Python 115a: Vamos criar um menu em Python,
# usando modularização.
# ---
# by geanclm in 19/04/2022 at 19:53h
# ---
from time import sleep
from  usefull.moeda import menu
from usefull.number import leiaInt
from usefull.color import textoAmarelo, textoVerde, textoVermelho

menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])

while True:
    op = int(leiaInt(f'{textoAmarelo("Digite uma opção: ")}'))
    if op == 3:
        print(f'{textoVerde("SAINDO DO SISTEMA...Até mais!")}')
        sleep(2)
        break
    if 1 != op != 2:
        print(f'{textoVermelho("Digite uma opção válida do MENU")}')