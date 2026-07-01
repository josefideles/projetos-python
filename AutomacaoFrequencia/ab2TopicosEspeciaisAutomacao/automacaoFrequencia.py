import pandas as pd
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
from fpdf import FPDF
from gerarListaPresenca_pdf import PDF

class AutomacaoFrequencia:
    def __init__(self):
        self.dataFrameAlunosCadastrados = None
        self.dataFrameRespostas = None
        self.df_final = None
        self.sheetRespostas = None

    def criar_credenciais_api(self):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file("automacao-frequencia.json", scopes=scopes)
        client = gspread.authorize(creds)

        sheet_id_respostas = "1HoguuPZzMe7pdqyCkf295a-j5U8uZKtx3f2A7iDDA0Y"
        self.sheetRespostas = client.open_by_key(sheet_id_respostas)
        dataRespostas = self.sheetRespostas.sheet1.get_all_records()
        self.dataFrameRespostas = pd.DataFrame(dataRespostas)

        sheet_id_alunosCadastrados = "1KiYU5Ay2QWV4wNINwzXbI6kPDiHWhJpoL3YeNGTPpik"
        sheetAlunosCadastrados = client.open_by_key(sheet_id_alunosCadastrados)
        dataAlunosCadastrado = sheetAlunosCadastrados.sheet1.get_all_records()
        self.dataFrameAlunosCadastrados = pd.DataFrame(dataAlunosCadastrado)

    def validar_dados(self):
        emails_cadastrados = self.dataFrameAlunosCadastrados["Email"].tolist()

        self.dataFrameRespostas["Data"] = pd.to_datetime(self.dataFrameRespostas["Data da aula de hoje"], format="%d/%m/%Y").dt.date
        self.dataFrameRespostas["Data e Hora"] = pd.to_datetime(self.dataFrameRespostas["Carimbo de data/hora"], format="%d/%m/%Y %H:%M:%S")
        self.dataFrameRespostas["Hora"] = self.dataFrameRespostas["Data e Hora"].dt.time
        self.dataFrameRespostas = self.dataFrameRespostas.drop(columns=["Data e Hora", "Carimbo de data/hora"])

        hora_inicio = datetime.strptime("19:00", "%H:%M").time()
        hora_fim = datetime.strptime("22:00", "%H:%M").time()

        df_horario_valido = self.dataFrameRespostas[(self.dataFrameRespostas["Hora"] >= hora_inicio) & (self.dataFrameRespostas["Hora"] <= hora_fim)]
        self.df_final = df_horario_valido[df_horario_valido["Endereço de e-mail"].isin(emails_cadastrados)].astype(str)

    def atualizar_aba_presenca(self):
        worksheet_list = [worksheet.title for worksheet in self.sheetRespostas.worksheets()]
        newWorksheetName = "PresencaLogicaAplicada"

        if newWorksheetName in worksheet_list:
            sheetPresencaConfirmada = self.sheetRespostas.worksheet(newWorksheetName)
        else:
            sheetPresencaConfirmada = self.sheetRespostas.add_worksheet(newWorksheetName, rows=50, cols=10)

        sheetPresencaConfirmada.clear()
        dados_para_atualizar = [self.df_final.columns.tolist()] + self.df_final.values.tolist()
        sheetPresencaConfirmada.update("A1", dados_para_atualizar)
        sheetPresencaConfirmada.format("A1:E1", {"textFormat": {"bold": True}})

    def gerar_pdf(self):
        disciplina = "CSIP0002 - TÓPICOS ESPECIAIS DE AUTOMAÇÃO"
        turma = "01 (46 alunos)"
        horario = "7M2345"
        docente = "JARIO JOSE DOS SANTOS JUNIOR"
        ano_semestre = "2024.1"
        dataAula = "23/11/2024"

        data = self.df_final.values.tolist()
        pdf = PDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_dados_disciplina(disciplina, turma, horario, docente, ano_semestre, dataAula)
        pdf.add_table(data)

        output_path = "presencaLogicaAplicada.pdf"
        pdf.output(output_path)
        print(f"PDF gerado e salvo como: {output_path}")

    def executar(self):
        self.criar_credenciais_api()
        self.validar_dados()
        self.atualizar_aba_presenca()
        self.gerar_pdf()

if __name__ == "__main__":
    automacao = AutomacaoFrequencia()
    automacao.executar()