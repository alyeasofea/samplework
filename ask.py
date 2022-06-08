import streamlit as st

import numpy as np
import pandas as pd

st.header("My first Streamlit App")
st.title("This is a title")

st.write("""
# This is a first-level heading
## This is a second-level heading
Hello,welcome! This is my first web app!!!! <3
""")

st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))
