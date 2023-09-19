import pandas as pd

df_books = pd.read_csv("C:/Users/sebas/OneDrive/Documentos/GitHub/ARCHIVOS-CLASES-PY-Y-PAG-WEB/Pandas-Numpy/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv")

print(df_books)

print(df_books[0:4])

print(df_books['Name'])

print(df_books[['Name','Author','Year']])

print(df_books.loc[:])

print(df_books.loc[0:4, ['Name', "Author"]])

print(df_books.loc[:, ['Reviews']] * -1)

print(df_books.loc[:, ['Author']] == 'JJ Smith')