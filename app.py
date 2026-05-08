import streamlit as st

# 1. Configuración de página (Oculta el menú desplegable predeterminado)
st.set_page_config(
    page_title="Sistema de Calificaciones",
    initial_sidebar_state="collapsed",
)

# 2. Código CSS para ocultar TODO (Botón Share, icono GitHub, Footer y Header)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display: none;}
            [data-testid="stStatusWidget"] {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- ABAJO SIGUE TU CÓDIGO NORMAL ---

st.title("Sistema de Calificaciones")

contraseña = st.text_input("Ingresa la contraseña:", type="password")

if contraseña == "ALFARO":
    st.success("Acceso correcto")
    nota = st.number_input("Ingresa tu nota (0 a 20):", min_value=0, max_value=20, step=1)
    
    if st.button("Verificar"):
        if nota <= 10:
            st.error(f"Nota: {nota} - Ni para eso")
        elif 11 <= nota <= 13:
            st.warning(f"Nota: {nota} - para dar pena siquiera")
        elif 14 <= nota <= 17:
            st.info(f"Nota: {nota} - peor es nada ")
        else:
            st.success(f"Nota: {nota} - alomenos ahi apruebas")
