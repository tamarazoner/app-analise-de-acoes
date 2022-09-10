#        índice

# 1) Colocar um titulo o Meu Lateral da App Web
# 2) Colocar uma Imagem no fundo do App
# 3) Colocar uma Tabela com titulo e titulo da tabela
# 4) Ler o  Encoding do arquivo CSV
# 5) Salvar arquivo zip contendo csv


# 1) Colocar um titulo do Menu Lateral
st.sidebar.markdown("side")

# 2) Colocar uma Imagem no fundo do App
import base64
main_bg = "C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/Touros_TRADER.png"
main_bg_ext = "png"

side_bg = "C:/Users/tamar/OneDrive/Área de Trabalho/Financeial Career Path/Touros_TRADER.png"
side_bg_ext = "png"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 3) Colocar uma Tabela com titulo e titulo da tabela
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'Titulo': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x

# 4) Ler o  Encoding do arquivo CSV
with open('BOVA11_holdings.csv') as f:
    print(f)

arquivo = open('BOVA11_holdings.csv', encoding='utf-8')
print(arquivo)
# Resposta: <_io.TextIOWrapper name='BOVA11_holdings.csv' mode='r' encoding='cp1252'>


# 5) Salvar arquivo zip contendo csv
compression_opts = dict(method='zip',
                        archive_name='out.csv')
df.to_csv('out.zip', index=False,
          compression=compression_opts)