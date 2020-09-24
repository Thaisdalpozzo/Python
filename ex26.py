frase = str(input('Digite qualquer frase: ')).upper().strip()
print('Aparece {} vezes a letra A'.format(frase.count('A')))
print('A primeira posição aparece em {}'.format(frase.find('A')+1))
print('A ultima posição aparece em {}'.format(frase.rfind('A')+1))
