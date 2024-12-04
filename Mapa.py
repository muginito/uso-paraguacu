import streamlit as st
from streamlit_folium import *
import folium

st.header("Mapa Interativo")

seletores = {
    "Assentamentos": st.secrets["ASSENTAMENTOS"],
    "Curso D'Água": st.secrets["CURSODAGUA"],
    "Ferrovias": st.secrets["FERROVIAS"],
    "Limite da Bacia": st.secrets["LIMITEBACIA"],
    "Localidades": st.secrets["LOCALIDADES"],
    "Municípios": st.secrets["MUNICIPIOS"],
    "Parque Nacional": st.secrets["PARQUENACIONAL"],
    "Quilombolas": st.secrets["QUILOMBOLAS"],
    "Rodovias": st.secrets["RODOVIAS"]
}

@st.cache_data
def carregar_geojson(url):
    """Função para carregar e retornar a URL do GeoJSON."""
    return url

base_map = folium.Map(location=[-12.900, -41.314], zoom_start=7)
base_map.fit_bounds([[-13.891012650559619, -42.65575422399996], [-10.734992022654184, -38.64452899499997]])


select = st.selectbox("GeoJson", seletores.keys(), index=5)

geojson_url = carregar_geojson(seletores.get(select))
geojson_layer = folium.GeoJson(geojson_url, name=select)
geojson_layer.add_to(base_map)

st_data = st_folium(base_map, use_container_width=True)
