# -*- coding: utf-8 -*-


def nota_quices(codigo, n1, n2, n3, n4, n5):
    p1 = min(n1, n2, n3, n4, n5)
    promedio = round((n1 + n2 + n3 + n4 + n5 - p1) / 4*5/100 , 2)
    return f"El promedio del estudiante {codigo} es: {promedio}"