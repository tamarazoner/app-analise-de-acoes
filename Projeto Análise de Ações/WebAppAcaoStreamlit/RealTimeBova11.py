# Bibliotecas do Robô
import pandas as pd  # Le Arquivos
import streamlit as st  # Daskboard
#import date as np
import time
from datetime import datetime




# 1) Abrindo a Arquivo a partir da 11 linha
def RealTime():
   #import timetime
   #import nump
   # Nome do Página
    st.header('***BOVA11 em Tempo Real***')
    st.markdown("<h1 style='color:#F00;'>BOVA11 em Tempo Real</h1>", unsafe_allow_html=True)

    ####DADOS EXCEL

    # Le arquivo CSV BOVA11_holdings que está no Google Dive e paga o valor das Cotas de cada Ativo
    #CarteiraBova11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", encoding='utf-8', sep=',', header=10, skipfooter=3)


    CarteiraBova11 = pd.read_csv("G:/Meu Drive/CarteiraBova11/BOVA11_holdings.csv", encoding='utf-8',
                             sep=',', header=10, skipfooter=3)
    # print(CarteiraBova11)

    # Transforma Cotas em float e muda a virgula para ponto
    CarteiraBova11['Cotas'] = CarteiraBova11['Cotas'].str.replace('.', '').str.replace(',', '.').astype("float")
    # print(CarteiraBova11['Cotas'])

    # Passa a Cotas DataFrame float em uma outra variável
    cotas = CarteiraBova11['Cotas']
    # print(f"Cotas final: \n{cotas}")
    st.write(f"Cotas final: \n ")
    st.write(cotas)

    # Le arquivo CSV BOVA11_holdings que está no Google Dive e paga o titulo do valor base
    Titulo = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=3, nrows=1, usecols=[1])
    Titulo_Valor_Base = Titulo['28 nov 2008'].sum()
    # print(Titulo_Valor_Base)

    # Le arquivo CSV BOVA11_holdings que está no Google Dive e paga a coluna do valor base
    Valor_Base_Calculo_BOVA11 = pd.read_csv("C:/Users/tamar/Google Drive/CarteiraBova11/BOVA11_holdings.csv", sep=',', header=4, nrows=1, usecols=[1])
    Valor_Base_Calculo_BOVA11
    # print(Valor_Base_Calculo_BOVA11)
    st.write(f"Coluna Valor Base: \n ")
    st.table(Valor_Base_Calculo_BOVA11)

    # Como temos agora o titulo da Coluna em uma variável, pegamos agora o valor base do DataFrame e tranformamos em float e muda a virgula para ponto
    Valor_Base_Calculo_BOVA11[Titulo_Valor_Base] = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].str.replace('.', '').str.replace(',', '.').astype("float")
    # print(Valor_Base_Calculo_BOVA11[Titulo_Valor_Base])

    # Passando o valor base em uma variável e mas antes somando ele para evitar erros
    valor_base = Valor_Base_Calculo_BOVA11[Titulo_Valor_Base].sum()
    # print(valor_base)
    st.write(f"Valor Base: {valor_base}\n ")

    ###DADOS EXCEL

    tempo = time.time() + 60
    #while time.time() < tempo:
    for i in range(0, 2):
        ####DADOS EXCEL

        CarteiraBova11 = pd.read_csv("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/BOVA11_DAYTRADE.csv", encoding='utf-8', skipfooter=7,
                                     sep=';', usecols=['Último_Preço'], header=10)
        # print(CarteiraBova11)

        # Le arquivo Excel BOVA_TRADE e paga o valor em tempo real do Último preço de cada Ativo
        #CarteiraBova11 = pd.read_csv("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/BOVA11_DAYTRADE.csv", encoding='utf-8', sep=';', header=10, skipfooter=3)  # , 47])  sheet_name="BOVA11"
        # print(CarteiraBova11)

        # Transforma o Último Preço em string e muda a virgula para ponto
        CarteiraBova11['Último_Preço'] = CarteiraBova11['Último_Preço'].apply(lambda x: str(x).replace(",", "."))
        # print(CarteiraBova11['Último_Preço'])

        # Transforma o Último Preço em DataFrame Numerico
        df = pd.DataFrame(CarteiraBova11['Último_Preço'])
        CarteiraBova11['Último_Preço'] = pd.to_numeric(CarteiraBova11['Último_Preço'], errors='coerce')

        # Transforma o Último Preço do DataFrame em Float64
        CarteiraBova11['Último_Preço'] = CarteiraBova11['Último_Preço'].astype('float64')
        # print(CarteiraBova11['Último_Preço'])

        # Passa o Último Preço DataFrame float64 em uma outra variável
        preco = CarteiraBova11['Último_Preço']
        st.write(f"Preço final: \n ")
        st.write(preco)

        # Faz a conta de multiplicação do ultimo preço x cotas e salva em uma nova coluna DataFrame de Preço_Cotas
        CarteiraBova11['Preco_Cotas'] = preco * cotas

        # Passa o Preço_Cotas DataFrame float em uma outra variável
        preco_cotas = CarteiraBova11['Preco_Cotas']

        # Soma a coluna preco_cotas e passa para uma outra variável
        soma_preco_cotas = preco_cotas.sum()
        #print(soma_preco_cotas)
        st.write(f"Soma do Preço por Cotas: \n {soma_preco_cotas}")
        #st.table(f"Soma do Preço por Cotas: \n {soma_preco_cotas}")

        # Dividindo a Soma do Preço das Cotas pelo Valor Base
        Valor_Real = soma_preco_cotas / valor_base
        #print(Valor_Real)

        # Exibindo o Valor Real da Carteira BOVA 11
        #print('Valor Real:  \n R$ {:.2f}'.format(Valor_Real))
        st.write('Valor Real:  \n R$ {:.2f}'.format(Valor_Real))

        ####DADOS EXCEL
        st.write(f'Atualização : {i} de 10')

        time.sleep(0.5)
    st.write("\nFim")

if __name__ == "__main__":
    RealTime()

    #pd.to_csv("C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/My trades - Performance/Bova11.csv")

