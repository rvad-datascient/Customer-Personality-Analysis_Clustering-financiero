# 📊 Customer Personality Analysis – Clustering Financiero

Este proyecto analiza clientes de una campaña de marketing, creando segmentos mediante clustering para entender su comportamiento y potencial de negocio.

## 🎯 Objetivos

- Identificar patrones de compra y características sociodemográficas.
- Agrupar a los clientes en segmentos estratégicos.
- Facilitar la personalización de campañas comerciales.

## 🚀 Flujo de Trabajo

1. **Limpieza y Feature Engineering**
   - Conversión de fechas.
   - Creación de variables derivadas (Edad, Gasto Total, etc.).
   - Imputación de nulos.
   - Codificación de variables categóricas.
   - Escalado de variables.

2. **Modelado**
   - Reducción de dimensionalidad (PCA, t-SNE).
   - K-Means Clustering (4 segmentos).
   - Evaluación con Silhouette Score.

3. **Resultados**
   - Segmentación en clusters:
     - Tradicionales
     - Desconectados
     - Alto Valor
     - Estrella

4. **Visualización**
   - Gráficos de dispersión.
   - Barras comparativas.
   - Radar chart de características.

## 🛠️ Estructura del Proyecto

├── 01_Data/
│ ├── Customer_Personality.csv
│ └── marketing_campaign.csv
├── 02_src/ # Scripts de limpieza, feature engineering, clustering
├── 03_notebooks/ # Notebooks de EDA y feature engineering
├── 05_ml_project/
│ ├── app.py
│ ├── model.pkl
│ ├── requirements.txt
│ ├── README.md
│ └── .gitignore

---

## 🌐 Aplicación Web

Ya puedes probar la aplicación en vivo aquí:

👉 [Haz clic para abrir la app de predicción]([https://impagohipotecas.streamlit.app/](https://customer-personality-analysisclustering-financiero-nc4v8nmvjxk.streamlit.app/))

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd "Customer Personality Analysis_Clustering financiero"

2. Instalar dependencias
pip install -r 05_ml_project/requirements.txt

3. Lanzar la aplicación Streamlit:
streamlit run 05_ml_project/app.py

📈 App de Streamlit
Permite:

Subir nuevos clientes.
Asignarles un segmento.
Visualizar perfiles.
