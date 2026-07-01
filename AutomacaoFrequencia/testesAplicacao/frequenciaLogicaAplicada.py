#importando as bibliotecas
import pandas as pd #para fazer o tratamento dos dados
import gspread #api for Google Sheets
from datetime import datetime #para manipular datas e horas
from google.oauth2.service_account import Credentials
from fpdf import FPDF #biblioteca para geracao de pdf
from fpdf.fonts import FontFace
from gerarListaPresenca_pdf import PDF


#criando as credenciais e autorizando o acesso a planilha
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("automacao-frequencia.json", scopes=scopes)
client = gspread.authorize(creds)

#passando o id e carregando a planilha de respostas do formulario
sheet_id_respostas = "1QJx1_RRGDX8K7po4tuOd2SwryORAR0KVh7tARmJ-IoU"
sheetRespostas = client.open_by_key(sheet_id_respostas)
dataRespostas = sheetRespostas.sheet1.get_all_records() #carrega todos os registros do Google Sheets com as respostas
dataFrameRespostas = pd.DataFrame(dataRespostas) # Converter os dados para um DataFrame do pandas
#print("Dados Respostas do Forms:\n{}".format(dataFrameRespostas.head())) #imprimindo o dataFrame. semelhante a `print("Dados carregados:")print(dataFrameAlunosCadastrados.head()))`

# Carregar planilha de alunos cadastrados
sheet_id_alunosCadastrados = "1KiYU5Ay2QWV4wNINwzXbI6kPDiHWhJpoL3YeNGTPpik"
sheetAlunosCadastrados = client.open_by_key(sheet_id_alunosCadastrados)
dataAlunosCadastrado = sheetAlunosCadastrados.sheet1.get_all_records() #carrega todos os registros do Google Sheets com os emails dos alunos da aula
dataFrameAlunosCadastrados = pd.DataFrame(dataAlunosCadastrado) # Converter os dados para um DataFrame do pandas
#print("Dados dos Alunos Cadastrados na Disciplina:\n{}".format(dataFrameAlunosCadastrados.head())) #imprimindo o dataFrame

# Filtrar e-mails autorizados
emails_cadastrados = dataFrameAlunosCadastrados["Email"].tolist()  # Obter lista de e-mails cadastrados

#manipulando a data e a hora para verificar se o aluno preencheu no horario da aula
dataFrameRespostas["Data"] = pd.to_datetime(dataFrameRespostas["Data da aula de hoje"], format="%d/%m/%Y").dt.date #Converter a nova coluna "Data" para datetime (apenas data)
dataFrameRespostas["Data e Hora"] = pd.to_datetime(dataFrameRespostas["Carimbo de data/hora"], format="%d/%m/%Y %H:%M:%S") # Converter a coluna "Carimbo de data/hora" para datetime completo
dataFrameRespostas["Hora"] = dataFrameRespostas["Data e Hora"].dt.time # Extrair apenas a hora
dataFrameRespostas = dataFrameRespostas.drop(columns=["Data e Hora"]) # Remover a coluna "Data e Hora" por ser redundante
dataFrameRespostas = dataFrameRespostas.drop(columns=["Carimbo de data/hora"]) # Remover a coluna "Carimbo de data/hora" por ser redundante
hora_inicio = datetime.strptime("19:00", "%H:%M").time() # Definir intervalo de horário da aula
hora_fim = datetime.strptime("22:00", "%H:%M").time() # Definir intervalo de horário da aula
df_horario_valido = dataFrameRespostas[(dataFrameRespostas["Hora"] >= hora_inicio) & (dataFrameRespostas["Hora"] <= hora_fim)] # Filtrar respostas pelo horário
df_final = df_horario_valido[df_horario_valido["Endereço de e-mail"].isin(emails_cadastrados)] # Filtrar respostas por e-mails autorizados

df_final = df_final.astype(str) # Converter todas as colunas do DataFrame para strings
#print("Respostas válidas no horário e com e-mails cadastrados:\n {}".format(df_final)) #imprimindo o dataFrame

# (Opcional) Exibir as respostas válidas no dia
print("Respostas válidas no horário e data da aula:")
print(df_horario_valido)

print("Respostas válidas no final:")
print(df_final)


# Gerenciar a aba "PresencaConfirmada"
worksheet_list = map(lambda x: x.title, sheetRespostas.worksheets())
newWorksheetName = "PresencaLogicaAplicada"


#criar uma nova aba para "PresencaConfirmada" caso ainda nao tenha
if newWorksheetName in worksheet_list: #verifica se ela ja estna na lista de abas criadas
    sheetPresencaConfirmada = sheetRespostas.worksheet(newWorksheetName)
    print("Ja criada")
else:
    sheetPresencaConfirmada = sheetRespostas.add_worksheet(newWorksheetName, rows=50, cols=10)
    print("Criou")


# Converter DataFrame em lista de listas e atualizar
sheetPresencaConfirmada.clear()
dados_para_atualizar = [df_final.columns.tolist()] + df_final.values.tolist()
sheetPresencaConfirmada.update(f"A1", dados_para_atualizar)
sheetPresencaConfirmada.format("A1:E1", {"textFormat": {"bold": True}})
print("Dados atualizados na aba 'PresencaConfirmada'")

# Dados para o cabeçalho
disciplina = "CSIP0002 - TÓPICOS ESPECIAIS DE AUTOMAÇÃO"
turma = "01 (46 alunos)"
horario = "7M2345"
docente = "JARIO JOSE DOS SANTOS JUNIOR"
ano_semestre = "2024.1"
dataAula = "23/11/2024"

# Criar o PDF com os dados validados
data = df_final.values.tolist()  # Dados para a tabela
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_dados_disciplina(disciplina, turma, horario, docente, ano_semestre, dataAula)

pdf.add_table(data)  # Adicionar a tabela no PDF

# Salvar o PDF
output_path = "presencaLogicaAplicada.pdf"
pdf.output(output_path)
print(f"PDF gerado e salvo como: {output_path}")