# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios
# anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.
# ---
# by geanclm in 18/04/2022
# ---
from usefull.moeda import resumo

n = float(input('Digite o preço R$: '))
resumo(n,20,12)