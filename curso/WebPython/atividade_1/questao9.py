'''A empresa SilasTech resolveu reajustar em 15% os salários dos seus colaboradores. 
Crie um programa que receba o salário antigo 
e imprima na tela o novo salário do funcionário já com o reajuste.
Reajustar o sarlário seria aumentar. Nesse caso, aumentar em 15%'''

salario = float(input('Insira o salário, em reais, do funcionário:\n'
                      'Obs: Para o cálculo só aceito o valor no padrão americano. No lugar de "," utilize o "." caso o valor seja decimal: '))

reajuste = salario*(115/100)
aumento = reajuste-salario

print('O seu salário era de R${}\n'
      'Você teve um aumento de R${:.2f}reais\n'
      'E o seu salário será R${:.2f}reais'
      .format(salario, aumento,reajuste))