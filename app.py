# Librerías
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Cargar datos
df = pd.read_csv(
    "C:/Users/ffern/Desktop/Sprint 7/Render_Proyecto_S7/bike_sales.csv")

# Título
st.header("Relación precio-kilometraje de motos usadas", divider="gray")

# Boton Descargar
st.download_button(
    label="Descargar dataset",
    data=df.to_csv(index=False),
    file_name="df.csv"
)

# Crear un botón
hist_button = st.button("Construir histograma")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de motos usadas")

    fig = px.histogram(df, x="km_driven")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scat_button = st.button("Contruir gráfico de dispersión")

if scat_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de motos usadas")

    # crear un gráfico  de dispersión
    fig = px.scatter(df, x="km_driven", y="selling_price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
