import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
df = pd.read_csv("BNB_sprint7.csv")

# Encabezado
st.header("Análisis de Datos de BNB")

# Casilla de verificación para mostrar histograma
if st.checkbox("Mostrar Histograma"):
    fig_hist = px.histogram(
        df,
        x="Close",
        nbins=50,
        title="Distribución del Precio de Cierre de BNB",
        labels={"Close": "Precio de cierre (USD)", "count": "Frecuencia"}
    )
    st.plotly_chart(fig_hist)

# Casilla de verificación para mostrar gráfico de dispersión
if st.checkbox("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(
        df,
        x="Close",
        y="Volume",
        title="Relación entre Precio de Cierre y Volumen Cotizado",
        labels={"Close": "Precio de cierre (USD)", "Volume": "Volumen cotizado (USD)"}
    )
    st.plotly_chart(fig_scatter)
