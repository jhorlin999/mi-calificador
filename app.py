import streamlit as st

st.title("Sistema de Calificaciones")

contraseña = st.text_input("Ingresa la contraseña:", type="password")

if contraseña == "ALFARO":
    st.success("Acceso correcto")
    nota = st.number_input("Ingresa tu nota (0 a 20):", min_value=0, max_value=20, step=1)
    
    if st.button("Verificar"):
        if nota <= 10:
            st.error("ni pa eso")
        elif 11 <= nota <= 13:
            st.warning("para dar pena siquiera")
        elif 14 <= nota <= 17:
            st.info("a nada")
        else:
            st.success("alomenos ahí, apruebas")
