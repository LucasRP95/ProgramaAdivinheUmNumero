from random import randint
from time import sleep
computador = randint(0, 5)#sorteia o numero.
print('-=-'*20)
print('Vou pensar em um número entre zero e cinco, tente adivinhar.')
jogador = int(input('Digite um número de 0 a 5: '))#jogador tenta adivinhar.
print('Processando...')
sleep(2)
print('-=-'*20)
if jogador == computador:
    print('Parabéns você acertou.')
else:
    print('GANHEI!!, você errou, eu pensei no número {}.'.format(computador))


