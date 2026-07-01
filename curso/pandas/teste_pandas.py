import pandas as pd
import openpyxl
planilha = pd.read_excel('dados.xlsx')
print(planilha.shape)
print(planilha.size)
print(planilha.columns)
print(planilha.head())
print(planilha.tail())
print(planilha.isnull())
print(planilha)