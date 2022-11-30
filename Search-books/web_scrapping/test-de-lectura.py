from xlrd import open_workbook
import xlrd
import openpyxl
import pandas as pd

archivo = "/mnt/d/Github/Search-books/web_scrapping/links.xlsx"

# openFile = xlrd.open_workbook(archivo)
# sheet = openFile.sheet_by_name('sectionts')
# print(sheet.nrows)
# print(sheet.ncols)

#data_only=True es para escoger solo el resultado de las formulas
book = openpyxl.load_workbook(archivo, data_only=True)
hoja = book.active

celdas = hoja['B2':'B8']

print(celdas)

for fila in celdas:
    print([celdas.value for celdas in fila])
    

# print("No de filas", sheet.nrows)
# df = pd.read_excel(archivo, sheet_name='sectionts')
# print(df.loc[:, 'Links'])