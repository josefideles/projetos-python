'''Faça um programa que leia um valor em reais 
e converta esse valor para dólares (1 dólar = R$ 4,88)'''

valor = float(input('Digite um valor em reais (R$) para saber o valor em dólares ($): '))

dolar = 4.88
valor_dolar = valor/dolar

print('R$', valor, 'reais em dólares são:  $', valor_dolar, 'dólares')


