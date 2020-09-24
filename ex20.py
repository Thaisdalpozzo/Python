import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
ordem = [n1,n2,n3]
random.shuffle(ordem)
print('A ordem dos alunos sorteados é {}'.format(ordem))


