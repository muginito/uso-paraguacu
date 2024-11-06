import streamlit as st
from streamlit_folium import *
import pandas as pd
import folium

st.title("Mapa Interativo")

map = folium.Map(location=[-12.900, -41.314], zoom_start=10)

st_data = st_folium(map)
