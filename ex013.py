salario = float (input ('Digite o salario: R$'))
aumento = salario + (salario * 15 / 100)
print ('O salario de R${:.2f} com 15% de aumento, passa a ser R$ {:.2f}'.format (salario, aumento))
