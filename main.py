import pandas as pd
vendas = pd.read_excel('Vendas.xlsx')
quant = vendas.loc[vendas["Quantidade"]>4]

campinas = vendas.loc[vendas["ID Loja"]=='Iguatemi Campinas']
campinasquant = campinas["Quantidade"].sum()
campinasvf = campinas["Valor Final"].sum()

Esplanada = vendas.loc[vendas["ID Loja"]=='Iguatemi Esplanada']
Esplanadaquant = Esplanada["Quantidade"].sum()
Esplanadavf = Esplanada["Valor Final"].sum()

Norte = vendas.loc[vendas["ID Loja"]=='Norte Shopping']
Nortequant = Norte["Quantidade"].sum()
Nortenasvf = Norte["Valor Final"].sum()

Bourbon = vendas.loc[vendas["ID Loja"]=='Bourbon Shopping SP']
Bourbonquant = Bourbon["Quantidade"].sum()
Bourbonvf = Bourbon["Valor Final"].sum()

Center = vendas.loc[vendas["ID Loja"]=='Center Shopping Uberlândia']
Centerquant = Center["Quantidade"].sum()
Centervf = Center["Valor Final"].sum()
  
f = open('resumo.txt','w')
arq = ['superaram 5 unidades de vendas',quant,'',''
,'    Iguatemi Campinas vendas            : {}..unidades'.format(campinasquant)
,'    Iguatemi Campinas valor final       : R$ {}'.format(campinasvf),''
,'    Iguatemi Esplanada vendas           : {}..unidades'.format(Esplanadaquant)
,'    Iguatemi Esplanada valor final      : R$ {}'.format(Esplanadavf),''
,'    Norte Shopping vendas               : {}..unidades'.format(Nortequant)
,'    Norte Shopping valor final          : R$ {}'.format(Nortenasvf),''
,'    Bourbon Shopping SP vendas          : {}..unidades'.format(Bourbonquant)
,'    Bourbon Shopping SP valor final     : R$ {}'.format(Bourbonvf),''
,'Center Shopping Uberlândia vendas       : {}..unidades'.format(Centerquant)
,'Center Shopping Uberlândia valor final  : R$ {}'.format(Centervf),'']
with open('resumo.txt','w')as arquivo:
    for x in arq:
        arquivo.write(str(x)+'\n')
f.close()