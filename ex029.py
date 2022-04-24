vel = float (input('Digite a velocidade do carro:'))
multa = (vel-80)*7
if vel > 80:
    print ('Você foi multado! A multa foi de R$ {:.2f}'.format(multa))
    print ('Dirija com segurança')
else:
    print ('Você não foi multado. Parabéns!!!')
