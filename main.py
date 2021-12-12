import pandas as pd
vendas = pd.read_excel('Vendas.xlsx')
print(vendas.loc[vendas["ID Loja"] == 'Iguatemi Campinas'])