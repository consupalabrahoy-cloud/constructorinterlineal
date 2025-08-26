import streamlit as st

# Función para copiar al portapapeles usando HTML y JavaScript
def copy_to_clipboard_button(label, text_to_copy):
    """
    Crea un botón que copia el texto dado al portapapeles.
    """
    # Se usa una clave única para cada botón para evitar errores de renderizado en Streamlit
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

col1, col2 = st.columns(2)

with col1:
    texto1 = st.text_area("Texto 1", height=300)

with col2:
    texto2 = st.text_area("Texto 2", height=300)

if st.button("Procesar"):
    lista1 = texto1.split("\n")
    lista2 = texto2.split("\n")

    resultado_str = ""
    # Se utiliza min() para asegurar que el bucle no exceda el texto más corto
    for i in range(min(len(lista1), len(lista2))):
        resultado_str += f"{lista1[i]}\n{lista2[i]}\n"

    # Mostrar el resultado
    st.text_area("Resultado", resultado_str, height=400, key="resultado_final")
    
    # Botón para copiar el resultado al portapapeles
    # La función se llama con el texto que se quiere copiar
    copy_to_clipboard_button("Copiar resultado", resultado_str)

