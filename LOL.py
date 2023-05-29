import math
import streamlit as st
import numpy as np
import pandas as pd

def main():

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
      
      # Mostrar los valores asignados
      st.write("Valores de longitud de tuberías:")
      st.write("L1 =", L1,"mts")
      st.write("L2 =", L2,"mts")
      st.write("L3 =", L3,"mts")
      st.write("L4 =", L4,"mts")
      st.write("L5 =", L5,"mts")
      st.write("L6 =", L6,"mts")
      st.write("L7 =", L7,"mts")
      st.write("L8 =", L8,"mts")
      st.write()
      # Calcular las variables establecidas
      Q6 = QA * 0.35
      Q7 = QA * 0.5
      Q8 = Q6 * 0.35

      # Sustituir en los demás caudales
      Q1 = QA - Q6
      Q2 = QA - Q6 + Q7
      Q3 = (3/4) * QA + Q8 + Q7 - Q6
      Q4 = Q6 - Q7 - Q8 - (1/2) * QA
      Q5 = Q6 - (1/4) * QA

      # Imprimir los resultados
      print("Variables establecidas:")
      print("Q1 =", Q1,"m3/s")
      print("Q2 =", Q2,"m3/s")
      print("Q3 =", Q3,"m3/s")
      print("Q4 =", Q4,"m3/s")
      print("Q5 =", Q5,"m3/s")
      print("Q6 =", Q6,"m3/s")
      print("Q7 =", Q7,"m3/s")
      print("Q8 =", Q8,"m3/s")
      print()

      def asignar_diametro(*caudales):
          data = [
              (0.00001, 0.00013, "1/8"),
              (0.00013, 0.00019, "1/4"),
              (0.00019, 0.00038, "3/8"),
              (0.00038, 0.00063, "1/2"),
              (0.00063, 0.00158, "3/4"),
              (0.00158, 0.00284, "1"),
              (0.00284, 0.00789, "1 1/4"),
              (0.00789, 0.01577, "1 1/2"),
              (0.01577, 0.03469, "2"),
              (0.03469, 0.08832, "2 1/2"),
              (0.08832, 0.15772, "3"),
              (0.15772, 0.28402, "3 1/2"),
              (0.28402, 0.50461, "4"),
              (0.50461, 1.17685, "5"),
              (1.17685, 2.64806, "6"),
              (2.64806, 5.94476, "8"),
              (5.94476, 11.86048, "10"),
              (11.86048, 22.23696, "12"),
              (22.23696, 40.01411, "14"),
              (40.01411, 71.20866, "16"),
              (71.20866, 126.7134, "18"),
              (126.7134, 224.9965, "20"),
              (224.9965, 524.8995, "24")
          ]

          diametros = []
          for caudal in caudales:
              diametro = None
              for item in data:
                  if item[0] <= caudal <= item[1]:
                      diametro = item[2]
                      break
              diametros.append(diametro)

          return diametros

      # Asignación de caudal
      caudal1 = abs(Q1)
      caudal2 = abs(Q2)
      caudal3 = abs(Q3)
      caudal4 = abs(Q4)
      caudal5 = abs(Q5)
      caudal6 = abs(Q6)
      caudal7 = abs(Q7)
      caudal8 = abs(Q8)


      diametros_asignados = asignar_diametro(caudal1, caudal2, caudal3, caudal4, caudal5, caudal6, caudal7, caudal8)

      # Guardar los valores de diámetro en una variable
      diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8 = diametros_asignados

      # Imprimir los valores de diámetro guardados en las variables
      st.write(f"El diámetro nominal asignado para caudal1 es: {diametro1}")
      st.write(f"El diámetro nominal asignado para caudal2 es: {diametro2}")
      st.write(f"El diámetro nominal asignado para caudal3 es: {diametro3}")
      st.write(f"El diámetro nominal asignado para caudal4 es: {diametro4}")
      st.write(f"El diámetro nominal asignado para caudal5 es: {diametro5}")
      st.write(f"El diámetro nominal asignado para caudal6 es: {diametro6}")
      st.write(f"El diámetro nominal asignado para caudal7 es: {diametro7}")
      st.write(f"El diámetro nominal asignado para caudal8 es: {diametro8}")
      st.write()

      def asignar_diametro_interno(diametros_nominales):
          resultados = []

          for d1 in diametros_nominales:
              if d1 == "1/8":
                  ID = 0.0068
              elif d1 == "1/4":
                  ID = 0.0092
              elif d1 == "3/8":
                  ID = 0.0125
              elif d1 == "1/2":
                  ID = 0.0158
              elif d1 == "3/4":
                  ID = 0.021
              elif d1 == "1":
                  ID = 0.0266
              elif d1 == "1 1/4":
                  ID = 0.0351
              elif d1 == "1 1/2":
                  ID = 0.0409
              elif d1 == "2":
                  ID = 0.0525
              elif d1 == "2 1/2":
                  ID = 0.0627
              elif d1 == "3":
                  ID = 0.0779
              elif d1 == "3 1/2":
                  ID = 0.0901
              elif d1 == "4":
                  ID = 0.1023
              elif d1 == "5":
                  ID = 0.1282
              elif d1 == "6":
                  ID = 0.1541
              elif d1 == "8":
                  ID = 0.2027
              elif d1 == "10":
                  ID = 0.2545
              elif d1 == "12":
                  ID = 0.3033
              elif d1 == "14":
                  ID = 0.3333
              elif d1 == "16":
                  ID = 0.

              else:
                  ID = "Indefinido"

              resultados.append(ID)

          return resultados



      # Obtener los valores de diámetro interno
      diametros_nominales = [diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8]
      diametros_internos = asignar_diametro_interno(diametros_nominales)

      # Guardar los valores de diámetro interno en variables individuales
      ID1, ID2, ID3, ID4, ID5, ID6, ID7, ID8 = diametros_internos

      # Imprimir los valores de diámetro interno
      st.write(f"El diámetro interno para caudal1 es: {ID1} mts")
      st.write(f"El diámetro interno para caudal2 es: {ID2} mts")
      st.write(f"El diámetro interno para caudal3 es: {ID3} mts")
      st.write(f"El diámetro interno para caudal4 es: {ID4} mts")
      st.write(f"El diámetro interno para caudal5 es: {ID5} mts")
      st.write(f"El diámetro interno para caudal6 es: {ID6} mts")
      st.write(f"El diámetro interno para caudal7 es: {ID7}""mts")
      st.write(f"El diámetro interno para caudal8 es: {ID8}""mts")
      st.write()

      st.write("Con todos estos valores se calculan los caudales reales de cada rama, para eso se hace uso del método de Hardy Cross")
      st.write()


      def calcular_area_diametro(diametro):
          radio = diametro / 2
          area = math.pi * (radio ** 2)
          return area


      A1 = calcular_area_diametro(ID1)
      A2 = calcular_area_diametro(ID2)
      A3 = calcular_area_diametro(ID3)
      A4 = calcular_area_diametro(ID4)
      A5 = calcular_area_diametro(ID5)
      A6 = calcular_area_diametro(ID6)
      A7 = calcular_area_diametro(ID7)
      A8 = calcular_area_diametro(ID8)

      st.write("Áreas de los diámetros:")
      st.write("Tubo 1:", A1,"mts^2")
      st.write("Tubo 2:", A2,"mts^2")
      st.write("Tubo 3:", A3,"mts^2")
      st.write("Tubo 4:", A4,"mts^2")
      st.write("Tubo 5:", A5,"mts^2")
      st.write("Tubo 6:", A6,"mts^2")
      st.write("Tubo 7:", A7,"mts^2")
      st.write("Tubo 8:", A8,"mts^2")
      st.write()

      st.write("Se sabe que en cada ramal existen accesorios, tanto codos como válvulas:")
      st.write("Para aquellos que tienen dichos artículos se asignan")

      
if __name__ == "__main__":
    main()
