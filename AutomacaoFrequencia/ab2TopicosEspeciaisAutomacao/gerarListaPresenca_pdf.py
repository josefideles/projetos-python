from fpdf import FPDF
from fpdf.fonts import FontFace
from datetime import datetime #para manipular datas e horas

class PDF(FPDF):
    def header(self):
        # Criar uma borda ao redor de todo o cabeçalho
        self.set_xy(10, 10)  # Posição inicial do cabeçalho
        self.set_line_width(0.3)  # Espessura da linha da borda
        self.rect(10, 10, 200, 26)  # Retângulo: (x, y, largura, altura)

        # Adicionando o logotipo e título
        self.image('logo_ufal.png', 12, 10, 25)  # Logotipo no canto superior esquerdo
        
        # Título central
        self.set_font('Arial', 'B', 10)
        self.set_xy(35, 12)  # Posição para começar o texto central
        self.cell(0, 7, 'UNIVERSIDADE FEDERAL DE ALAGOAS', border=0, ln=True, align='C')
        self.cell(0, 7, 'SISTEMA INTEGRADO DE GESTÃO DE ATIVIDADES ACADÊMICAS', border=0, ln=True, align='C')

        # Exibe a data e hora de emissão
        emitido_em = datetime.now().strftime("EMITIDO EM %d/%m/%Y %H:%M")
        self.cell(0, 7, emitido_em, border=0, ln=True, align='C')

        # Linha adicional para o título da lista
        self.ln(10)
        self.set_font('Arial', 'B', 12)
        self.cell(190, 5, 'LISTA DE ALUNOS PRESENTES', border=0, ln=True, align='C')
        self.ln(10)

    def add_dados_disciplina(self, disciplina, turma, horario, docente, ano_semestre, dataAula):
        # Criar uma borda ao redor dos dados da disciplina
        # Ajustar posição para evitar sobreposição
        y_inicio = self.get_y()  # Pega a posição atual para calcular
        altura_retangulo = 20  # Altura total do bloco
        self.rect(10, y_inicio, 190, altura_retangulo)

        # Inserir os dados da disciplina no formato solicitado
        self.set_font('Arial', '', 10)
        self.set_xy(12, y_inicio +2)  # Posição inicial do texto. E Adicionar margem interna
        self.cell(0, 5, f"Disciplina: {disciplina}   Ano/Semestre: {ano_semestre}", ln=True)
        self.cell(0, 5, f"Turma: {turma}   Horário: {horario}   Data: {dataAula}", ln=True)
        self.cell(0, 5, f"Docente: {docente}", ln=True)
        self.ln(10)  # Espaço após o bloco de informações da disciplina

    def footer(self):
        # Adicionando o número da página no rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='R')

    def add_table(self, data):

        self.set_font('Arial', '', 8)

        # Configuração das colunas e centralização
        col_widths = [50, 50, 30, 30]
        header = ['Email', 'Nome', 'Matrícula', 'Data']
        
        self.set_fill_color(192, 192, 192)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 9)

        # Posição inicial da tabela
        self.ln(10)  # Espaço entre o cabeçalho e a tabela
        x_start = (self.w - sum(col_widths)) / 2
        self.set_x(x_start)

        # Cabeçalhos
        for col_width, header_text in zip(col_widths, header):
            self.cell(col_width, 10, header_text, border=1, align='C', fill=True)
        self.ln()

        # Linhas da tabela
        self.set_font('Arial', '', 8)
        for row in data:
            self.set_x(x_start)
            for col_width, cell_value in zip(col_widths, row):
                self.cell(col_width, 8, str(cell_value), border=1, align='C')
            self.ln()