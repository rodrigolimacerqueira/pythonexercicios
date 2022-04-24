from random import randint
from time import sleep
print('=='*20)
print('Acerte o número!!!')
print('=='*20)
comp = randint(0,5)
jog = int (input('Digite um número entre 0 e 5, para tentar adivinhar:'))
print ('Processando...')
sleep(3)
if jog == comp:
    print ('Você adivinhou. Parabéns!!!')
else:
    print ('Você perdeu! O número é {}'.format(comp))
