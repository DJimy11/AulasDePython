a = float(input('inisira o valor da priemeira recta: '))
b = float(input('insira o valor da segunda recta: '))
c = float(input('insira o valor da ultima recta: '))
if (b - c)*-1 < a and (a - c)*-1 < b and (a - b)*-1 < c:
    if b + c > a and a + c > b and a + b > c:
        print(f'As rectas {a}, {b} e {c} podem formar um triângulo!')
else:
    print(f'As rectas {a}, {b} e {c} não podem formar um triângulo!')
