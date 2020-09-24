largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
tot = largura * altura
tinta = tot / 2
print('A parede tem {}x{}, e sua área é {}m². Você vai gastar {}l de tinta para pintar toda sua parede.'.format(largura,altura,tot, tinta))
