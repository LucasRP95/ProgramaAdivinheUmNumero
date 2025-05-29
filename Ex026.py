frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez apareceu na posição {}'.format(frase.find('A')))
print('A ultima letra apareceu na posiçao {}'.format(frase.rfind('A')))
