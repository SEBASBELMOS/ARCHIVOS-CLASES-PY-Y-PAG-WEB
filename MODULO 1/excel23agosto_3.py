import openpyxl as op

libro = op.Workbook()

hoja = libro.active

d = hoja.cell(row=4, column=2, value=20)

print(d.value)
libro.save("datosf.xlsx")