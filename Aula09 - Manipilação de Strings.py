frase = 'aula de python'
#Análise de Strings
tamanho = len(frase)
print(f'O tamanho da frase é: {tamanho}')
letra = frase.count(' ')
print(f'Existe {letra} espaços na frase.')
enco = 'a'
palavra = frase.find(enco)
print(f'O {enco} começou na posição: {palavra}')
existe = '123' not in frase
print(f'Existe na frase? R: {existe}')

#Transformação de Strings
novo = frase.replace('Python', 'C#')
print(novo)
maiuscula = frase.upper()
print(f'Tudo maiúsculo: {maiuscula}')
minusculo = frase.lower()
print(f'Tudo minúsculo: {minusculo}')
cap = frase.capitalize()
print(f'Primeira letra maiúsculo: {cap}')
tt = frase.title()
print(f'Primeiras letras maiúsculas: {tt}')

#Divisão de Strings
div = frase.split()
print(div)
print(div[0])
#Junção de Strings
juncao = '-'.join(frase.split())
print(juncao)