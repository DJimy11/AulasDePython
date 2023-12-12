velocidade = float(input('insira a velocidade que foi lida: '))
if velocidade <= 80:
    print('voce esta dentro do limite faça uma boa viagem')
else:
    print('o sr/a acbaou de ultrappasar o limite de velocidade e a '
          'a sua multa sera de:')
if velocidade > 80:
    multa = (velocidade - 80) * 7000
    print(f'{multa}kz')
