from math import sqrt, ceil, floor
from random import randint, choice
# MÓDULO MATH
# Ceil: erredonda para cima
# floor: arredonda para baixo
# trunc: mostra apenas a parte inteira do número
# pow: que calcula a potência de um número
# sqrt: calcula raiz quadrada de número
# factorial: calcula o fatorial de um número
#Sorteando um nome na lista usando a biblioteca Random

'''nome = ['Dumilde', 'Josias', 'Tyron']
print(f'O nome escolhido foi: {choice(nome)}')

#Sorteando um número entre 1 e 10 usando a biblioteca Random
num = randint(1, 10)
print(f'O número sorteado foi: {num}')'''

#Usando funções da biblioteca Math
num = float(input('Insira um número: '))
raiz = sqrt(num)
print(raiz)
print(f'{ceil(raiz)}')
print(f'{floor(raiz)}')

