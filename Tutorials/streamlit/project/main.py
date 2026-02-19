import streamlit as st
import pandas as pd
import numpy as np

#write and input data
st.write("Hello world")
fav_movie = st.text_input("Whats ya favorite movie?")

st.write(f"Your fav movie is {fav_movie}")

st.link_button("Mortgage", url="/mortgage_calc")

#reads data
data = pd.read_csv("movies.csv")
st.write(data)

#generates random chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# makes chart
st.bar_chart(chart_data)
st.line_chart(chart_data)