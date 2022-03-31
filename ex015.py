kms = float (input("Quantos kms do carro percorreu?"))
dias = int (input('Quantos dias o carro ficou com o cliente?'))
pagardia = dias * 60
kmrodado = kms * 0.15
total = (dias * 60) + (kms * 0.15)
print ('O carro percorreu {} kms, e ficou {} dias com o cliente, ficando um total a pagar de: R$ {:.2f}'.format (kms, dias, total))
