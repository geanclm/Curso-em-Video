# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos
# no desafio 111, temos um módulo chamado dado. Crie uma função
# chamada leiaDinheiro() que seja capaz de funcionar como a
# função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.
# ---
# by geanclm in 18/04/2022 at 22:53h
# ---
from usefull.dado import leiaDinheiro
from usefull.moeda import resumo

n = leiaDinheiro('Digite o preço R$: ')
resumo(n,35,22)