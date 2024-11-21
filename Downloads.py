import streamlit as st
import time

link_download = st.secrets["DOWNLOAD"]

st.link_button(label="Dados Uso Paraguaçu", url=link_download)


# data = {
#     'Ano': [2010, 2010, 2011, 2011, 2012, 2012, 2013, 2013, 2014, 2014],
#     'Município': ['Município A', 'Município B', 'Município A', 'Município B',
#                   'Município A', 'Município B', 'Município A', 'Município B',
#                   'Município A', 'Município B'],
#     'Área': [1500, 1300, 1600, 1400, 1700, 1500, 1650, 1550, 1800, 1600]
# }
# df = pd.DataFrame(data)

# # Título do app
# st.title("Medidas de Áreas por Ano e Município")

# st.bar_chart(data, x='Ano', y='Área', color="Município", stack=False)
