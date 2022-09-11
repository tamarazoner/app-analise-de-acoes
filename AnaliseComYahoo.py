#pip install pandas_datareader
import pandas as pd  # Le Arquivos
import streamlit as st  # Daskboard
import numpy as np
from pandas_datareader import data as dt
import datetime
#!pip install yfinance
import numpy as np
import datetime
import yfinance as y
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def Analise():
    # Nome do Página
    st.header('***Analise de Com Yahoo***')

    start = datetime.datetime(2021,1,1)
    # end = datetime.datetime(2020,1,1)
    end = datetime.date.today()

    start_date = st.sidebar.text_input('Digite uma dada de início', start)
    end_date = st.sidebar.text_input('Digite uma dada de fim', end)

    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    #st.sidebar.number_input()
    #start_date = st.sidebar.text_input('Digite uma dada de início','2020,1,1')
    #start_date = st.sidebar.number_input(2020,1,1)
    #start = datetime.datetime(start_date)
    #end_date = st.sidebar.text_input('Digite uma dada de final')
    #end = datetime.datetime(end_date)

    # Escolhendo o Ativo para o Robô
    ativo_escolha1 = st.sidebar.text_input('Escolha sua primeira ação', 'petr4.sa')
    petr = y.download(ativo_escolha1, start, end)

    ativo_escolha2 = st.sidebar.text_input('Escolha sua segunda ação', 'vale3.sa')
    vale = y.download(ativo_escolha2, start, end)

    ativo_escolha3 = st.sidebar.text_input('Escolha sua terceira ação', 'itub4.sa')
    itub = y.download(ativo_escolha3, start, end)

    ativo_escolha4 = st.sidebar.text_input('Escolha sua quarta ação', 'wege3.sa')
    wege = y.download(ativo_escolha4, start, end)

    ibov = y.download('^bvsp', start, end)

    """
    # Aula 33
    #Alocação da Carteira
    #Variáveis que recebe o tempo desejado
    start = datetime.datetime(2018,1,1)
    end = datetime.datetime(2020,1,1)
  
    #Criação da Lista do Carteira
    petr = y.download('petr4.sa', start, end)
    vale = y.download('vale3.sa', start, end)
    itub = y.download('itub4.sa', start, end)
    wege = y.download('wege3.sa', start, end)
    ibov = y.download('^bvsp', start, end)
  """
    st.markdown("<h1 style='color:#F00;'>Petrobras</h1>", unsafe_allow_html=True)
    petr.columns = ['Alto', 'Baixo', 'Abertura', 'Fechamento', 'Volume', 'Adj Close']
    st.write(petr)

    #Criando um For para normalização dos Retornos da Carteira
    for papeis in (petr, vale, itub, wege):
      papeis['Retorno Normalizado'] = papeis['Adj Close'] / papeis['Adj Close'].iloc[0]  #Normalizando os Retornos

    #Alocando R$$ de acordo com o peso das carteira Capital Inicial de R$10.000,00
    #25% petr, 25% vale, 25% itub, 25% wege
    #Alocando o peso de cada papel
    st.markdown("<h1 style='color:#F00;'>Petrobras Retorno Normalizado</h1>", unsafe_allow_html=True)
    for papeis, peso in zip((petr, vale, itub, wege), [.25, .25, .25, .25]):
      papeis['Alocacao'] = papeis['Retorno Normalizado'] * peso
    petr.columns = ['Alto', 'Baixo', 'Abertura', 'Fechamento', 'Volume', 'Fechamento Ajustado', 'Retorno Normatizado', 'Alocacao']
    st.write(petr)

    #Calculando o Valor de acordo com seu peso de cada papel na carteira
    # Valor de Patrimonio por papel

    for papeis in (petr, vale, itub, wege):
      papeis['Valor Posicao'] = papeis ['Alocacao'] * 1000

    #Calculando o Retorno em R$$ da carteira de acordo com cada peso
    # Cada busca feita em um papel é igual a uma aba do excel
    # Para apurarmos o retorno da carteira de acordo com o seu peso que será o valor aplicado. Temos que unir tudo isso
    # em uma aba só e para isso vamos usar o Concat

    valor_posicoes = [petr['Valor Posicao'], vale['Valor Posicao'], itub['Valor Posicao'], wege['Valor Posicao']]
    valor_carteira = pd.concat(valor_posicoes, axis= 1)
    # axis pega somente a linha, sem ele vai pegar a coluna inteira

    st.markdown("<h1 style='color:#F00;'>Renomeando os Titulos dos Ativos ou Colunas</h1>", unsafe_allow_html=True)
    #Renomeando os Titulos dos Ativos ou Colunas
    #valor_carteira.columns = ['Petro', 'Vale', 'Itub', 'Wege']
    valor_carteira.columns = [ativo_escolha1, ativo_escolha2, ativo_escolha3, ativo_escolha4]
    st.write(valor_carteira)

    st.markdown("<h1 style='color:#F00;'>Calculando o Retorno da Carteira</h1>", unsafe_allow_html=True)
    #Calculando o Retorno da Carteira
    valor_carteira['Total R$'] = valor_carteira.sum(axis=1)
    valor_carteira.columns = [ativo_escolha1, ativo_escolha2, ativo_escolha3, ativo_escolha4, 'Total R$']
    st.write(valor_carteira)

    #Comprarando o Retorno da Carteira com o Ibovespa e Exibindo no Gráfico Normalizado (Todos Ativos da Carteira em um único Ativo, Média dos ativos)
    (valor_carteira['Total R$'] / valor_carteira['Total R$'].iloc[0]).plot(figsize=(10,8), label="Carteira")
    (ibov['Adj Close'] /  ibov['Adj Close'].iloc[0]).plot(label="Ibovespa")
    plt.legend()

    #Exibir Gráficamente de foma Normalizada Todos os Ativos da Carteira
    (valor_carteira / valor_carteira.iloc[0]).plot(figsize=(10,6))


    # Aula 35
    st.markdown("<h1 style='color:#F00;'>Calculo do Retorno Diário da Carteira Últimos 5</h1>", unsafe_allow_html=True)
    #Calculo do Retorno Diário da Carteira Últimos 5
    valor_carteira['Retorno Diário'] = valor_carteira['Total R$'].pct_change() * 100

    valor_carteira.columns = [ativo_escolha1, ativo_escolha2, ativo_escolha3, ativo_escolha4, 'Total R$', 'Retorno Diário']
    st.write(valor_carteira.tail(5))

    #Calculo do Retorno Médio Diário da Carteira
    valor_carteira['Retorno Diário'].mean()

    #Calculo do DESVIO PADÃO Diário da Carteira
    valor_carteira['Retorno Diário'].std()

    #Calculo da Distribuição Diário da Carteira. Usando um Gráfico de Barras e ou Linha no modelo Histograma.
    #Calculo da Distribuição Diário da Carteira. Usando um Gráfico de Barras modelo Histograma.
    valor_carteira['Retorno Diário'].plot(kind='hist', bins=100, figsize=(8,5))
    # kind='hist defique que será do modelo Histograma. bins=100 defina quantas linhas vão aparecer, barras.

    #Calculo da Distribuição Diário da Carteira. Usando um Gráfico de Linha no modelo Histograma.
    valor_carteira['Retorno Diário'].plot(kind='kde', figsize=(8,5))

    #Calculando o Retorno ACUMULADO da carteira
    retorno_aplicacao = (valor_carteira['Total R$'][-1] / valor_carteira['Total R$'][0] -1) * 100

    st.markdown("<h1 style='color:#F00;'>Retorno em Porcentagem</h1>", unsafe_allow_html=True)
    # retorno em Porcentagem
    st.write(round(retorno_aplicacao))

    """
    # Aula 37
    #Variáveis que recebe o tempo desejado
    start = datetime.datetime(2018,1,1)
    end = datetime.datetime(2020,6,1)
    
    #Criação da Lista do Carteira
    papeis = ['btow3.sa', 'lame4.sa', 'sled4.sa', '^bvsp']
    """
    papeis = [ativo_escolha1, ativo_escolha2, ativo_escolha3,  ativo_escolha4, '^bvsp']

    st.markdown("<h1 style='color:#F00;'>Pegando Dados da Carteira no Yahoo</h1>", unsafe_allow_html=True)
    #Pegando Dados da Carteira no Yahoo
    carteira = y.download(papeis, start, end)['Adj Close']
    #carteira.columns = ['B2W Digital', 'Lojas Americanas', 'Saraiva', 'Ibovespa']
    carteira.columns = [ativo_escolha1, ativo_escolha2, ativo_escolha3,  ativo_escolha4, 'Ibovespa']
    st.write(carteira.tail())

    #Mostrando o Resultado da Carteira no Gráfico NORMALIZADO
    #st.line_chart((carteira / carteira.iloc[0]).plot(figsize=(10,8)))
    st.write('Gráfico NORMALIZADO')
    st.line_chart((carteira / carteira.iloc[0]))

    # Modelo
    st.write('Gráfico de Barras modelo Histograma')
    arr = np.random.normal(1, 1, size=130)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)


if __name__ == "__main__":
    Analise()


    #Indice Ibovespa Futuro -> IBV=F