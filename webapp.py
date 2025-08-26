import streamlit as st

st.title("Procesador de Texto Interlineal")
st.write("Ingresa dos textos y el programa los unirá línea por línea.")

col1, col2 = st.columns(2)

with col1:
    texto1 = st.text_area("Texto 1", height=300)

with col2:
    texto2 = st.text_area("Texto 2", height=300)

if st.button("Procesar"):
    lista1 = texto1.split("\n")
    lista2 = texto2.split("\n")

    resultado_str = ""
    # Se usa min() para asegurar que el bucle no exceda el texto más corto
    for i in range(min(len(lista1), len(lista2))):
        resultado_str += f"{lista1[i]}\n{lista2[i]}\n"

    st.text_area("Resultado", resultado_str, height=400)
