'''Faça um programa que leia um valor flutuante
e mostre ma tela somente a parte inteira do número'''

import math
number = float(input('Write a number to remove the decimal part: '))
print(math.trunc(number))