import random

n1 = input('Primeiro aluno(a): ')
n2 = input('segundo aluno(a): ')
n3 = input('terceiro aluno(a): ')
n4 = input('quarto aluno(a): ')
lista = [n1, n2, n3, n4]
print('O aluno(a) escolhido(a) foi {}'.format(random.choice(lista)))

