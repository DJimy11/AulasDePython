num = int(input('Insira um número inteiro: '))
print('[ 1 ] - CONVERTER EM BINÁRIO\n'
      '[ 2 ] - CONVERTER EM OCTAL\n'
      '[ 3 ] - CONVERTER EM HEXADECIMAL')

opção = int(input('Vai convertar para qual valor: '))
if opção == 1:
    print(f'Convertendo o valor {num} para BINÁRIO: {bin(num)[2:]}')
elif opção == 2:
    print(f'Convertendo o valor {num} para OCTAL: {oct(num)[2:]}')
elif opção == 3:
    print(f'Convertendo o valor {num} para HEXADECIMAL: {hex(num)[2:]}')
else:
    print('\033[31mOpção inválida! Tenta outra vez.\033[m')

