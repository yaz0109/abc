import streamlit as st
import numpy as np
import pandas as pd

def INTRODUCCION():
    st.title("RED DE TUBERÍAS")
    st.write("Aquí, se proporciona un croquis isométrico de la red de tuberías como ayuda visual."
             " Sin embargo, se necesitan algunas especificaciones para estas tuberías y "
             "esta es la situación de diseño que debe enfrentar un ingeniero.")
    st.write("El objetivo de la red es suministrar agua en cuatro puntos "
             "diferentes de una gran planta de proceso como parte de los servicios. "
             "Se han ideado unas válvulas de compuerta en la red, como se muestra, "
             "para que se pueda cortar el suministro en cualquiera de los cuatro puntos diferentes.")
    st.write("Se estableció la disposición de la red de tuberías al considerar "
             "el equipo de proceso instalado, los soportes mecánicos de tubería "
             "plausibles y la seguridad. "
             "Sin embargo, no se determinaron los tamaños de las tuberías.") 

    col1, col2 = st.columns(2)
    col1.subheader('Columna 1')
    col1.write('Contenido de la columna 1')
    col2.subheader('Columna 2')
    col2.write('Contenido de la columna 2') 
    
    st.progress(progress_variable_1_to_100)
    st.balloons()
    st.snow()
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')
    st.exception(e)
