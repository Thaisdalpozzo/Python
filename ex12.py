preco = float(input('Preco original do produto R$: '))
soma = preco * 5 / 100
fim = (soma - preco)
print('O produto que vale {} tem 5% de desc. o valor do desconto é {:.2f} e o preco do produto com desconto fica {}'.format(preco,soma, fim))
