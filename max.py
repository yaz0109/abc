import streamlit as st
import numpy as np
import pandas as pd
import math

def main():

    image_url = "https://i.pinimg.com/564x/a7/db/1c/a7db1c37805f8ddb1a34f70c94f4784e.jpg"
    st.image(image_url, use_column_width=True, caption="Imagen centrada")

    seleccion = st.selectbox("Seleccione una opción:", ["INTRODUCCIÓN", "PROGRAMA", "FUENTES BIBLIOGRAFICAS"])

    if seleccion == "INTRODUCCIÓN":
        st.subheader("INTRODUCCIÓN")

        bs.INTRODUCCIÓN()

    elif seleccion == "PROGRAMA":
        st.subheader("PROGRAMA")

        bs.INTRODUCCIÓN()

    elif seleccion == "FUENTES BIBLIOGRAFICAS":
        st.subheader("FUENTES BIBLIOGRAFICAS")

        bs.FUENTESBIBLIOGRAFICAS()  
        
        
    st.title("Menú:")
    if st.button("INTRODUCCIÓN"):
        st.write("INTRODUCCIÓN:")
    if st.button("PROGRAMA"):
        st.write("PROGRAMA:")
    if st.button("FUENTES BIBLIOGRAFICAS"):
        st.write("FUENTES BIBLIOGRAFICAS")
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
