import math
dim = float(input('Digite o valor que você tem na carteira para conversão em Dólares. R$:'))
con = float(input('Informe o valor da cotação do dólar:'))
resu = dim / con
print('O valor total de Reais convertido em Dolar é: {:.2f}¢'.format(resu))