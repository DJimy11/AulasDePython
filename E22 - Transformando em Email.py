nome = str(input('insira o seu nome completo '))
dividir = nome.split()
gmail = ''.join(dividir).lower()
print(f'Obrigado por confiar na nossa empresa sr.{nome}! Este e o seu novo E-mail: {gmail}@gmail.com')
