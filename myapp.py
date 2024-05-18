import streamlit as st

def baloes():
    st.balloons()

st.subheader("Nada não :)")
v1 = st.button("Clique aqui (2x)")

if 'show_text' not in st.session_state:
    st.session_state.show_text = False

def toggle_text():
    st.session_state.show_text = not st.session_state.show_text

if st.session_state.show_text:
    st.subheader("18 anos já? velha demais em, credo. Já pode ser presa agora.")
    st.subheader("PARABÉNS DODORA!! Muitos anos de vida e saúde, tmj.")

if v1:
    toggle_text()

if v1:
    baloes()
