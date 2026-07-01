#importando as bibliotecas
import pandas as pd #para fazer o tratamento dos dados
import gspread #api for Google Sheets
from datetime import datetime #para manipular datas e horas
from google.oauth2.service_account import Credentials
from fpdf import FPDF #biblioteca para geracao de pdf

#criando as credenciais e autorizando o acesso a planilha
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("automacao-frequencia.json", scopes=scopes)
client = gspread.authorize(creds)

#passando o id e carregando a planilha de respostas do formulario
sheet_id_respostas = "1YrE7HWgu4jrC3ODWse_LANVh8OFfIV87W5UQ3JmXFrc"
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
hora_inicio = datetime.strptime("14:00", "%H:%M").time() # Definir intervalo de horário da aula
hora_fim = datetime.strptime("16:00", "%H:%M").time() # Definir intervalo de horário da aula
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
newWorksheetName = "PresencaConfirmada"


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

# Classe personalizada para criação do PDF
class PDF(FPDF):
    def header(self):
        # Adicionando o logotipo e título
        self.image('logo_ufal.png', 8, 8, 25)  # Ajuste o caminho do logotipo (10, 8: Define a posição no canto superior esquerdo; 33: Define a largura da imagem.)
        self.set_font('Arial', 'B', 10) #Configura a fonte para o texto que será escrito (tipo, estilo e tamanho).
        self.cell(0, 10, 'UNIVERSIDADE FEDERAL DE ALAGOAS', border=False, ln=True, align='C')
        self.cell(0, 10, 'SISTEMA INTEGRADO DE GESTÃO DE ATIVIDADES ACADÊMICAS', border=False, ln=True, align='C')
        self.cell(0, 10, 'EMITIDO EM {} {}', border=False, ln=True, align='C')
        self.cell(0, 10, 'LISTA DE FREQUÊNCIA', border=False, ln=True, align='C')
        '''self.cell: Adiciona uma célula (retângulo de texto). Os parâmetros são:
                0: Largura automática (ocupa toda a largura da página).
                10: Altura da célula.
                Texto: O texto a ser exibido.
                border=False: Define se haverá borda ao redor do texto.
                ln=True: Move para a próxima linha após imprimir o texto.
                align='C': Centraliza o texto.'''
        
        self.ln(10) #Adiciona uma linha em branco para espaçamento.

    def footer(self):   #O rodapé aparecerá automaticamente em todas as páginas.
        # Adicionando o número da página no rodapé
        self.set_y(-15) #Move o cursor 15 unidades acima do final da página (negativo indica distância da borda inferior).
        self.set_font('Arial', 'I', 8)  # Define a fonte como Arial, itálico, tamanho 8
        self.cell(0, 10, f'Página {self.page_no()}', align='C') #self.page_no(): Retorna o número da página atual.

    def add_table(self, data):  #adiciona uma tabela
        # Adicionando tabela com os dados
        self.set_font('Arial', '', 8)
        col_widths = [50, 50, 20, 20]  # Ajuste das larguras das colunas (Define as larguras das colunas da tabela. Aqui, 30 para a primeira coluna, 80 para a segunda, e assim por diante.)
        header = ['Email', 'Nome', 'Matricula', 'Data'] #Contém os nomes das colunas da tabela.

        # Cabeçalhos da tabela
        for col_width, header_text in zip(col_widths, header):
            self.cell(col_width, 10, header_text, border=1, align='C')
        self.ln()

        # Linhas da tabela
        for row in data:
            for col_width, cell_value in zip(col_widths, row):
                self.cell(col_width, 8, cell_value, border=1, align='C')
            self.ln()

# Criar o PDF com os dados validados
data = df_final.values.tolist()  # Dados para a tabela
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_table(data)  # Adicionar a tabela no PDF

# Salvar o PDF
output_path = "lista_presenca.pdf"
pdf.output(output_path)
print(f"PDF gerado e salvo como: {output_path}")