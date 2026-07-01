'''Fazer um código para inserir um mes 
e me entregar o numero de dias desse mes
e qual o mês que foi escolhido de acordo com o número de meses do ano'''
import pandas
from ex02 import contador

year = pandas.DataFrame({
    'Número': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
})
month = int(input('Digite o número de um mês do ano para saber a quantidade de dias: '))
if month in year['Número'].values:
    month_select = year.loc[year['Número'] == month, 'Mês'].values[0]     #nunca esquecer de passar a tabela e especificar o nome da linha para procurar. nesse caso especificar que e para localizar dento de 'year', em 'year' o 'Número'
    print("Você escolheu o mês {}".format(month_select))

#concluir o códico com uma importação do ex02.py