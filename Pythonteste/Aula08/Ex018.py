import math

angulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
input('O ângulo de {} \ntem seno de {:.2f} \ne cosseno de {:.2f} \ne tangente de {:.2f}'.format(angulo, seno, cos, tang))

