import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([st.Page("Tabela.py", title="Home", icon=":material/home:"),
                    st.Page("Mapa.py", icon=":material/map:"),
                    st.Page("Downloads.py", icon=":material/download:"),
                    st.Page("Sobre.py", icon=":material/more_horiz:"),
                    ])

st.title("Uso da Bacia do Paraguaçu")

pg.run()
