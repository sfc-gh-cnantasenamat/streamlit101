# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import time

# st.write('Hello world!')

# App title
st.title('🎈 My First Streamlit App')

# Load CSV data
t0 = time.time()
df = pd.read_csv('data/us-population-2010-2019.csv', index_col=0)
t1 = time.time()
ms = (t1-t0)*1000
st.write(ms)

# Year selectbox
selected_year = st.selectbox('Select a year', list(df.year.unique())[::-1])

# Year number_input
#selected_year = st.number_input('Enter a year',
#                                 placeholder='Enter a  year from 2010-2019',
#                                 value=2019)

# Display data subset
df_selected_year = df[df.year == selected_year]
st.dataframe(df_selected_year, height=250, use_container_width=True)

st.area_chart(df_selected_year, x='states', y='population')
