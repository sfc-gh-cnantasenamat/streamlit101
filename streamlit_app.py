# Import libraries
import streamlit as st
import pandas as pd

# st.write('Hello world!')

# App title
# st.title('🎈 My First App')

# Load CSV data
df = pd.read_csv('data/us-population-2010-2019-reshaped.csv')
df
