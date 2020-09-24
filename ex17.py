import math
catop = float(input('Digite o número do cateto oposto: '))
catadj = float(input('Digite o número do cateto adjacente: '))
soma = math.hypot(catop, catadj)
print('A soma da Hipotenusa do Triangulo Retângulo é {:.2f}'.format(soma))

