import openpyxl as op

libro = op.load_workbook("clase_23agosto.xlsx")

Datos = libro.active

for row in Datos.iter_rows(min_row=1, max_col=5, max_row=5):
    for cell in row:
        print(cell)