# Exercício Python 109: Modifique as funções que form criadas
# o desafio 107 para que elas aceitem um parâmetro a mais, informando
# se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# esenvolvida no desafio 108.
# ---
# by geanclm in 18/04/2022
# ---
from usefull.moeda import aumentar, diminuir, dobro, metade, moeda

# entrada de dados
n = float(input('Digite o preço R$: '))
p = float(input('Percentual [%]: '))

# aplicando os módulos do pacote usefull.moeda
print(f'Aumentando {p}% o valor final é {aumentar(n,p,formatar=True)}')
print(f'Diminuindo {p}% o valor final é {diminuir(n,p,formatar=True)}')
print(f'O dobro de {moeda(n)} é {dobro(n,formatar=True)}')
print(f'A metade de {moeda(n)} é {metade(n,formatar=True)}')