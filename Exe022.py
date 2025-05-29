nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiuscula é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem o total de {} letras.'.format(len(nome) - nome.count(" "))) #desconsidera os espaços entre as palavras
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

