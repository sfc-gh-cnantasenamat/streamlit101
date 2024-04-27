import streamlit as st
import pandas as pd 
import time

st.header('My App')

# Load data
#df = pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)
#df

# Caching data experiment

# Not using st.cache_data
#x0 = time.time()
#df1 = pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)
#x1 = time.time()

# Using st.cache_data
#t0 = time.time()
@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)

# df2 = load_data()
#t1 = time.time()

# Benchmark results
#with st.expander('Benchmark results'):
#    st.write('Not using st.cache_data', round((x1-x0)*1000, 3), 'milliseconds')
#    st.write('Using st.cache_data', round((t1-t0)*1000, 3), 'milliseconds')

df = load_data()

# Year selection
# Using st.number_input
#selected_year = st.number_input('Enter a year',
#                                placeholder='Enter a year from 2010-2019',
#                                value=2019)

# Using st.selectbox
selected_year = st.selectbox('Select a year',
                             list(df.year.unique())[::-1])

# Display data subset
df_selected_year = df[df.year == selected_year]
st.dataframe(df_selected_year, height=250, use_container_width=True)

# Display chart
st.bar_chart(df_selected_year,
             x='states',
             y='population')
