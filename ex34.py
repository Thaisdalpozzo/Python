salario = float(input('Digite o valor do seu salário R$ '))
if salario <= 1250:
    sal = salario + (salario * 15 / 100)
else:
    sal = salario + (salario * 10 / 100)
print('O seu salário antigo era R${:.3f} e passou a ser R${:.3f} '.format(salario,sal))
