import pandas as pd
#from openpyxl import Workbook
#arquivo_excel = Workbook()
import gspread
import numpy as np
import datetime
import xlrd
"""
planilha1 = arquivo_excel.active
planilha1.title = "Gastos"
planilha2 = arquivo_excel.create_sheet("Ganhos")
planilha2 = arquivo_excel.create_sheet("Ganhos", 0)
print(arquivo_excel.sheetnames)
planilha1['A1'] = 'Categoria'
planilha1['B1'] = 'Valor'
planilha1['A2'] = "Restaurante"
planilha1['B2'] = 45.99
valores = [
    ("Código", "Valor"),
    ("GGBR4", '=RTD("rtdtrading.rtdserver";; $A4; "ULT")'),
    ("B3SA3", '=RTD("rtdtrading.rtdserver";; $A5; "ULT")'),
    ("VALE3", '=SOMA(23, 5)')
]
for linha in valores:
    planilha1.append(linha)
planilha1.cell(row=3, column=1, value=34.99)
planilha1['C1'] = '=SOMA(23, 5)'
arquivo_excel.save("relatorio.xlsx")

#df1 = pd.DataFrame([['GGBR4', '=RTD("rtdtrading.rtdserver";; $B2; "ULT")'], ['B3SA3', 'RTD("rtdtrading.rtdserver";; $B3; "ULT)']],
#                   index=['row 1', 'row 2'],
#                   columns=['Código', 'col 2'])
#df1.to_excel("output.xlsx")



#df1.to_excel("output.xlsx", sheet_name='Sheet_name_1')

#CarteiraBova11 = pd.read_csv("C:/Users/tamar/Downloads/Bova11_teste.csv", encoding='utf-8', sep=';', header=10, usecols=['Preço', 'Cotas'], skipfooter=3)
#print(CarteiraBova11) , engine='openpyxl'

#Excel_Trader = pd.read_excel("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/BOVA11_DAYTRADE.xlsx", sheet_name = "BOVA11", header=10, usecols=['Último_Preço'])#, 47])
#print(Excel_Trader)

                # Linha , Coluna, 'O qua vai ser alterado'
#Excel_Trader.update_cell(1,2, '=RTD("rtdtrading.rtdserver";; $A1; "ULT")') #update_cell: pelos números da linha e coluna
#Excel_Trader.update_acell('f2', 10)


#Excel_Trader = pd.read_excel("C:/Users/tamar/Downloads/excel_trader.xlsx") #, sheet_name='Shee1')  # usecols=['Preço', 'Cotas'], skipfooter=3)  # usecols=["Código", "Cotas"])
#print(Excel_Trader)
#x = xlrd.open_workbook('C:/Users/tamar/Downloads/excel_trader.xls')
#p = x.sheet_by_name('Planilja1')

import pandas as pd

# RTD("rtdtrading.rtdserver";; $C9; "ULT")
# 1) Abrindo a Arquivo a partir da 11 linha
#CarteiraBova11 = pd.read_csv("C:/Users/tamar/Downloads/Bova11_teste.csv", encoding='utf-8', sep=';', header=10)
#print(CarteiraBova11)

Excel_Trader = pd.read_excel("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/BOVA11_DAYTRADE.xlsx", sheet_name = "BOVA11", header=10, usecols=['Último_Preço'], skipfooter=3)#, 47])
print(Excel_Trader)



# 2) Abrindo o arquivo e exibindo apenas a colona do Código e Cotas
# encoding = Lendo em Portugues. sep = Passar o conteudo apos , para coluna. header = Define a linha onde começa o arquivo, usecols = Pega as colunas especificas. nrows = Lê só o numero de linhas especificado
CarteiraBova11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", encoding='utf-8', sep=',', header=10, usecols=['Preço', 'Cotas'], skipfooter=3)#usecols=["Código", "Cotas"])
print(CarteiraBova11)

# 5) ou 1) Lendo o arquivo
# encoding = Lendo em Portugues. sep = Passar o conteudo apos , para coluna. header = Define a linha onde começa o arquivo, usecols = Pega as colunas especificas. nrows = Lê só o numero de linhas especificado
#CarteiraBova11 = pd.read_csv("C:/Users/tamar/Downloads/Bova11_teste.csv", encoding='utf-8', sep=';', header=11)
#print(CarteiraBova11)

# 7) Pegando uma coluna especifica e trocando as virguras por pontos
CarteiraBova11['Preço'] = CarteiraBova11['Preço'].apply(lambda x: str(x).replace(",","."))
print(CarteiraBova11['Preço'])

# 8) Convetento para Numero
# create a dataframe
df = pd.DataFrame(CarteiraBova11['Preço'])
# show the dataframe
print(df)
# converting each value of column to a string
CarteiraBova11['Preço'] = pd.to_numeric(CarteiraBova11['Preço'], errors = 'coerce')

# 9) Esta etapa não é tão nescessário porem vamos fazer pois ela já remove mais um valor,
# no primeiro removeu o Winfutv e agora remove a GOLL4
CarteiraBova11['Preço'] = CarteiraBova11['Preço'].astype('float64')
print(CarteiraBova11['Preço'])

preco = CarteiraBova11['Preço']
print(f"preço fina: \n {preco}")

CarteiraBova11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", encoding='utf-8', sep=',', header=10, skipfooter=3)
print(CarteiraBova11)

# 13) Pegando a coluna Cotas e removendo as virgulas e já converte e floate
#CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.', '').str.replace(',', '.').astype("float")
CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.', '').str.replace(',', '.').astype("float")
#CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.', '').str.replace(',', '.').astype("float")
#CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].astype(str)
#CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.0', ' ')

print(CarteiraBova11['Cotas'])

cotas = CarteiraBova11['Cotas']
print(f"Cotas final: \n{cotas}")

CarteiraBova11['Preco_Cotas'] = preco * cotas

preco_cotas = CarteiraBova11['Preco_Cotas']
soma_preco_cotas = preco_cotas.sum()
print(soma_preco_cotas)

# 16) Abrindo Arquivo csv na coluna e linha especifica, e salvando em uma variavel
# encoding = Lendo em Portugues. sep = Passar o conteudo apos , para coluna. header = Define a linha onde começa o arquivo, usecols = Pega as colunas especificas. nrows = Lê só o numero de linhas especificado
Titulo = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=3, nrows=1, usecols=[1])
Titulo_Valor_Base = Titulo['28 nov 2008'].sum()
print(Titulo_Valor_Base)


Valor_Base_Calculo_BOVA11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=4, nrows=1, usecols=[1])
Valor_Base_Calculo_BOVA11
print(Valor_Base_Calculo_BOVA11)

Valor_Base_Calculo_BOVA11[Titulo_Valor_Base] = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].str.replace('.', '').str.replace(',', '.').astype("float")
#Valor_Base_Calculo_BOVA11['13.593.294.302,58'] = Valor_Base_Calculo_BOVA11['13.593.294.302,58'].apply(lambda x: str(x).replace(".",","))
print(Valor_Base_Calculo_BOVA11[Titulo_Valor_Base])

#base = Valor_Base_Calculo_BOVA11
#Valor_Base = pd.DataFrame(data=base, columns=['Base'])
#print(Valor_Base)


# 17) Removendo caracter ponto e virgula da string
novo = "115.150.000,00"
#novo = Valor_Base_Calculo_BOVA11
b = ".,"
for i in range(0,len(b)):
  novo= novo.replace(b[i],"")
print(novo)

# 18) Criando uma coluna com o novo valor para tranformalo e DataFrame
base = [novo]
Valor_Base = pd.DataFrame(data=base, columns=['Base'])
print(Valor_Base)

Valor_Base['Base'] = Valor_Base['Base'].str.replace('.', '').str.replace(',', '.')
Valor_Base['Base'] = Valor_Base['Base'].apply(lambda x: str(x).replace(",","."))
print(Valor_Base['Base'])


# create a dataframe
df = pd.DataFrame(Valor_Base['Base'])
# show the dataframe
print (df)
# show the datatypes
print(df.dtypes)
# converting each value of column to a string
Valor_Base = pd.to_numeric(Valor_Base['Base'], errors = 'coerce') 

valor_base = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base]
valor_base = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].sum()
print(valor_base)

Valor_Real = soma_preco_cotas/valor_base
print(Valor_Real)
print('Valor Real:  \n R$ {:.2f}'.format(Valor_Real))

Valor_Base = Valor_Base[0]
print(Valor_Base)

Valor_Real = soma_preco_cotas/Valor_Base
print(Valor_Real)
"""

df = pd.DataFrame({'name': ['GGBR4', '=RTD("rtdtrading.rtdserver";; $B2; "ULT")'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
df.to_csv(index=False)

#compression_opts = dict(method='zip', archive_name='out.csv')
#df.to_csv('out.zip', index=False, compression=compression_opts)

import pandas as pd
nome = ['GGBR4', 'João', 'Daniel', 'GGBR4']
idade = ['=RTD("rtdtrading.rtdserver";; $A1; "ULT")', 38, 24,'=RTD("rtdtrading.rtdserver";; $B2; "ULT")']
dados = {
'nome':nome,
'idade':idade
}
pessoas = pd.DataFrame(dados)
type(pessoas)
#<class 'pandas.core.frame.DataFrame'>
pessoas

pessoas.to_csv('pessoas.csv')