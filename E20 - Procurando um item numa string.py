frase = str(input('insira uma frase ')).upper()
contar = frase.count('A')
encontrar = frase.find('A')
last = frase.rfind('A')

print(f'Na frase "{frase}" a letra a esta repetida {contar}x')
print(f'A primeira  letra (a) esta na posiçao numero {encontrar}')
print(f'A ultma letra (a) encontra-se na na posiçao numero {last}')
