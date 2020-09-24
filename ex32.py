ano = int(input('Digte o seu ano atual e veja se é Bissexto ou não: '))
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('Ano bissexto!')
        else:
            print(' Não Bissexto')
    else:
        print('Bissexto')
else:
    print('Não Bissexto')
