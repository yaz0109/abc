import streamlit as st
import numpy as np
import pandas as pd

def PROGRAMA():
    st.title("DATOS DE ENTRADA")
    st.write("Resultado")
    table_data = {'Column 1': [1, 2], 'Column 2': [3, 4]}
    st.write(pd.DataFrame(data=table_data))
            
