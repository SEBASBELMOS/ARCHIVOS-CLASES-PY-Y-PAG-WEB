import openpyxl as op

libro = op.Workbook()

hoja = libro.active

hoja["A4"] = "curso"
hoja["B4"] = 185 * 2

libro.save("datosf.xlsx")