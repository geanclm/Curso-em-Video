# by geanclm in 17/04/2022 at 14:55h
# programa principal

from usefull.number import fatorial
from usefull.number import dobro
from usefull.number import triplo

n = int(input('digite um número: '))
fat = fatorial(n)

print(f'O fatorial de {n} é {fat}')
print (f'O dobro de {n} é {dobro(n)}')
print (f'O triplo de {n} é {triplo(n)}')