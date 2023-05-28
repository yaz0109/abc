import streamlit as st
import numpy as np
import pandas as pd

def INTRODUCCION():
    st.title("RED DE TUBERÍAS")
    st.write("Las redes de tuberías son sistemas de tuberías interconectadas que se utilizan para transportar diferentes tipos de fluidos, la construcción y diseño de estos sistemas es muy importante tomando en cuenta el objetivo que esta debe de cumplir, así como las características del fluido a transportar y las especificaciones para garantizar la eficiencia del sistema.")
    st.write("Este tipo de sistemas son comúnmente utilizados en diversas áreas de la ingeniería y procesos de la industria, como conductores de líquidos y gases ya sea potables, reciclables o de deshecho. ")
   
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
    
    st.write("¡Hola! Haz clic en el botón para ver los globos.")

    if st.button("Mostrar globos"):
         st.balloons()
        
if __name__ == '__main__':
    INTRODUCCION()
