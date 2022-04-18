from random import shuffle
nom1 = str (input ('Digite o primeiro nome:'))
nom2 = str (input ('Digite o segundo nome:'))
nom3 = str (input ('Digite o terceiro nome:'))
nom4 = str (input ('Digite o quarto nome:'))
lista = [nom1,nom2,nom3,nom4]
shuffle (lista)
print ('A sequencia dos nomes sorteados foram:')
print (lista)

