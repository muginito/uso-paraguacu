import streamlit as st
from streamlit_folium import *
import pandas as pd
import geopandas as gpd
from dotenv import load_dotenv
from os import getenv
import folium
import streamlit.components.v1 as components

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

# gdf = gpd.read_file(r"./dados/geojson/CursoDagua.geojson").simplify(tolerance=0.001, preserve_topology=True)

# geojson_data = gdf.to_json()

map = folium.Map(location=[-12.900, -41.314], zoom_start=10)

# folium.GeoJson(geojson_data, name="geojson").add_to(map)

select = st.multiselect("GeoJson", seletores)

# if select:
#     file_path = seletores.get(select[0])
#     gdf = gpd.read_file(file_path)
#     geojson_data = gdf.to_json()\
#     # .simplify(tolerance=0.001, preserve_topology=True)
#     folium.GeoJson(geojson_data, name="geojson").add_to(map)

@ st.cache_data
def carregar_geojson(l, seletores):
    file_path = seletores.get(l[0])
    gdf = gpd.read_file(file_path)
    return gdf.to_json()

if select:
    geojson_data = carregar_geojson(select, seletores)
    folium.GeoJson(geojson_data, name="geojson").add_to(map)

with st.container():
    st_data = st_folium(map, use_container_width=True)
