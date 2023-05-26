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
        ("INTRODUCCIÓN", "PROGRAMA", "FUENTES BIBLIOGRAFICAS","AGRADECIMIENTOS")
    )

    if opcion == "INTRODUCCIÓN":
        st.write("INTRODUCCIÓN:")
    elif opcion == "PROGRAMA":
        st.write("PROGRAMA:")
    elif opcion == "FUENTES BIBLIOGRAFICAS":
        st.write("FUENTES BIBLIOGRAFICAS:")

if __name__ == "__main__":
    main()
