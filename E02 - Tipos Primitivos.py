#a = 1
#b = 2
#c = 3
#O código abaixo vai mostrar uma mensagem na tela usando f string
#print(f'Número 1 é: {a} o número 2 é: {b} e o número 3 é: {c}')
#idade = int(input())
#nome = str(input())
#peso = float(input())
#nome1 = str(input('Insira o nome1: '))
#nome2 = str(input('Insira o nome2: '))
#nome3 = str(input('Insira o nome3: '))
#print(f'Nome1 é: {nome1} o Nome2 é:{nome2} e o Nome3 é: {nome3}')

valor = input('Escreva algo: ')
print(f'O valor {valor} está todo em maiúsculas? R: {valor.isupper()}')
print(valor.islower())
print(valor.isalnum())
print(valor.isnumeric())
print(valor.isalpha())
print(valor.isspace())
