import random

n1 = input('Aluno: ')
n2 = input('Aluno: ')
n3 = input('Aluno: ')
n4 = input('Aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista) #shuffle embaralha os itens da lista.
print('A ordem de apresentação será: {}'.format(lista))
