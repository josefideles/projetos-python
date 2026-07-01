'''Crie um programa de finaniamento de um automóvel.
Para isso, peça para o usuário digiar o valor do automóvel,
o salário do uuário e em quantos anos el deseja pagar.
Seu programa deve calcular uma margem de lucro de 22% para a loja do automóve e,
após isso, autorizar o empréstimo caso o valor da parcela não ultrapasse 30% do valor do salário do usuário.
Caso o valor da parcela exceda os 30% será negado'''

welcome = '\nSeja bem vindo à concessionária do Simas. A SimasTurbo\n'
print(welcome)

value = float(input('Insira o valor do automóvel desejado: '))
if value <= 0:
    print('Você não pode inserir valores menores que 0!')
    value = float(input('Insira novamente o valor do automóvel desejado: '))
    wage = float(input('Insira o seu salário atual: '))
    year = float(input('Em quantos anos você pretende pagar as parcelas do automóvel: '))

    if wage%1 == 0:     #estou convertendo o valor de wage == salario, e convertendo para o tipo inteiro caso nao tenha valor decimal
        wage = int(wage)
    if value%1 == 0:
        value = int(value)
    if year%1 == 0:
        year = int(year)

    profit = value*1.22 #profit = lucro
    installment_value = wage*0.30
    installments = year*12
    payments = profit/installments

    approved = 'O seu financiamento foi concedido. Agora você tem que pagar para o Simas!!♥♥'
    denied = 'O seu financiamento foi negado. Você é liso, vai trabalhar para poder usar o negocinho do Simas!!☺☻'
    text = '\nO seu automóvel foi no valor de {} reais.\nO seu salário é no valor de {} reais.\nVocê escolheu {:.0f} anos para realizar o pagamento, e serão {:.0f} parcelas no valor de {:.2f} reais por mês\n'.format(value,wage, year, installments, payments)

    if payments <= installment_value:
        print(text)
        print(approved)
    else:
        print(text)
        print(denied)
else:
    print('oi')