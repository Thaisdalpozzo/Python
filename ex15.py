car = float(input('Quantos km foram percorridos no carro alugado? '))
di = int(input('Quantos dias o carro foi alugado?'))
soma =(0.15 * car) + 60 * di
print('o preço a pagar pelos {} dias percorridos com o carro com base em seus KM rodados: {}Km. A soma do valor a ser pago é de R${}'.format(di,car,soma))


