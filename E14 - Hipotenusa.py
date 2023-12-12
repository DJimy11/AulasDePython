from math import sqrt, pow
from random import shuffle
'''oposto = float(input('Digite o comprimento do cateto oposto:  '))
adjacente = float(input('Digite o comprimento do cateto adjacente:  '))
hipotenusa = sqrt(oposto**2 + adjacente**2)
print(f'A Hipotenusa é igual a: {hipotenusa}')'''

nome1 = str(input('Insira o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))
nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print(f'A nova ordem dos nomes é: {nomes}')