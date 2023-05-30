import streamlit as st
import numpy as np
import pandas as pd

def ESPECIFICACIONES ():

    
    
    st.markdown(f"<h2 style='text-align: center;'> ESPECIFICACIONES DE LA RED TUBERÍAS </h2>", unsafe_allow_html=True)
    
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué tubería de acero? </h3>", unsafe_allow_html=True)
    st.write ()

    st.write ("Existen varias razones por las que se utilizará el acero como material para tuberías en las redes de tubería. Algunas de las razones son las siguientes:")
    st.write ("1.	Resistencia: El acero es un material muy resistente y duradero. Tiene una alta resistencia a la tracción, lo que significa que puede soportar una gran cantidad de peso y tensión sin deformarse o romperse.")
    st.write ("2.	Durabilidad: Las tuberías de acero son resistentes a la corrosión y pueden durar décadas sin necesidad de mantenimiento. Esto las hace ideales para su uso en aplicaciones de alta presión y temperatura.")
    st.write ("3.	Seguridad: Las tuberías de acero son muy seguras, ya que son resistentes al fuego y no se queman fácilmente. También son capaces de soportar terremotos y otros desastres naturales, lo que las convierte en una opción ideal para sistemas de tuberías en áreas de riesgo sísmico.")
    st.write ("4.	Economía: Aunque el costo inicial de la instalación de tuberías de acero puede ser mayor que el de otros materiales, su durabilidad y resistencia a largo plazo pueden hacer que sean más económicas a largo plazo. Además, el acero es fácil de fabricar y transportar, lo que puede ayudar a reducir los costos.")
    st.write ("5.	Versatilidad: Las tuberías de acero se pueden utilizar en una amplia variedad de aplicaciones, incluyendo sistemas de agua potable, gasoductos, oleoductos, sistemas de calefacción y refrigeración, entre otros. También pueden ser fabricadas en una variedad de tamaños y formas para adaptarse a las necesidades específicas de cada proyecto.")

    st.markdown(f"<h3    style='text-align: center;'> Cédula 40 </h3>", unsafe_allow_html=True)
    st.write ("La "Cédula" en tuberías de acero es un término que se refiere a la pared de la tubería y se utiliza para indicar su espesor. La cédula a usar, en nuestro caso, la cédula 40, se refiere a un espesor de pared de 0,109 pulgadas (2,77 mm) y es una de las cédulas más comunes utilizadas en tuberías de acero.")
    st.write ("La razón por la que la cédula 40 es tan común en tuberías de acero es porque tiene un equilibrio ideal entre resistencia y costo. Es lo suficientemente gruesa como para soportar la presión y el peso necesarios para muchas aplicaciones, pero no es tan gruesa que resulte prohibitivamente costosa.")
    st.write ("Además, la cédula 40 es compatible con muchos accesorios de tubería estándar, lo que facilita la instalación y el mantenimiento. También es comúnmente utilizada en aplicaciones de tubería que requieren una presión moderada, como en sistemas de agua y gas.")
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué se usan codos? </h3>", unsafe_allow_html=True)
    st.write ()
    st.write ("El diseño de la red de tubería tiene variaciones en la elevación por ende será necesario cambiar la dirección del flujo del fluido para ella (según el libro de Crane). Accesorios: Los acoplamientos o accesorios para conexión se clasifican en: de derivación, reducción, ampliación y desviación. Los accesorios como tes, cruces, codos con salida lateral, etc., pueden agruparse como accesorios de derivación. Los conectores de reducción o ampliación son aquellos que cambian la superficie de paso del fluido. En esta clase están las reducciones y los manguitos. Los accesorios de desvío, curvas, codos, curvas en D, etc., son los que cambian la dirección de flujo. Se pueden combinar algunos de los accesorios de la clasificación general antes mencionada. Además, hay accesorios como conexiones y uniones que no son resistentes al flujo, motivo por el cual no se consideran aquí.")
    st.write () 
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué se usan Válvulas de compuerta? </h3>", unsafe_allow_html=True)








if __name__ == '__main__':
    ESPECIFICACIONES()