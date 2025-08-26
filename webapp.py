import streamlit as st

# Función para copiar al portapapeles usando HTML y JavaScript
def copy_to_clipboard_button(label, text_to_copy):
    """
    Crea un botón que copia el texto dado al portapapeles.
    """
    st.button(
        label,
        key=f"copy_{label}",
        help="Copia el texto del área de resultado.",
        on_click=lambda: st.write(
            f"<script>navigator.clipboard.writeText(`{text_to_copy}`)</script>",
            unsafe_allow_html=True
        )
    )

st.title("Procesador de Texto Interlineal")
st.write("Ingresa dos textos y el programa los unirá línea por línea.")

# --- Inicializar st.session_state para almacenar los valores ---
# Se inicializa solo si las claves no existen para evitar errores de renderizado
if 'texto1' not in st.session_state:
    st.session_state.texto1 = ""
if 'texto2' not in st.session_state:
    st.session_state.texto2 = ""
if 'resultado' not in st.session_state:
    st.session_state.resultado = ""

col1, col2 = st.columns(2)

with col1:
    # Se usa el key y el valor de st.session_state para conectar el widget
    st.session_state.texto1 = st.text_area(
        "Texto 1", 
        height=300, 
        key="texto1", 
        value=st.session_state.texto1
    )

with col2:
    # Se usa el key y el valor de st.session_state para conectar el widget
    st.session_state.texto2 = st.text_area(
        "Texto 2", 
        height=300, 
        key="texto2", 
        value=st.session_state.texto2
    )

# --- Botones de acción ---
# El botón de limpiar restablece el estado de la aplicación.
# Se usa st.session_state para manejar el estado de las áreas de texto.
if st.button("Limpiar campos"):
    st.session_state.texto1 = ""
    st.session_state.texto2 = ""
    st.session_state.resultado = ""
    st.experimental_rerun()


# El botón de procesar se ejecuta y calcula el resultado.
if st.button("Procesar"):
    # Acceder a los valores desde st.session_state
    lista1 = st.session_state.texto1.split("\n")
    lista2 = st.session_state.texto2.split("\n")

    resultado_str = ""
    # Usar min() para asegurar que el bucle no exceda el texto más corto
    for i in range(min(len(lista1), len(lista2))):
        resultado_str += f"{lista1[i]}\n{lista2[i]}\n"
    
    # Almacenar el resultado en el estado de la sesión
    st.session_state.resultado = resultado_str

# Mostrar el resultado desde el estado de la sesión
st.text_area("Resultado", st.session_state.resultado, height=400)
    
# Botón para copiar el resultado al portapapeles
# La función se llama con el texto que se quiere copiar desde el estado de la sesión
copy_to_clipboard_button("Copiar resultado", st.session_state.resultado)
