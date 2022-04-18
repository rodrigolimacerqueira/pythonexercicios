from math import hypot
catetoo = float (input('Digite o cateto oposto:'))
catetoa = float (input('Digite o cateto adjascente:'))
hip = hypot(catetoo, catetoa)
print ('O comprimento da hipotenusa é: {:.2f}'.format (hip))
