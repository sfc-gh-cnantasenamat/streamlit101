# Import libraries
import streamlit as st
import pandas as pd
import time
#import plotly.express as px

#st.write('Hello world!')

# App title
st.title('🎈 My First Streamlit App')

# Load CSV data

#df = pd.read_csv('data/us-population-2010-2019.csv', index_col=0)


# Caching data
# Not using st.cache_data
x0 = time.time()
df = pd.read_csv('data/us-population-2010-2019.csv', index_col=0)
x1 = time.time()


# Using st.cache_data
t0 = time.time()
@st.cache_data
def load_data():
  return pd.read_csv('data/us-population-2010-2019.csv', index_col=0)

df = load_data()
t1 = time.time()

with st.expander('Benchmarks'):
  st.write('Not using st.cache_data', (x1-x0)*1000, 'milliseconds')
  st.write('Using st.cache_data', (t1-t0)*1000, 'milliseconds')


# Year selection
# Using st.selectbox
selected_year = st.selectbox('Select a year', list(df.year.unique())[::-1])

# Using st.number_input
#selected_year = st.number_input('Enter a year',
#                                 placeholder='Enter a  year from 2010-2019',
#                                 value=2019)


# Display data subset
df_selected_year = df[df.year == selected_year]
st.dataframe(df_selected_year, height=250, use_container_width=True)


# Display chart
st.bar_chart(df_selected_year, x='states', y='population')
