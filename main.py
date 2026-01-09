import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Josmo Analytics", page_icon="👟")

# Título con estilo
st.markdown("# 🚀 Josmo Market Intelligence")
st.markdown("---")

# Cargar los datos generados
df = pd.read_csv('market_data.csv')

# --- SIDEBAR FILTERS ---
st.sidebar.header("Configuración de Vista")
selected_brand = st.sidebar.multiselect("Filtrar por Marca", options=df['Marca'].unique(), default=df['Marca'].unique())
filtered_df = df[df['Marca'].isin(selected_brand)]

# --- MAIN METRICS ---
m1, m2, m3 = st.columns(3)
with m1:
    avg_price = filtered_df['Precio Retailer ($)'].mean()
    st.metric("Precio Promedio Mercado", f"${avg_price:.2f}")
with m2:
    low_stock = len(filtered_df[filtered_df['Stock'] != 'In Stock'])
    st.metric("Alertas de Stock", low_stock, delta_color="inverse")
with m3:
    discounts = len(filtered_df[filtered_df['Diferencia (%)'] < 0])
    st.metric("Productos en Oferta", discounts)

# --- VISUALIZACIÓN ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Variación de Precios por Producto")
    fig_price = px.bar(filtered_df, x='Producto', y=['Precio Oficial ($)', 'Precio Retailer ($)'], 
                       barmode='group', color_discrete_sequence=['#1f77b4', '#ff7f0e'])
    st.plotly_chart(fig_price)

with col_right:
    st.subheader("Distribución de Stock")
    fig_pie = px.pie(filtered_df, names='Stock', hole=0.4, color='Stock',
                    color_discrete_map={'In Stock':'green', 'Low Stock':'orange', 'Out of Stock':'red'})
    st.plotly_chart(fig_pie)


st.subheader("📋 Datos en Tiempo Real")
st.dataframe(filtered_df.style.highlight_min(axis=0, subset=['Precio Retailer ($)'], color='#ffcccc'))

criticos = df[df['Stock'] == 'Out of Stock']
if not criticos.empty:
    st.subheader("🚨 Alertas de Inventario")
    st.error(f"Se han detectado {len(criticos)} rupturas de stock en canales externos.")
    st.dataframe(criticos[['Fecha', 'Marca', 'Producto', 'Canal']])
else:
    st.success("Todo el inventario está disponible.")
