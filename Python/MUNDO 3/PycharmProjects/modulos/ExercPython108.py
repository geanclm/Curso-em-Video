# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
# ---
# by geanclm in 18/04/2022 at 11:23h
# ---
from usefull.moeda import aumentar, diminuir, dobro, metade, moeda

# entrada de dados
n = float(input('Digite o preço: '))
p = float(input('Percentual [%]: '))

# aplicando os módulos do pacote usefull.moeda
print(f'Aumentando {p}% o valor final é {moeda(aumentar(n,p),"R$")}')
print(f'Diminuindo {p}% o valor final é {moeda(diminuir(n,p))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
print(f'A metade de {moeda(n)} é {moeda(metade(n))}')