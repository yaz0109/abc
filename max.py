import streamlit as st
import numpy as np
import pandas as pd
import math

def main():
    st.title("Challenging situation")
    st.write("Pipe network stronghold")
    st.write("Pipe network design")
    texto_ingresado = st.text_input("Ingrese su texto", "Texto predeterminado")
    st.write("Texto ingresado:", texto_ingresado)
    st.title("Menú con 3 opciones")

    opcion = st.sidebar.radio(
        "Selecciona una opción:",
        ("Opción 1", "Opción 2", "Opción 3")
    )
    st.title("Botones para la selección de opciones")

    if st.button("Opción 1"):
        st.write("Has seleccionado la Opción 1")
    if st.button("Opción 2"):
        st.write("Has seleccionado la Opción 2")
    if st.button("Opción 3"):
        st.write("Has seleccionado la Opción 3")
    if opcion == "Opción 1":
        st.write("Has seleccionado la Opción 1")
    elif opcion == "Opción 2":
        st.write("Has seleccionado la Opción 2")
    elif opcion == "Opción 3":
        st.write("Has seleccionado la Opción 3")
if __name__ == "__main__":
     main()
