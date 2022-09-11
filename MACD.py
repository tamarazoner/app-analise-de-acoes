# Bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

# Bibliotecas


def macd():
    # Nome do Página
    st.header('***MACD***')
    st.markdown("<h1 style='color:#F00;'>MACD</h1>", unsafe_allow_html=True)
    # Buscando no Banco de dados
    #df = pd.read_csv('C:/Users/tamar/Google Drive/COTAHIST_A_SERHIST/all_bovespa.csv', delimiter=',')
    df = pd.read_csv('G:/Meu Drive/COTAHIST_A_SERHIST/all_bovespa.csv', delimiter=',')
    st.write(df)

    # Escolhendo o Ativo para o MACD
    ativo_escolha = st.sidebar.text_input('Escolha sua ação', 'GGBR4')
    df_acao = df[df['Sigla_Acao'] == ativo_escolha]

    df_acao['Data_Pregao'] = pd.to_datetime(df_acao['Data_Pregao'], format='%Y-%m-%d')
    df_acao.dtypes

    df_acao_2020 = df_acao[df_acao['Data_Pregao'] >= '2020-03-01']
    df_acao_2020

    df_acao_2020 = df_acao[df_acao['Data_Pregao'] >= '2020-03-01']
    df_acao_2020

    df_acao_2020 = df_acao_2020.set_index(pd.DatetimeIndex(df_acao_2020['Data_Pregao'].values))
    df_acao_2020

    rapidaMME = df_acao_2020.Preco_Fechamento.ewm(span=12).mean()
    lentaMME = df_acao_2020.Preco_Fechamento.ewm(span=26).mean()
    MACD = rapidaMME - lentaMME

    sinal = MACD.ewm(span=9).mean()

    plt.figure(figsize=(15, 5))
    plt.plot(df_acao_2020.index, MACD, label='Itau', color='blue')
    plt.plot(df_acao_2020.index, sinal, label='sinal', color='orange')
    plt.xticks(rotation=90)
    plt.legend(loc='upper right')
    #plt.show()

    df_acao_2020['MACD'] = MACD
    df_acao_2020['sinal'] = sinal
    st.write(df_acao_2020)

    minimo = min([min(df_acao_2020['sinal']), min(df_acao_2020['MACD'])])
    maximo = max([max(df_acao_2020['sinal']), max(df_acao_2020['MACD'])])

    fig = make_subplots(vertical_spacing=0, rows=2, cols=1, row_heights=[4, 3])

    fig.add_trace(
        go.Candlestick(x=df_acao_2020.index, open=df_acao_2020['Preco_Abertura'], high=df_acao_2020['Preco_Maximo'],
                       low=df_acao_2020['Preco_Minino'], close=df_acao_2020['Preco_Fechamento']))

    fig = make_subplots(vertical_spacing=0, rows=2, cols=1, row_heights=[4, 3])
    """
    fig.add_trace(go.Scatter(x=df_acao_2020.index, y=df_acao_2020['MACD'], name='MACD', line=dict(color='blue')), row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=df_acao_2020.index, y=df_acao_2020['sinal'], name='Sinal', line=dict(color='yellow')),
                  row=2, col=1)

    fig.update_layout(xaxis_rangeslider_visible=False,
                      xaxis=dict(zerolinecolor='black', showticklabels=False),
                      xaxis2=dict(showticklabels=False))
    fig['layout']['yaxis2'].update(range=[minimo, maximo])

    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=False)
    fig.show()
"""
if __name__ == "__main__":
    macd()