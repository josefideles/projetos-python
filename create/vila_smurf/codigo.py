import pandas as pd
import openpyxl
import time

welcome = ("\nSeja bem vindo à Vilda dos Smur'f tintaria\n\nPara você saber quantos litros de tinta irá precisar, insira as informações a seguir:")
print(welcome)

altura = float(input('Digite a altura do seu mural: '))
largura = float(input('Digite a largura do seu mural: '))
area = altura*largura
qtd_tinta = area/2
lata_int = qtd_tinta//5
lata_float = qtd_tinta%5

if lata_float != 0:
    latas = lata_int+1
else:
    latas = lata_int

catalogo = pd.DataFrame({   #a estrutura estava dando erro porque nao estava com virgula, diferenciando os elementos
    'Número': [1, 2, 3, 4, 5, 6],
    'Cor': ['Branco', 'Cinza', 'Laranja', 'Azul', 'Verde', 'Preto'],
    'Valor por Litro': [7, 7, 10, 11, 11, 12]
})
print('\nA área do seu mural é de {} Metros quadrados \nCom 1L de tinta você consegue pintar 2 Metros quadrados. \nPara pintar o mural você irá precisar de {} Litros de tinta!'.format(area, qtd_tinta))
print('\n Irei te apresentar o catalogo de tintar para você escolher: \n\n{}'.format(catalogo))

tinta = (int(input('Qual a cor da tinta que você deseja?\nInsira o número da tinta que escolheu:')))

if tinta in catalogo['Número'].values:
    cor_escolhida = catalogo.loc[catalogo['Número'] == tinta, 'Cor'].values[0]
    val_cor = qtd_tinta * catalogo.loc[catalogo['Número'] == tinta, 'Valor por Litro'].values[0]
    print('Você escolheu a cor {} e irá precisar de {} latas de tintas.\nE p valor será de {}'.format(cor_escolhida, latas, val_cor))
else:
    print('Não temos esse produto em nosso estoque')