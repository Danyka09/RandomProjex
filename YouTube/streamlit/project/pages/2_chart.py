import streamlit as st
import pandas as pd
import numpy as np

#generates random chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# makes chart
st.bar_chart(chart_data)
st.line_chart(chart_data)