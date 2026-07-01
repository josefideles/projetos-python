'''Crie um código que determine (imprima)
se um dado número N inteiro (recebido através do teclado)
é PAR ou ÍMPAR'''

number = int(input('Digite um número inteiro para saber se ele é PAR ou ÍMPAR: '))

if number%2 == 0:
    print('O {} é um número par'.format(number))
else:
    print('O seu número {} é um número ímpar'.format(number))