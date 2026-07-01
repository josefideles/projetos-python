value = float(input('Insira o valor do automóvel desejado: '))
wage = float(input('Insira o seu salário atual: '))
year = float(input('Em quantos anos você pretende pagar as parcelas do automóvel: '))

profit = value*1.22 #profit = lucro
installments = profit/(year*12)
payments = profit/installments

approved = 'O seu financiamento foi concedido!'
denied = 'O seu financiamento foi negado!'
text = 'Parcelas excedem 30% do seu salário. Valor da parcela {}.'.format(payments)

if payments <= 0.30*value:
    print(approved)
else:
    print(text)
    print(denied)


