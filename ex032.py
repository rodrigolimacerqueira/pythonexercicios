from datetime import date
ano = int (input('Digite o ano, ou tecle 0 para ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano == 400:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format (ano))
