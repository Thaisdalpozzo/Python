from random import randint
print('Tente desvendar qual número o computador pensou...')
comput = randint(0,5)
jogador = int(input('Advinhe o número que pensei.... :'.format(comput)))
if jogador == comput:
    print('Você venceu!!! PARÁBENS! ')
else:
    print('O computador venceu!!! PERDEU! ')

