'''Crie um programa que peça ao usuário para inserir dois números 
e verifique se o primeiro número é divisível pelo segundo'''

number1 = float(input('Insira um número para saber se ele é divisível pelo segundo número: '))
number2 = float(input('Insira o segundo número para ter a divisibilidade: '))
if number1%number2 == 0:
    if number1%1 == 0:
        number1 = int(number1)
    if number2%1 == 0:
        number2 = int(number2)
    print('O número {} é divisível por {}!\nE o valor da divisão é {:.0f}'.format(number1, number2, (number1/number2)))
    #print(f"O número {number1} é divisível pelo segundo número, o {number2}\nE o valor da divisão é {number1//number2}")
else:
    print('Os números não tem a divisão exata!!')