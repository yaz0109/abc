import streamlit as st
import pandas as pd
df = pd.read_csv('https://raw.githubbusercontent.com/quantum-apps/mapa/main/data.csv') 
st.write(df)
st.map(df)
st.title ("Mi primera App")
#st.button("dale click")
#st.button("otro boton")
