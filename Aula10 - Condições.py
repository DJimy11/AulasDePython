cores = {'sem cores': '\033[0;0;0m',    # Sem Cores
         'preto': '\033[0;30;107m',     # Preto
         'vermelho': '\033[31m',        # Vermelho
         'verde': '\033[32m',           # Verde
         'amarelo': '\033[33m',         # Amarelo
         'azul': '\033[34m',            # Azul
         'roxo': '\033[35m'             # Roxo
          }

# Condiçao composta
'''a = str(input('O pai está em casa? [S/N]  ')).upper()
if a[0] == 'S':
    print(f'{cores["azul"]}Vais com o pai.{cores["sem cores"]}')
else:
    print(f'{cores["vermelho"]}Vais de táxi!{cores["sem cores"]}')'''

'''# Condição simples
num = int(input('Insira um número:'))
if num >= 5:
    print(f'{num} é maior ou igual que 5')

# Condição simplificada
num = int(input('Insira um número: '))
print('Maior' if num > 5 else 'Menor')
d = 5
dis = d*0.5 if d >= 5 else d*0.4
print(dis)'''

'''distancia = float(input('Qual distãncia vai andar: '))
if distancia <= 10:
    print('Você vai num lugar próximo!')
elif distancia > 10 and distancia <= 50:
    print('Você vai num lugar um pouco distante!')
elif distancia >= 51 and distancia <= 100:
    print('Estás a ir muito longe!')
else:
    print('Estás a ir no cu do Bói')
print('Boa Viagem!')'''
