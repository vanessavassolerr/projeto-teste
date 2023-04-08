import openpyxl
from openpyxl import Workbook

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('Base de Imoveis')
sheet_vagas = workbook['Dados Imoveis']
sheet_vagas.append(['ID', 'Rua', 'Numero', 'Complemento', 'Descricao Geral'])

continuar = 's'
while continuar=='s':
        id = input('ID: ')
        rua = input('Rua: ')
        numero = input('Numero: ')
        descricao_geral = input ('Descricao Geral: ')
        sheet_vagas.append([id, rua, numero, descricao_geral])
        continuar = input('Deseja continuar? (s ou n): ')

workbook.save('Base Imoveis.xlsx')