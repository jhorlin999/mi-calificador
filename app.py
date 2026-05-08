import streamlit as st

st.title("Sistema de Calificaciones")

contraseña = st.text_input("Ingresa la contraseña:", type="password")

if contraseña == "ALFARO":
    st.success("Acceso correcto")
    nota = st.number_input("Ingresa tu nota (0 a 20):", min_value=0, max_value=20, step=1)
    
    if st.button("Verificar"):
        if nota <= 10:
            st.error("Estas desaprobado")
        elif 11 <= nota <= 13:
            st.warning("Estas regular")
        elif 14 <= nota <= 17:
            st.info("Estas bueno")
        else:
            st.success("Estas excelente")
