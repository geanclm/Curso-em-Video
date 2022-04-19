# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# by geanclm in 19/04/2022 at 07:34h

from usefull.number import leiaInt, leiaReal

ni = leiaInt('Digite um inteiro: ')
nr = leiaReal('Digite um número real: ')

print(f'''O valor inteiro informado  é {ni}
 e o valor real, {nr}.''')