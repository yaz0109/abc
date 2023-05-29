import math
import streamlit as st
import numpy as np
import pandas as pd

def LOL():

      st.write("RED DE TUBERÍAS")
      st.write()
      st.write("Aquí, se proporciona un croquis isométrico de la red de tuberías como ayuda visual."
            " Sin embargo, se necesitan algunas especificaciones para estas tuberías y "
            "esta es la situación de diseño que debe enfrentar  un ingeniero.")
      st.write()

      st.write("El objetivo de la red es suministrar agua en cuatro puntos  "
            "diferentes de una gran planta de proceso como parte de los servicios. "
            "Se han ideado unas válvulas de compuerta en la red, como se muestra, "
            "para que se pueda cortar el suministro en cualquiera de los cuatro puntos diferentes.")
      st.write()

      st.write(" Se estableció la disposición de la red de tuberías al considerar "
            "el equipo de proceso instalado, los soportes mecánicos de tubería "
            "plausibles y la seguridad. "
            "Sin embargo, no se determinaron los tamaños de las tuberías.")
      st.write()

      # Solicitar al usuario el valor de QA (caudal de alimentación)
      QA = st.number_input("Ingrese el valor de QA (caudal de alimentación): ")
      st.write()

      #DATOS
      # Declarar las variables de longitud de tuberías
      L1 = 74
      L2 = 113
      L3 = 73
      L4 = 198
      L5 = 22
      L6 = 13
      L7 = 61
      L8 = 33
      # Definir la velocidad constante
      velocidad = 1.5
      # Declarar los valores para gravedad, rugosidad, y viscosidad
      g= 9.81 # en m/s^2
      e= 4.60E-05  # en metros
      v= 1.085000E-06  # en m^2/s

      # Solicitar al usuario el valor de HGL en metros
      HGL = st.number_input("Ingrese el valor de HGL de alimentación (en metros): ")
