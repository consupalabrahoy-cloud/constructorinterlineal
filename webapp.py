import streamlit as st

# Función para copiar al portapapeles usando HTML y JavaScript
def st_copy_to_clipboard(text_to_copy):
    """
    Crea un botón para copiar el texto dado al portapapeles.
    """
    st.button(
        "Copiar al portapapeles",
        on_click=lambda: st.write(
            f"<script>navigator.clipboard.writeText(`{text_to_copy}`)</script>",
            unsafe_allow_html=True
        )
    )

st.title("Procesador de Texto Interlineal")
st.write("Ingresa dos textos y el programa los unirá línea por línea.")

# Inicializa st.session_state para almacenar el resultado
if 'resultado_interlineal' not in st.session_state:
    st.session_state.resultado_interlineal = ""

col1, col2 = st.columns(2)

with col1:
    texto1 = st.text_area("Texto 1", height=300)

with col2:
    texto2 = st.text_area("Texto 2", height=300)

if st.button("Procesar"):
    lista1 = texto1.split("\n")
    lista2 = texto2.split("\n")

    resultado_str = ""
    for i in range(min(len(lista1), len(lista2))):
        resultado_str += f"{lista1[i]}\n{lista2[i]}\n"

    # Almacena el resultado en el estado de la sesión
    st.session_state.resultado_interlineal = resultado_str

# Muestra el resultado desde el estado de la sesión
st.text_area("Resultado", st.session_state.resultado_interlineal, height=400, key="resultado_final")
    
# Botón para copiar el resultado
st_copy_to_clipboard(st.session_state.resultado_interlineal)
