preco = float(input('Digite o preço do produto: R$'))
desconto= preco - (preco * 5 / 100) #preco - 5%
print('O produto, com 5% de desconto custa: R${:.2f}'.format(desconto))
