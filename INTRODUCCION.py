import streamlit as st
import numpy as np
import pandas as pd

def INTRODUCCION():
    st.title("RED DE TUBERÍAS")
    st.write("La mecánica de fluidos es una rama de la física que estudia el comportamiento de los fluidos, tanto líquidos como gases, y las fuerzas que actúan sobre ellos. Se ocupa del estudio de las propiedades físicas de los fluidos, como la densidad, la presión, la viscosidad y el caudal, así como de los principios que rigen el flujo de los fluidos.")
    st.write("La mecánica de fluidos tiene una amplia gama de aplicaciones en diversas áreas de la ciencia y la ingeniería. Algunas de las aplicaciones generales de la mecánica de fluidos es el diseño de sistemas de suministro de agua y saneamiento, en la planificación de sistemas de drenaje y en el análisis de la resistencia de estructuras expuestas a corrientes de agua, como puentes y presas.")
    st.write("Este tipo de sistemas son comúnmente utilizados en diversas áreas de la ingeniería y procesos de la industria, como conductores de líquidos y gases ya sea potables, reciclables o de deshecho. ")
   
    st.write("En esta web interactiva se busca determinar ciertos valores de una red de tuberías, a partir de ciertos principios manejados en un curso de mecánica extendido.")
    st.write("Una red de tuberías es un sistema de transporte de fluidos que consta de una serie de tubos interconectados que permiten el flujo de líquidos, gases u otros tipos de fluidos de un punto a otro. Estas redes se utilizan ampliamente en diversas aplicaciones, como el suministro de agua potable, el transporte de petróleo y gas, el sistema de alcantarillado, la distribución de productos químicos, entre otros.")
    st.write("Se estableció la disposición de la red de tuberías al considerar. ")
    st.write("La red que tenemos en este diseño, consta de material de acero, diámetros ajustables, longitudes y alturas definidas." )
    st.write("El objetivo es que quien entienda y haga uso del sistema, pueda agregar las especificaciones pertinentes, que le atribuirán un diseño de tuberías optimo; todo ello en función del caudal de alimentación desde el nodo A, por ende, las respectivas descargas en nodos J, M, U y Z. Asignando también la energía total por unidad de peso del fluido (agua e 25 a 60 °C), HGL de alimentación ") 

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
