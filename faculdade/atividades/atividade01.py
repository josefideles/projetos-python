'''Crie um programa que peça ao usuário para inserir a sua idade
e verifique se ele é de menor de idade, adulto ou idoso'''

age = int(input('Insira a sua idade: '))

if age < 18:
    print('Você ainda é menor de idade!')
elif age < 60:
    print('Você já está na fase adulta!')
else:
    print('Você já está velhor, já é um idoso!')