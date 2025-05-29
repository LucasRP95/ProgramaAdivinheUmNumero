num = int(input('Informe um numero: '))
#n = str(num)
print('Analisando o número {}'.format(num))
#print('unidade: {}'.format(n[3]))
#print('dezena: {}'.format(n[2]))
#print('centena: {}'.format(n[1]))
#print('milhar: {}'.format(n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))
print('Obrigado')