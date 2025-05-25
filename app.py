import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
# Asegúrate de que el CSV esté en la misma carpeta que app.py
df = pd.read_csv("BNB_sprint7.csv")

# Encabezado
st.header("Análisis de Datos de BNB")

# Botón para mostrar histograma
if st.button("Mostrar Histograma"):
    fig_hist = px.histogram(
        df,
        x="close",
        nbins=50,
        title="Distribución del Precio de Cierre de BNB",
        labels={"close": "Precio de cierre (USD)", "count": "Frecuencia"}
    )
    st.plotly_chart(fig_hist)

# Botón para mostrar gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(
        df,
        x="close",
        y="quote_volume",
        title="Relación entre Precio de Cierre y Volumen Cotizado",
        labels={
            "close": "Precio de cierre (USD)", "quote_volume": "Volumen cotizado (USD)"}
    )
    st.plotly_chart(fig_scatter)
# Fin del script
