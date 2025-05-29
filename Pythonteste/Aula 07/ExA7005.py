n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=', ') #O end serve para não quebar a linha.
print('a divisão inteira é {} e potência é {}'.format(di, e))
