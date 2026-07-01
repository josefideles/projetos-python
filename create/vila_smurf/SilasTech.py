'''Desafio: Vamos criar um programa em Python que permita 
calcular não apenas o salário reajustado para um único funcionário, 
mas que também possa lidar com o reajuste salarial para um grupo de funcionários
com diferentes cargos e níveis salariais. 
Além disso, queremos que o programa aceite diferentes percentagens de reajuste para cada grupo de funcionários.'''

class Funcionários:
    def __init__(self, nome, salario, reajuste):
        self.nome = nome
        self.salario = salario
        self.reajuste = reajuste

funcionario = Funcionários(input('Digite o nome do funcionário', input('\nDigite o salário para ter o reajuste',)))
