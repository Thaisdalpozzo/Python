distancia = float(input('Digite a distância de uma viagem em KM: '))
print('Você está prestes a começar uma viagem de {}'.format(distancia))

if distancia <= 200:
    preco1 = distancia * 0.50
    print('Você terá que pagar {:.2f}'.format(preco1))
else:
    preco2 = distancia * 0.45
    print('Você terá que pagar {:.2f}'.format(preco2))
