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

            #Codos

      Codo1=3
      Codo2=4
      Codo3=2
      Codo4=7
      Codo5=0
      Codo6=0
      Codo7=4
      Codo8=0

      #Valores de K para accesorios

      kcodo=30
      kválvula=8

      #HARDY CROSS
      

      st.write("Cálculo de los caudales reales:")
      st.write("Para el cálculo de los nuevos caudales se realiza un proceso iterativo donde se incluye ajustar los valores iniciales para caudal a través de una corrección")
      st.write("gracias al cálculo de los hL (pérdidas del tubo correspondiente), igualando la suma de aquellos a 0:")

      # ITERACIONES

      st.write("Instrucciones para la búsqueda de los caudales reales")
      st.write("1.- Calcular los valores de los caudales en función al flujo")
      st.write("2.- Calcular el valor respectivo de número de Raynolds, con las dimensiones, el caudal y la viscosidad del fluido")
      st.write("3.- Obtener el valor de factor de fricción para el respectivo tubo")
      st.write("4.- Realizar la operación que ayuda a determinar la pérdida de fricción K del tubo")
      st.write("5.- Con el valor K, tabular el hL del tubo")
      st.write("6.- Determinar la corrección para el caudal, renombrarlo y continuar con la siguiente iteración")
      st.write("7.- En caso de tener un caudal en más de un circuito usar la corrección común para caudal total de este")
      
      
      # Cálculo de D/e
      D_e_1 = ID1/e
      D_e_2 = ID2/e
      D_e_3 = ID3/e
      D_e_4 = ID4/e
      D_e_5 = ID5/e
      D_e_6 = ID6/e
      D_e_7 = ID7/e
      D_e_8 = ID8/e

      #ITERACIÓN 1

      I=1




      #CIRCUITO 1
      Q1_I1=Q1
      Q7_I7=-1*Q7
      Q5_I5=-1*Q5
      Q6_I6=-1*Q6


      #CIRCUITO 1 (signos)



      Signo1=Q1_I1/(abs(Q1_I1))
      Signo7=Q7_I7/(abs(Q7_I7))
      Signo5=Q5_I5/(abs(Q5_I5))
      Signo6=Q6_I6/(abs(Q6_I6))




      # Calcular números de Raynolds
      Nre1= (abs(Q1_I1*ID1))/(A1*v)
      Nre7= (abs(Q7_I7*ID7))/(A7*v)
      Nre5= (abs(Q5_I5*ID5))/(A5*v)
      Nre6= (abs(Q6_I6*ID6))/(A6*v)

      # Calcular el factor de fricción fT

      fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
      fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
      fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
      fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

      K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
      K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
      K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
      K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL1=K1*(Q1_I1**2)*Signo1
      hL7=K7*(Q7_I7**2)*Signo7
      hL5=K5*(Q5_I5**2)*Signo5
      hL6=K6*(Q6_I6**2)*Signo6




      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ1=2*K1*abs(Q1_I1)
      kQ7=2*K7*abs(Q7_I7)
      kQ5=2*K5*abs(Q5_I5)
      kQ6=2*K6*abs(Q6_I6)




      # Calcular de deltaQ CIRCUITO 1

      SUMAhL1=hL1+hL7+hL5+hL6
      SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

      DeltaQ1=(SUMAhL1/SUMA2kQ1)




      Q1_I1=Q1_I1-DeltaQ1
      Q7_I7=Q7_I7-DeltaQ1
      Q5_I5=Q5_I5-DeltaQ1
      Q6_I6=Q6_I6-DeltaQ1





      #CIRCUITO 2
      Q2_I2=Q2
      Q7_I7_2=Q7
      Q8_I8=-1*Q8




      #CIRCUITO 2 (signos)
      Signo2=Q2_I2/(abs(Q2_I2))
      Signo7=Q7_I7_2/(abs(Q7_I7_2))
      Signo8=Q8_I8/(abs(Q8_I8))




      # Calcular números de Raynolds
      Nre2= (abs(Q2_I2*ID2))/(A2*v)
      Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
      Nre8= (abs(Q8_I8*ID8))/(A8*v)


      # Calcular el factor de fricción fT

      fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
      fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
      fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)


      K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
      K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
      K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL2=K2*(Q2_I2**2)*Signo2
      hL7=K7*(Q7_I7_2**2)*Signo7
      hL8=K8*(Q8_I8**2)*Signo8



      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ2=2*K2*abs(Q2_I2)
      kQ7=2*K7*abs(Q7_I7_2)
      kQ8=2*K8*abs(Q8_I8)



      # Calcular de deltaQ CIRCUITO 2

      SUMAhL1=hL2+hL7+hL8
      SUMA2kQ1=kQ2+kQ7+kQ8

      DeltaQ2=(SUMAhL1/SUMA2kQ1)

      Q2_I2=Q2_I2-DeltaQ2
      Q7_I7_2=Q7_I7_2-DeltaQ2
      Q8_I8=Q8_I8-DeltaQ2



      #CIRCUITO 3
      Q3_I3=Q3
      Q8_I8_2=Q8
      Q4_I4=-1*Q4



      #CIRCUITO 3 (signos)
      Signo3=Q3_I3/(abs(Q3_I3))
      Signo8=Q8_I8_2/(abs(Q8_I8_2))
      Signo4=Q4_I4/(abs(Q4_I4))



      # Calcular números de Raynolds
      Nre3= (abs(Q3_I3*ID3))/(A3*v)
      Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
      Nre4= (abs(Q4_I4*ID4))/(A4*v)


      # Calcular el factor de fricción fT

      fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
      fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
      fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)


      K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
      K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
      K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL3=K3*(Q3_I3**2)*Signo3
      hL8=K8*(Q8_I8_2**2)*Signo8
      hL4=K4*(Q4_I4**2)*Signo4



      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ3=2*K3*abs(Q3_I3)
      kQ8=2*K8*abs(Q8_I8_2)
      kQ4=2*K4*abs(Q4_I4)



      # Calcular de deltaQ CIRCUITO 3

      SUMAhL1=hL3+hL8+hL4
      SUMA2kQ1=kQ3+kQ8+kQ4

      DeltaQ3=(SUMAhL1/SUMA2kQ1)

      Q3_I3=Q3_I3-DeltaQ3
      Q8_I8_2=Q8_I8_2-DeltaQ3
      Q4_I4=Q4_I4-DeltaQ3




      #Caudales comunes

      Q7_I7=Q7_I7+DeltaQ2
      Q7_I7_2=Q7_I7_2+DeltaQ1
      Q8_I8=Q8_I8+DeltaQ3
      Q8_I8_2=Q8_I8_2+DeltaQ2



      #PORCENTAJES DE ERROR

      Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
      Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
      Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
      Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
      Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
      Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
      Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
      Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
      Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
      Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100





      #ITERACIÓN 2,3,4... (COPIAR CAUDALES ANTERIORES SOLAMENTE)

      iteracion = 2
      while iteracion <= 21:

          # Resto del código...

          #CIRCUITO 1 (signos)

          Signo1=Q1_I1/(abs(Q1_I1))
          Signo7=Q7_I7/(abs(Q7_I7))
          Signo5=Q5_I5/(abs(Q5_I5))
          Signo6=Q6_I6/(abs(Q6_I6))

          # Calcular números de Raynolds
          Nre1= (abs(Q1_I1*ID1))/(A1*v)
          Nre7= (abs(Q7_I7*ID7))/(A7*v)
          Nre5= (abs(Q5_I5*ID5))/(A5*v)
          Nre6= (abs(Q6_I6*ID6))/(A6*v)

          # Calcular el factor de fricción fT

          fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
          fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
          fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
          fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

          K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
          K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
          K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
          K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL1=K1*(Q1_I1**2)*Signo1
          hL7=K7*(Q7_I7**2)*Signo7
          hL5=K5*(Q5_I5**2)*Signo5
          hL6=K6*(Q6_I6**2)*Signo6

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ1=2*K1*abs(Q1_I1)
          kQ7=2*K7*abs(Q7_I7)
          kQ5=2*K5*abs(Q5_I5)
          kQ6=2*K6*abs(Q6_I6)

          # Calcular de deltaQ CIRCUITO 1

          SUMAhL1=hL1+hL7+hL5+hL6
          SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

          DeltaQ1=(SUMAhL1/SUMA2kQ1)

          Q1_I1=Q1_I1-DeltaQ1
          Q7_I7=Q7_I7-DeltaQ1
          Q5_I5=Q5_I5-DeltaQ1
          Q6_I6=Q6_I6-DeltaQ1

          #CIRCUITO 2

          #CIRCUITO 2 (signos)
          Signo2=Q2_I2/(abs(Q2_I2))
          Signo7=Q7_I7_2/(abs(Q7_I7_2))
          Signo8=Q8_I8/(abs(Q8_I8))

          # Calcular números de Raynolds
          Nre2= (abs(Q2_I2*ID2))/(A2*v)
          Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
          Nre8= (abs(Q8_I8*ID8))/(A8*v)

          # Calcular el factor de fricción fT

          fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
          fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
          fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)

          K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
          K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
          K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL2 = K2 * (Q2_I2 ** 2) * Signo2
          hL7 = K7 * (Q7_I7_2 ** 2) * Signo7
          hL8 = K8 * (Q8_I8 ** 2) * Signo8

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ2=2*K2*abs(Q2_I2)
          kQ7=2*K7*abs(Q7_I7_2)
          kQ8=2*K8*abs(Q8_I8)

          # Calcular de deltaQ CIRCUITO 2

          SUMAhL1=hL2+hL7+hL8
          SUMA2kQ1=kQ2+kQ7+kQ8

          DeltaQ2=(SUMAhL1/SUMA2kQ1)

          Q2_I2=Q2_I2-DeltaQ2
          Q7_I7_2=Q7_I7_2-DeltaQ2
          Q8_I8=Q8_I8-DeltaQ2

          #CIRCUITO 3

          #CIRCUITO 3 (signos)
          Signo3=Q3_I3/(abs(Q3_I3))
          Signo8=Q8_I8_2/(abs(Q8_I8_2))
          Signo4=Q4_I4/(abs(Q4_I4))

          # Calcular números de Raynolds
          Nre3= (abs(Q3_I3*ID3))/(A3*v)
          Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
          Nre4= (abs(Q4_I4*ID4))/(A4*v)

          # Calcular el factor de fricción fT

          fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
          fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
          fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)

          K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
          K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
          K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL3=K3*(Q3_I3**2)*Signo3
          hL8=K8*(Q8_I8_2**2)*Signo8
          hL4=K4*(Q4_I4**2)*Signo4

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ3=2*K3*abs(Q3_I3)
          kQ8=2*K8*abs(Q8_I8_2)
          kQ4=2*K4*abs(Q4_I4)

          # Calcular de deltaQ CIRCUITO 3

          SUMAhL1=hL3+hL8+hL4
          SUMA2kQ1=kQ3+kQ8+kQ4

          DeltaQ3=(SUMAhL1/SUMA2kQ1)

          Q3_I3=Q3_I3-DeltaQ3
          Q8_I8_2=Q8_I8_2-DeltaQ3
          Q4_I4=Q4_I4-DeltaQ3

          #Caudales comunes

          Q7_I7=Q7_I7+DeltaQ2
          Q7_I7_2=Q7_I7_2+DeltaQ1
          Q8_I8=Q8_I8+DeltaQ3
          Q8_I8_2=Q8_I8_2+DeltaQ2

          #PORCENTAJES DE ERROR

          Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
          Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
          Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
          Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
          Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
          Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
          Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
          Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
          Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
          Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100

      # Actualizar el valor de iteracion
          iteracion += 1

if __name__ == "__main__":
    main()
