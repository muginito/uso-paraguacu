import streamlit as st

link_download = st.secrets["DOWNLOAD"]

st.link_button(label="Dados Uso Paraguaçu", url=link_download)
