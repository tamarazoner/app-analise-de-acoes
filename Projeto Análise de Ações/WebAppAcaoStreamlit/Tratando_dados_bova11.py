import pandas as pd
import streamlit as st  # Daskboard

# Le arquivo Excel BOVA_TRADE e paga o valor em tempo real do Último preço de cada Ativo
CarteiraBova11 = pd.read_excel("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/BOVA11_DAYTRADE.xlsx", sheet_name = "BOVA11", header=10, usecols=['Último_Preço'], skipfooter=3)#, 47])

#print(CarteiraBova11)

# Transforma o Último Preço em string e muda a virgula para ponto
CarteiraBova11['Último_Preço'] = CarteiraBova11['Último_Preço'].apply(lambda x: str(x).replace(",","."))
#print(CarteiraBova11['Último_Preço'])

# Transforma o Último Preço em DataFrame Numerico
df = pd.DataFrame(CarteiraBova11['Último_Preço'])
CarteiraBova11['Último_Preço'] = pd.to_numeric(CarteiraBova11['Último_Preço'], errors = 'coerce')

# Transforma o Último Preço do DataFrame em Float64
CarteiraBova11['Último_Preço'] = CarteiraBova11['Último_Preço'].astype('float64')
#print(CarteiraBova11['Último_Preço'])

# Passa o Último Preço DataFrame float64 em uma outra variável
preco = CarteiraBova11['Último_Preço']
print(f"preço fina: \n {preco}")
st.write(f"preço fina: \n {preco}")

# Le arquivo CSV BOVA11_holdings que está no Google Dive e paga o valor das Cotas de cada Ativo
CarteiraBova11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", encoding='utf-8', sep=',', header=10, skipfooter=3)
#print(CarteiraBova11)

# Transforma Cotas em float e muda a virgula para ponto
CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.', '').str.replace(',', '.').astype("float")
#print(CarteiraBova11['Cotas'])

# Passa a Cotas DataFrame float em uma outra variável
cotas = CarteiraBova11['Cotas']
print(f"Cotas final: \n{cotas}")

# Faz a conta de multiplicação do ultimo preço x cotas e salva em uma nova coluna DataFrame de Preço_Cotas
CarteiraBova11['Preco_Cotas'] = preco * cotas
# Passa o Preço_Cotas DataFrame float em uma outra variável
preco_cotas = CarteiraBova11['Preco_Cotas']

# Soma a coluna preco_cotas e passa para uma outra variável
soma_preco_cotas = preco_cotas.sum()
print(soma_preco_cotas)

# Le arquivo CSV BOVA11_holdings que está no Google Dive e paga o titulo do valor base
Titulo = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=3, nrows=1, usecols=[1])
Titulo_Valor_Base = Titulo['28 nov 2008'].sum()
print(Titulo_Valor_Base)

# Le arquivo CSV BOVA11_holdings que está no Google Dive e paga a coluna do valor base
Valor_Base_Calculo_BOVA11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=4, nrows=1, usecols=[1])
Valor_Base_Calculo_BOVA11
print(Valor_Base_Calculo_BOVA11)

# Como temos agora o titulo da Coluna em uma variável, pegamos agora o valor base do DataFrame e tranformamos em float e muda a virgula para ponto
Valor_Base_Calculo_BOVA11[Titulo_Valor_Base] = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].str.replace('.', '').str.replace(',', '.').astype("float")
print(Valor_Base_Calculo_BOVA11[Titulo_Valor_Base])

# Passando o valor base em uma variável e mas antes somando ele para evitar erros
valor_base = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].sum()
print(valor_base)

# Dividindo a Soma do Preço das Cotas pelo Valor Base
Valor_Real = soma_preco_cotas/valor_base
print(Valor_Real)

# Exibindo o Valor Real da Carteira BOVA 11
print('Valor Real:  \n R$ {:.2f}'.format(Valor_Real))




