import streamlit as st

# Función para copiar al portapapeles de manera confiable
def st_copy_to_clipboard(label, text_to_copy):
    """
    Crea un botón que copia el texto dado al portapapeles de manera confiable.
    """
    st.button(
        label,
        on_click=lambda: st.write(
            f"""
            <script>
                navigator.clipboard.writeText(`{text_to_copy}`);
            </script>
            """,
            unsafe_allow_html=True
        )
    )

st.title("Procesador de Texto Interlineal")
st.write("Ingresa dos textos y el programa los unirá línea por línea.")

# Inicializa st.session_state para almacenar los valores
if 'texto1' not in st.session_state:
    st.session_state.texto1 = ""
if 'texto2' not in st.session_state:
    st.session_state.texto2 = ""
if 'resultado' not in st.session_state:
    st.session_state.resultado = ""

col1, col2 = st.columns(2)

with col1:
    # El key es suficiente para vincular el campo de texto con st.session_state
    texto1 = st.text_area(
        "Texto 1",
        height=300,
        key="texto1"
    )

with col2:
    # El key es suficiente para vincular el campo de texto con st.session_state
    texto2 = st.text_area(
        "Texto 2",
        height=300,
        key="texto2"
    )

# Botones de acción
if st.button("Procesar"):
    lista1 = st.session_state.texto1.split("\n")
    lista2 = st.session_state.texto2.split("\n")
    resultado_str = ""
    for i in range(min(len(lista1), len(lista2))):
        resultado_str += f"{lista1[i]}\n{lista2[i]}\n"
    st.session_state.resultado = resultado_str

if st.button("Limpiar campos"):
    st.session_state.texto1 = ""
    st.session_state.texto2 = ""
    st.session_state.resultado = ""

# Muestra el resultado
st.text_area("Resultado", st.session_state.resultado, height=400)
    
# Botón para copiar el resultado al portapapeles
st_copy_to_clipboard("Copiar resultado", st.session_state.resultado)
