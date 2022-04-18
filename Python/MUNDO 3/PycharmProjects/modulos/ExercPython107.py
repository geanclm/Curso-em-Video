# Exercício Python 107: Crie um módulo chamado moeda.py que tenha
# as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# ---
# by geanclm in 18/04/2022 at 6h
# ---
import usefull.moeda

# entrada de dados
n = float(input('Digite o preço: '))

# aplicando os módulos do pacote usefull.moeda
print(f'Aumentando {n}% o valor final é R$ {usefull.moeda.aumentar(n)}')
print(f'Diminuindo {n}% o valor final é R$ {usefull.moeda.diminuir(n)}')
print(f'O dobro de {n} é R$ {usefull.moeda.dobro(n)}')
print(f'A metade de {n} é {usefull.moeda.metade(n)}')