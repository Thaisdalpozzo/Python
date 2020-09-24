vel = float(input('Digite a velocidade do seu carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi MULTADO! o valor a ser pago é: {:.2f}'.format(multa))
else:
    print('Você está na velocidade correta! ')
