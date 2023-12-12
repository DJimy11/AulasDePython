print('=' * 50)
print(f'\033[1;34m{"BANCO SILVANS":^50}\033[m')
print('=' * 50)

valor_casa = float(input('Qual é o valor da casa? KZ'))
salário = float(input('Qual é o seu salário? KZ'))
anos = int(input('E quantos anos vais pagar a casa: '))
prestação = valor_casa / (anos * 12)
s30 = salário * (30 / 100)
print(f'Para pagar a casa de {valor_casa}KZ em {anos} anos.')
print(f'serão necessários {prestação:.1f} por mês.')

print('=' * 50)
print(f'\033[1;34mComparando {prestação:.1f} - {s30:.1f}...\033[m')
print('=' * 50)

if prestação > s30:
    print(f'\033[1;31mInfelizmente não podemos fazer o empréstimo!\033[m')
else:
    print(f'\033[1;34mO empréstimo foi feito com sucesso!\033[m')
print('Obrigado! Volte falar.')
