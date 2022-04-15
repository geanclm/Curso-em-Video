n1 = int(input('digite a nota 1: '))
n2 = int(input('digite a nota 2: '))
reais = float(input('quantos reais voce tem? '))
suc = int(n1+1)
ant = int(n1-1)
dobro = int(n1*2)
triplo = int(n1*3)
raiz =  float(n1**(1/2))
soma = n1+n2
media = float(soma/2)
m = n1*100
mm = n1*1000

t1 = n1*1
t2 = n1*2
t3 = n1*3
t4 = n1*4
t5 = n1*5
t6 = n1*6
t7 = n1*7
t8 = n1*8
t9 = n1*9

dollar = float(reais/3.27)
area = n1*n2
LitrosTinta = float(area/2)
desconto = n1-(n1*(5/100))
reajuste = n1+(n1*(15/100))

#exercicio 05
print('o sucessor eh {}, e o anteecessor eh {}'.format (suc, ant))
#exercicio 06
print ('o dobro eh {}, o triplo eh {}, e a raiz quadrada eh {}'.format(dobro, triplo, raiz))
#ecercicio 07
print('a media de notas eh {}'.format(media))
#exercicio 08
print ('o valor de ',n1,' em centimetros eh {}, e milimetros eh {}'.format(m,mm))
#exercicio 09 - TABUADA
print('a tabuada de ',n1,' eh {} {} {} {} {} {} {} {} {}'.format(t1, t2, t3, t4, t5, t6, t7, t8, t9))

#exercicio 10 - DOLLAR
print('voce pode comprar dollares = {}'.format(dollar))

#exercicio 11
print('a area total de parede eh {} e a quantidade de listros de tinta necessaria são {}'.format(area, LitrosTinta))

#exercicio 12
print(' o valor de',n1, 'com 5% desc eh R$ {}'.format(desconto))

#exercicio 13
print ('o valor',n1,' com 15% de aumento eh igual a {}'.format(reajuste))