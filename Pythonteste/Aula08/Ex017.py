from math import hypot

ad = float(input('Adjascente: '))
op = float(input('Oposto: '))
#hipo = (ad**2 + op**2) ** (1/2)
#print('A hipotenusa é {:.2f}'.format(hipo))
hipo = hypot(op, ad)
print('A hipotenusa é {:.2f}'.format(hipo))