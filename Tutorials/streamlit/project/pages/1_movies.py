import streamlit as st
import pandas as pd
import numpy as np

#reads data
data = pd.read_csv("movies.csv")
st.write(data)