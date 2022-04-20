nome = str (input('Digite seu nome completo:')).strip()
print ('O seu nome todo em maiusculo é:{}'.format(nome.upper()))
print ('O seu nome todo em minusculo é:{}'.format (nome.lower()))
print ('O nome completo tem: {} letras'.format (len(nome) - nome.count(' ')))
separa = nome.split()
print ('O primeiro nome tem {} letras'.format (len(separa[0])))



