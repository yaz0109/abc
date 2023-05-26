import streamlit as st
import numpy as np
import pandas as pd
import math
#___________________________________
import INTRODUCCIÓN as itr
def main():

    image_url = "https://i.pinimg.com/564x/a7/db/1c/a7db1c37805f8ddb1a34f70c94f4784e.jpg"
    st.image(image_url, use_column_width=True, caption=".")

    seleccion = st.selectbox("Seleccione una opción:", ["INTRODUCCIÓN", "PROGRAMA", "FUENTES BIBLIOGRAFICAS"])

    if seleccion == "INTRODUCCIÓN":
        st.subheader("INTRODUCCIÓN")
        itr.INTRODUCCIÓN()

    elif seleccion == "PROGRAMA":
        st.subheader("PROGRAMA")

        bs.PROGRAMA()

    elif seleccion == "FUENTES BIBLIOGRAFICAS":
        st.subheader("FUENTES BIBLIOGRAFICAS")

        fb.FUENTESBIBLIOGRAFICAS()  
        
        
   

if __name__ == "__main__":
    main()
