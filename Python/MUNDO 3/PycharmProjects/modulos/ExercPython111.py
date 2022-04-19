# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha
# dois módulos internos chamados moeda e dado. Transfira todas
# as funções utilizadas nos desafios 107, 108 e 109 para o primeiro
# pacote e mantenha tudo funcionando.
# ---
# by geanclm in 18/04/2022 at 21h
# ---
from usefull.moeda import resumo

n = float(input('Digite o preço R$: '))
resumo(n,20,12)