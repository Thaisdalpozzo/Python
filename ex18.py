import math
ang = float(input('Digite um ângulo para ser calculado: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Seno de {:.2f} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang,seno,cos,tang))
