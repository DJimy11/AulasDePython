from random import randint
sortear = randint(1, 5)
adivinhar = int(input('em qual numero estou a pensar? '))
if adivinhar == sortear:
    print('correcto')
else:
    print('errrouuu!!!!')
if adivinhar > 5:
    print('dica o numero que eu pensei esta no intervalo de 1 a 5')
print(f'o numero que eu pensei foi {sortear}')
