# Bibliotecas do Robô
import pandas as pd  # Le Arquivos
import streamlit as st  # Daskboard
import numpy as np
from datetime import date
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt



def acao():
    # Nome do Página
    st.header('***Robô de Prever Intra Day de Ações***')
    st.markdown("<h1 style='color:#F00;'>Robô de Prever Intra Day de Ações</h1>", unsafe_allow_html=True)
    # Buscando no Banco de dados
    #df = pd.read_csv('C:/Users/tamar/Google Drive/COTAHIST_A_SERHIST/all_bovespa.csv', delimiter=',')
    df = pd.read_csv('G:/Meu Drive/COTAHIST_A_SERHIST/all_bovespa.csv', delimiter=',')

    # Escolhendo o Ativo para o Robô
    ativo_escolha = st.sidebar.text_input('Escolha sua ação', 'GGBR4')
    df_acao = df[df['Sigla_Acao'] == ativo_escolha]

    # Exibir Tabela com Dados do Ativo
    st.write('Tabela com Todos os Dados do Ativo Escolhido')
    st.write(df_acao)

    # Mormatizando Data
    df_acao['Data_Pregao'] = pd.to_datetime(df_acao['Data_Pregao'], format='%Y-%m-%d')

    # Criando Médias Moveis de 5 dias e de 21 dias
    df_acao['mm5d'] = df_acao['Preco_Fechamento'].rolling(5).mean()
    df_acao['mm21d'] = df_acao['Preco_Fechamento'].rolling(21).mean()

    # Removendo Linhas Nulas, dos 21 dias primeiroas da Média Moveis de 21 dias
    df_acao.dropna(inplace=True)
    #df_acao

    # Reindexando o Data Frame. Reorganizando a Númeração das Linhas
    df_acao = df_acao.reset_index(drop=True)
    #df_acao

    # Determinando a Quantidade de Linhas que Será para Treino, Teste e Validação
    qtd_linhas = len(df_acao)
    qtd_linhas_treino = round(.70 * qtd_linhas)
    qtd_linhas_teste = qtd_linhas - qtd_linhas_treino
    qtd_linhas_validacao = qtd_linhas - 1
    info = (
        f"Linhas treino= 0:{qtd_linhas_treino}"
        f" Linhas teste= {qtd_linhas_treino}:{qtd_linhas_treino + qtd_linhas_teste - 1}"
        f" Linhas validação= {qtd_linhas_validacao}"
    )
    info

    # Removendo as Colunas que não Vamos Usar para Prever # de 11 titulos quero só 7 ai remove 5 # separando as features das labels
    features = df_acao.drop(['Sigla_Acao', 'Nome_Acao', 'Data_Pregao', 'Preco_Fechamento'], 1)
    labels = df_acao['Preco_Fechamento']
    # df_acao.tail()

    # Escolhendo as Melhores Métricas que Vamos Usar para Prever.O Robô escolhe apenas 7 Métricas.
    # Note que ele Escolheu como dados importantes para prever:
    # preco minimo, qtd negocios, preco maximo, mm21d, volume negociado e mm5d

    # Escolhendo as melhores features com Kbest
    features_list = ('Preco_Abertura', 'Preco_Maximo', 'Preco_Minino', 'Qtd_Negocios', 'Volume_Negocios', 'mm5d', 'mm21d')

    k_best_features = SelectKBest(k='all')
    k_best_features.fit_transform(features, labels)
    k_best_features_scores = k_best_features.scores_
    raw_pairs = zip(features_list[0:], k_best_features_scores)
    ordered_pairs = list(reversed(sorted(raw_pairs, key=lambda x: x[1])))  # Ordena as Featuresa do Maior para o Menos
    k_best_features_final = dict(ordered_pairs[:15])
    best_features = k_best_features_final.keys()
    #st.write(f'Melhores features: {k_best_features_final}')

    # Escolhendo As Métricas que o Robô escolheu que tem Maior Acerto.
    ### Removendo então a MM21d, qtd negociada.


    # Separando as Features Escolhidas
    features = df_acao.loc[:, ['Preco_Maximo', 'Preco_Minino', 'Preco_Abertura', 'mm5d']]
    #st.write(features)

    ### Determinando os Pesos para Cada Situação, Treino, Teste e Validação"""
    # Separa os dados de treino teste e validação
    X_train = features[:qtd_linhas_treino]
    X_test = features[qtd_linhas_treino:qtd_linhas_treino + qtd_linhas_teste - 1]

    y_train = labels[:qtd_linhas_treino]
    y_test = labels[qtd_linhas_treino:qtd_linhas_treino + qtd_linhas_teste - 1]
    print(len(X_train), len(y_train))
    print(len(X_test), len(y_test))

    # Normalizando os Dados da Features.
    ### Para que o robô considere todoas as metricas com o mesmo pesso.
    # Normalizando os dados de entrada(features)
    # Gerando o novo padrão
    scaler = MinMaxScaler()
    X_train_scale = scaler.fit_transform(X_train)  # Normalizando os dados de entrada(treinamento)
    X_test_scale = scaler.transform(X_test)  # Normalizando os dados de entrada(teste)

    # """# Executando o Robôs"""
    st.write('"""*Executando o Robôs*"""')

    # """## Executando o Robô no Treino da Regressão Linear"""
    # Treinamento Usando Regressão Linear # Média de Acertos: 98.35
    lr = linear_model.LinearRegression()
    lr.fit(X_train_scale, y_train)
    pred = lr.predict(X_test_scale)
    cd = r2_score(y_test, pred)
    st.write(f'Resultado do Coeficiente de determinação da Regressão Linear: {cd * 100:.2f}')

    # """## Executando o Robô no Treino da Rede Neural Simples"""
    # Rede Neural Simples # Média de Acertos: 98.02
    rn = MLPRegressor(max_iter=2000)
    rn.fit(X_train_scale, y_train)
    pred = rn.predict(X_test_scale)
    cd = rn.score(X_test_scale, y_test)
    st.write(f'Resultado do Coeficiente de determinação da Rede Neural Simples: {cd * 100:.2f}')


    # """## Exibindo a Ultima Linda sem o Fechamento"""
    st.write('Com Estes Dados que o Robô Fazer a Previsão')
    valor_novo = features.tail(1)
    df = pd.DataFrame(valor_novo)
    st.table(df)

    # ultimos_dez_fechamentos = features.tail(5)
    # """# Exibindo o Valor Previsto pelo Robô"""
    # executando a previsão
    previsao = scaler.transform(valor_novo)
    pred = lr.predict(previsao)
    # pred
    # """# Exibindo o Valor já Previsto Anteriormente com o Valor Real Acontecido."""
    st.write('Previsão Feita com Base na Regressão Linear')
    from datetime import date
    data_pregao = date.today()
    dd = pd.DataFrame({f'Data_Pregao': data_pregao, 'Previsao': pred})
    dd.set_index('Data_Pregao', inplace=True)
    info = (
        f"Data da previsão: {data_pregao}."
        f"\n    Valor Previsto pelo Robô: {pred}"
    )
    st.write(info)

if __name__ == "__main__":
    acao()

# streamlit run webappacaostreamlit.py
# pip3 install numpy
# pip install streamlit

#Operador do mercado financeiro, Faço anali-ses para compra e vende de ações voltado ao consumidor pessoa fisica  que investe no máximo,  50.000,00.
#Tenho suporte de uma corretora de investimentos.
#Desenvo um Programa  de Data Cience para operar no mercado financeiro.
#Ganhos conforme acertividade das operaçoes, por isso meus rendimentos são variados.