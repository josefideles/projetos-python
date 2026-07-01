from fpdf import FPDF
from fpdf.fonts import FontFace

class PDF(FPDF):
    def header(self):
        # Adicionando o logotipo e título
        self.image('logo_ufal.png', 8, 8, 25)  # Logotipo no canto superior esquerdo
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, 'UNIVERSIDADE FEDERAL DE ALAGOAS', border=False, ln=True, align='C')
        self.cell(0, 5, 'SISTEMA INTEGRADO DE GESTÃO DE ATIVIDADES ACADÊMICAS', border=False, ln=True, align='C')
        self.cell(0, 5, 'LISTA DE FREQUÊNCIA', border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        # Adicionando o número da página no rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='R')

    def add_table(self, data):
        # Adicionando tabela com os dados
        self.set_font('Arial', '', 8)

        # Configurando estilos de cabeçalho
        blue = (0, 0, 255)
        grey = (192, 192, 192)
        headings_style = FontFace(emphasis="BOLD", color=blue, fill_color=grey)

        # Configurando largura total da tabela
        total_width = 160  # Ajuste para centralizar na página
        page_width = self.w - 2 * self.l_margin
        x_start = (page_width - total_width) / 2  # Calcula a posição inicial para centralizar

        # Configuração das colunas
        col_widths = [50, 50, 30, 30]  # Ajuste das larguras das colunas
        header = ['Email', 'Nome', 'Matrícula', 'Data']

        # Configurando o cabeçalho da tabela
        self.set_fill_color(*grey)  # Cor de fundo do cabeçalho
        self.set_text_color(*blue)  # Cor do texto do cabeçalho
        self.set_font('Arial', 'B', 9)  # Fonte do cabeçalho

        # Movendo para posição inicial da tabela
        self.set_x(x_start)

        # Cabeçalhos da tabela
        for col_width, header_text in zip(col_widths, header):
            self.cell(col_width, 10, header_text, border=1, align='C', fill=True)  # Estilizando com preenchimento
        self.ln()  # Próxima linha

        # Resetando estilos para as células normais
        self.set_fill_color(240, 240, 240)  # Fundo das células alternadas
        self.set_text_color(0, 0, 0)  # Cor do texto padrão
        self.set_font('Arial', '', 8)  # Fonte padrão

        # Linhas da tabela
        for i, row in enumerate(data):
            self.set_x(x_start)  # Centralizar cada linha
            for col_width, cell_value in zip(col_widths, row):
                self.cell(col_width, 8, str(cell_value), border=1, align='C', fill=(i % 2 == 0))  # Fundo alternado
            self.ln()  # Próxima linha

# Criar o PDF com os dados validados
data = [
    ["user1@example.com", "João Silva", "20210001", "21/11/2024"],
    ["user2@example.com", "Maria Lima", "20210002", "21/11/2024"],
    ["user3@example.com", "Pedro Santos", "20210003", "21/11/2024"],
    ["user4@example.com", "Ana Souza", "20210004", "21/11/2024"],
]  # Exemplo de dados

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_table(data)  # Adicionar a tabela no PDF

# Salvar o PDF
output_path = "presencaLogicaAplicada.pdf"
pdf.output(output_path)
print(f"PDF gerado e salvo como: {output_path}")

"""# Classe personalizada para criação do PDF
class PDF(FPDF):
    def header(self):
        # Adicionando o logotipo e título
        self.image('logo_ufal.png', 8, 8, 25)  # Ajuste o caminho do logotipo (10, 8: Define a posição no canto superior esquerdo; 33: Define a largura da imagem.)
        self.set_font('Arial', 'B', 10) #Configura a fonte para o texto que será escrito (tipo, estilo e tamanho).
        self.cell(0, 5, 'UNIVERSIDADE FEDERAL DE ALAGOAS', border=False, ln=True, align='C')
        self.cell(0, 5, 'SISTEMA INTEGRADO DE GESTÃO DE ATIVIDADES ACADÊMICAS', border=False, ln=True, align='C')
        #self.cell(0, 10, 'EMITIDO EM {} {}', border=False, ln=True, align='C')
        self.cell(0, 5, 'LISTA DE FREQUÊNCIA', border=False, ln=True, align='C')
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
        with pdf.table(text_align="CENTER") as table:
            for row in data:
                for col_width, cell_value in zip(col_widths, row):
                    self.cell(col_width, 8, cell_value, border=1, align='C')
                self.ln()

        headings_style = fpdf.FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
        with pdf.table(
            borders_layout="NO_HORIZONTAL_LINES",
            cell_fill_color=(224, 235, 255),
            col_widths=(42, 39, 35, 42),
            headings_style=headings_style,
            line_height=6,
            text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
            width=160,
        ) as table:
            for data_row in data:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)"""