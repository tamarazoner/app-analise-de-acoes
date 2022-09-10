# ok - Abrindo no Chorme o App Web
# streamlit run webappacaostreamlit.py
# OKS
# pip install streamlit
# pip install gspread
# pip install matplotlib
# pip install bokeh
# pip install plotly
# pip install plot
# pip install sklearn
# pip install yfinance

# Biblioteca
import pandas as pd
from robotprovidesclosure import acao
from RealTimeBova11 import RealTime
from MACD import macd
from MetaTrader import Cotacao
from AnaliseComYahoo import Analise
import streamlit as st

# %%writefile app.py


st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione uma opção',
                                         ['Analise de Ações', 'Robô de Prever Intra Day de Ações', 'Real Time Bova11', 'MACD',
                                          'Cotação em Tempo Real com MetaTrader5', 'Analise Com Yahoo'])
st.title('**Web App de Analise de Ações**')


def get_data():
  #  path = "C:/Users/tamar/Google Drive/COTAHIST_A_SERHIST/all_bovespa.csv"
    path = "G:/Meu Drive/COTAHIST_A_SERHIST/all_bovespa.csv"
    return pd.read_csv(path)

df = get_data()
if paginaSelecionada == 'Analise de Ações':
    st.header('***Analise Gráfica de Ações***')
    df_data = pd.to_datetime(df['Data_Pregao']).dt.date.drop_duplicates()

    min_date = min(df_data)
    max_date = max(df_data)

    # Criando uma side bar
    st.sidebar.header('Determine os dados da Ação')

    stock = (df['Sigla_Acao']).drop_duplicates()
    stock_choice = st.sidebar.selectbox('Escolha sua ação', stock)

    # stock_choice = st.sidebar.text_input('Escolha sua ação')

    start_date = st.sidebar.text_input('Digite uma dada de início', min_date)
    end_date = st.sidebar.text_input('Digite uma dada de final', max_date)

    # if st.sidebar.button('Baixar Séries Históricas - B3'):
    #     #st.write(series_historicas())
    # else:
    #     st.write(f'Aguarde - data: {end_date}')
    # # atualizar = series_historicas()

    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    if start > end:
        st.error('Data Final deve ser **MAIOR** que a data inicial.')

    df = df[(df['Sigla_Acao'] == stock_choice) & (pd.to_datetime(df['Data_Pregao']) >= start) & (
            pd.to_datetime(df['Data_Pregao']) <= end)]
    df = df.set_index(pd.DatetimeIndex(df['Data_Pregao'].values))

    # Criando o Gráfico

    st.header('AÇÃO: ' + stock_choice)

    st.write('Preço de Fechamento')
    st.line_chart(df['Preco_Fechamento'])

    st.write('Volume Negocios')
    st.line_chart(df['Volume_Negocios'])

if paginaSelecionada == 'Robô de Prever Intra Day de Ações':
    robotprovidesclosure = acao()

if paginaSelecionada == 'MACD':
    macd = macd()

if paginaSelecionada == 'Real Time Bova11':
    bova = RealTime()

elif paginaSelecionada == 'Cotação em Tempo Real com MetaTrader5':
    MetaTrader = Cotacao()

elif paginaSelecionada == 'Analise Com Yahoo':
    Yahoo = Analise()