
print('..........ANALISADOR DE TRIÂNGULOS..........')
r1 = float(input('1° reta: '))
r2 = float(input('2° reta: '))
r3 = float(input('3° reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;30;45mE possivel fazer um triângulo! \033[m')
else:
    print('Não é possivel formar um triângulo!')

