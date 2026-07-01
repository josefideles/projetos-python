'''Crie um programa que peça ao usuário para inserir dous números
e diga qual deles é maior, ou se são iguais'''

number = float(input('Insira um número: '))
number2 = float(input('Insira outro número: '))
if number%1 == 0:       #estou criando uma condicao para eliminar os pontos flutuantes caso seja um numero inteiro
    number = int(number)
if number2%1 == 0:
    number2 = int(number2)
if number > number2:
    print(f" O número {number} é maior que o outro número")
elif number2 > number:
    print(f'O número {number2} é maior que o outro número')
else:
    print('Os números são iguais')

