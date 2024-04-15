# Import libraries
import streamlit as st
import pandas as pd

# st.write('Hello world!')

# App title
st.title('🎈 My First Streamlit App')

# Load CSV data
df = pd.read_csv('data/us-population-2010-2019.csv', index_col=0)

# Year selector
year_list = list(df.year.unique())[::-1]

# selected_year = st.selectbox('Select a year', year_list)
selected_year = st.number_input('Enter a year',
                                 placeholder='Enter a  year from 2010-2019',
                                 format='string')

# Data processing
if selected_year:
  df_selected_year = df[df.year == selected_year]
  df_selected_year
