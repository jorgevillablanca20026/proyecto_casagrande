import streamlit as st
import pandas as pd
import libreria_funciones as lf

st.title("Proyecto Final")
st.sidebar.title("Parámetros")
st.sidebar.image('python_logo.png')
st.image('python_logo.png')


uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

monto=st.numbers_intut("Ingrese el monto:",min_value = 0, max_value=10000, value=1000)
interes.numbers_intut("Ingrese el interes:",min_value = 0.0, max_value=1.0, value=0.10)
anios.numbers_intut("Ingrese el año:",value=1)
numero_pagos.numbers_intut("Ingrese el número de pagos:", value=12)

cuota = lf.cuota_prestamo(1000,0.10,5,12)
st.write(cuota)

