a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o o terceiro número: '))
# Verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print(f'{menor} é o menor número.')
# Verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print(f'{maior} é o maior número.')
