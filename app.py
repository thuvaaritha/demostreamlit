import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Research Study Dashboard")

daya = pd.DataFrame({
    "x" : np.arange(1,101),
    "y" : np.random.normal(0,1,100)
})

subset_size = st.slider("Selext the number of data points" , 10, 100, 50)