#!pip install MetaTrader5
#pip install datetime
import time
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd  # Le Arquivos
import streamlit as st  # Daskboard

def Cotacao():
    st.header('***Cotações em Tempo Real pelo Meta Trader***')
    # conecte-se ao MetaTrader 5 e ja Abre

    if not mt5.initialize():
        st.write("initialize() falhou")
        mt5.shutdown()

    # Mostrar todos os Ativos Disponíveis
    ativos = mt5.symbols_get()
    st.write('Mostrar todos os Ativos Disponíveis: ')
    st.write(len(ativos))

    # mostras 10 ativos
    st.write('Mostras primeiros 10 ativos: ')
    for i in range(10):
        st.write(ativos[i].name)

    # Retorna quantos candles quiser do ativo x, do tempo de 1m, do indice 0 ate 1(ultimo valor)
    st.write('Retorna quantos candles quiser do ativo x(Win), do tempo de 1m, do indice 0 ate 1(ultimo valor): ')
    st.write(mt5.copy_rates_from_pos('WIN$', mt5.TIMEFRAME_M1, 0, 1))

    # Exibe e passa os dados do ativo para um DataFrame
    def get_ohlc(ativo, timeframe, n=5):
        ativo = mt5.copy_rates_from_pos(ativo, timeframe, 0, n)
        ativo = pd.DataFrame(ativo)
        ativo['time'] = pd.to_datetime(ativo['time'], unit='s')
        ativo.set_index('time', inplace=True)
        return ativo
    st.write('Exibe e passa os dados do ativo para um DataFrame: ')
    st.write(get_ohlc('WIN$', mt5.TIMEFRAME_M1))

    #retorna o ultimo tik
    st.write('Mostra o ultimo tik: ')
    st.write(mt5.symbol_info_tick('WIN$'))

#    tempo = time.time() + 5

#    while time.time() < tempo:
#        tick = mt5.symbol_info_tick('WIN$')
#        st.write(f"WIN$ - Último:{tick.last}, bid:{tick.bid}, ask:{tick.ask}", end='\r')
#        time.sleep(0.5)
    if st.button('Atualizar Preço da Ação '):
        tick = mt5.symbol_info_tick('WIN$')
        st.write('Exibir Último Preço da Ação ')
        st.write(f"WIN$ - Último: {tick.last}, bid:{tick.bid}, ask:{tick.ask}", end='\r')
        st.write(f"WIN$ - Último: {tick.last}", end='\r')
    else:
       st.write('Exibir Último Preço da Ação')

if __name__ == "__main__":
    Cotacao()

    """
import MetaTrader5 as mt5

# exibimos dados sobre o pacote MetaTrader5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# obtemos todos os símbolos
symbols = mt5.symbols_get()
print('Symbols: ', len(symbols))
count = 0
# exibimos os 5 primeiros
for s in symbols:
    count += 1
    print("{}. {}".format(count, s.name))
    if count == 5: break
print()

# obtemos símbolos cujos nomes contêm RU
ru_symbols = mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()

# obtemos símbolos cujos nomes não contêm USD, EUR, JPY e GBP
group_symbols = mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name, ":", s)

# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()"""