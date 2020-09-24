import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
nom = [n1,n2,n3]
esco = random.choice(nom)
print('o Aluno escolhido é {}'.format(esco))
