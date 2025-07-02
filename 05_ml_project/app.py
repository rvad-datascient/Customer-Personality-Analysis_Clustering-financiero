# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# -----------------------------
# Rutas absolutas relativas al script
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar modelo entrenado
model_path = os.path.join(BASE_DIR, "kmeans_customer_segments.pkl")
kmeans_model = joblib.load(model_path)

# Cargar dataset final con clusters (opcional)
@st.cache_data
def load_data():
    csv_path = os.path.join(BASE_DIR, "customer_segments.csv")
    df = pd.read_csv(csv_path)
    return df

df = load_data()

# -----------------------------
# Título y descripción
# -----------------------------
st.title("📊 Customer Personality Segmentation App")

st.write("""
Esta aplicación permite clasificar clientes en segmentos y analizar características clave.
""")

# -----------------------------
# Mostrar datos cargados
# -----------------------------
if st.checkbox("Mostrar datos"):
    st.dataframe(df.head())

# -----------------------------
# Subir CSV para predicción
# -----------------------------
st.subheader("🎯 Clasificar nuevo cliente")
uploaded_file = st.file_uploader(
    "Sube un CSV con los datos escalados del cliente (mismos features que el dataset de entrenamiento):",
    type="csv"
)

if uploaded_file:
    new_data = pd.read_csv(uploaded_file)
    cluster_pred = kmeans_model.predict(new_data)
    st.success(f"✅ Segmento asignado: **{cluster_pred[0]}**")

# -----------------------------
# Visualización de distribución de clusters
# -----------------------------
st.subheader("📈 Distribución de segmentos")

if "Segment" in df.columns:
    counts = df['Segment'].value_counts().sort_index()
    st.bar_chart(counts)
else:
    st.warning("La columna 'Segment' no se encontró en el dataset.")

# -----------------------------
# Footer
# -----------------------------
st.write("© 2025 – Customer Personality Analysis Clustering")


