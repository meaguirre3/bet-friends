import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
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

def get_deudas():
    data=[[0, 20, 0, 0, 0,20], 
          [0, 0, 0, 0, 0,0], 
          [0, 0, 0, 0, 0,0],
         [0, 0, 0, 0, 0,0],
         [0, 0, 0, 0, 0,0],
         [10, 0, 0, 0, 0,0]]
    fig = px.imshow(data,
                    x=['Lobiño', 'Pacha','Chicho', 'Alexis', 'Ri','Marco'],
                    y=['Lobiño', 'Pacha','Chicho', 'Alexis', 'Ri','Marco'],
                    text_auto=True)
    fig.update_xaxes(side="top")
    fig.update_layout(
    title="Acumulado Pagar ")
    st.plotly_chart(fig, theme=None)

get_deudas()
def get_tabla():
    df = pd.read_csv('history.csv')
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=list(df.values),
               fill_color='lavender',
               align='left'))])
    st.plotly_chart(fig)
get_tabla()
