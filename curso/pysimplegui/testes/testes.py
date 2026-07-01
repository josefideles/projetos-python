#nome = input ('Digite o seu nome:')
#oi = 'Hello, '
#print(oi + nome)

print('Cálculos Matemáticos')
print("")
print('1º Resolva os cálculos a seguir:')
print('')

n1 = 7
n2 = 5
n3 = 3

a1 = print('a)', n1, '+', n2, '=')
a1r = int(input('Digite o resultado da soma: '))  #está convertendo para inteiro porque quando eu inserir o valor será atribuido como str
if a1r == (12):
    print('CERTO')
else:
   print('ERRADO')
soma = n1+n2
print('O resultado do cálculo é: ', soma)
print('')
subtr = n1-n2
b1 = print('b)', n1, '-', n2, '=')
b1r_str = input()
b1r = int(input('Digite o resultado da subtração: '))
b1r_str = input()
if b1r == 2:
    print ('CERTO')
else:
    print('ERRADO')
print('O resultado da subtração é: ', subtr)


