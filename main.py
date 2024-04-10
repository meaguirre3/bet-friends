import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta


st.title('💵 Bet Friends :sunglasses:')
st.text('Pagina para recordar las apuestas')
# Agregar un widget en la barra lateral
#st.sidebar.header('Menu')


# Using object notation
#add_selectbox = st.sidebar.selectbox(
#    "Select",
#    ("Historial", "Apuesta Actual")
#)


# Datos de ejemplo
personas = ['Lobiño', 'Pacha','Chicho', 'Alexis', 'Ri','Marco']
puntuaciones = [10,20 ,0.5, 0.5, 0.5,10]
emojis = ['👶🏿🍊🍽️','🍺⚽', '🤵🍺', '👻', '😎🍊','🚴']

# Crear el gráfico de barras
fig = go.Figure()

for persona, punt, emoji in zip(personas, puntuaciones, emojis):
    fig.add_trace(go.Bar(x=[persona], y=[punt], text=emoji, textposition='auto', name=persona))
    

# Configuración del diseño
fig.update_layout(
    title='Puntuaciones Apuestas',
    xaxis_title='Nombre',
    yaxis_title='Dolares',
    barmode='group'
)

# Mostrar el gráfico usando Streamlit
st.plotly_chart(fig)
# Using "with" notati

# Generar datos de ejemplo


# Cargar los datos desde el archivo CSV
df = pd.read_csv("history.csv")

# Convertir la columna 'fecha' a tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Crear el gráfico temporal
fig = go.Figure()

# Iterar sobre cada nombre único y agregar una línea para cada uno
#for nombre in df['nombre'].unique():
#    df_temp = df[df['nombre'] == nombre]
#    fig.add_trace(go.Scatter(x=df_temp['fecha'], y=df_temp['apuesta'], mode='lines+markers', name=nombre))
for nombre in df['nombre'].unique():
    df_temp = df[df['nombre'] == nombre]
    partido = df_temp['partido']
    fig.add_trace(go.Scatter(
        x=df_temp['fecha'].dt.strftime('%Y-%m-%d'),
        y=df_temp['apuesta'],
        mode='lines+markers',  # Include lines along with markers
        name=nombre,
        marker=dict(size=8, opacity=0.8),  # Adjust marker size and opacity
        line=dict(width=2),  # Adjust line width
        hovertemplate=partido  # Define the tooltip content
    ))

# Configurar el diseño del gráfico
fig.update_layout(
    title="Apuestas a lo largo del tiempo",
    xaxis_title="Fecha",
    yaxis_title="Apuesta",
    legend_title="Nombre",
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

def get_chart_12486592():
    import plotly.express as px
    data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
    fig = px.imshow(data,
                    labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['Morning', 'Afternoon', 'Evening']
                   )
    fig.update_xaxes(side="top")

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

get_chart_12486592()
