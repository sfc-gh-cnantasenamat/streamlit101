# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# st.write('Hello world!')

# App title
st.title('🎈 My First Streamlit App')

# Load CSV data
df = pd.read_csv('data/us-population-2010-2019.csv', index_col=0)

# Year selectbox
# selected_year = st.selectbox('Select a year', list(df.year.unique())[::-1])

# Year number_input
selected_year = st.number_input('Enter a year',
                                 placeholder='Enter a  year from 2010-2019',
                                 value=2019)

# Display data subset
df_selected_year = df[df.year == selected_year]
df_selected_year

st.area_chart(df_selected_year, x='states', y='population')
