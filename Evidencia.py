import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

st.title("Titulo: Analitica de datos")
st.header("Este es un header xd")
st.subheader("Este es un subheader")


st.text("Texto: Hola stream")
st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
st.header("Successful")
st.info("Información")
st.warning("warning")
st.error("Error")
st.exception("NameError('no está definido')")
st.header("Obtener informacion de ayuda python")
st.help(range)
st.header("widgets: ")
st.subheader("Checkbox")

if st.checkbox("Show/Hide"):
  st.text("Mostrar u ocultar widget")
  st.subhead("Radio Buttons")

status = st.radio("Cual es su estatus",("Activo","Inactivo"))

if status == "Activo":
    st.success("Estás activo")
else: 
    st.warning("Inactivo")
    st.subheader("SelectBox")

occupation = st.selectbox(
    "Tu ocupación", ["Programador", "Científico de datos", "BI", "Ingeniero de Datos"]
)

st.write("Opción seleccionada:", occupation)
st.subheader("MultiSelect")

location = st.multiselect(
    "Donde trabajas?",
    ("México", "New York", "Guadalajara", "Monterrey", "Nepal", "Buenos Aires", "Caracas"),
)

st.write("Seleccionó:", len(location), "locaciones")
st.subheader("Slider")

level = st.slider("Cual es tu nivel?", 1, 5)
st.write("Nivel:", level)