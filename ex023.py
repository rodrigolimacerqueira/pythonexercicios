num = int (input ('Digite um numero, de 0 a 9999:'))
un = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print ('Unidades: {}'.format(un))
print ('Dezenas: {}'.format (dez))
print ('Centenas:{}'.format (cent))
print ('Milhares:{}'.format(mil))
