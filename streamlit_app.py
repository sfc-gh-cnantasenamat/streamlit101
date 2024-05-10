import streamlit as st
import pandas as pd 
import time
import altair as alt

st.title('My first Streamlit app 🎈')

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)

df = load_data()


st.header("1. Inspect the data 🔍")
st.write("`st.data_editor` allows us to display AND edit data")
st.data_editor(df)

st.header("2. Get started with a simple bar chart 📊")
st.write("Let's chart the US state population data from the year 2019")
st.bar_chart(df[['year','states','population']],
            x='states',
            y='population')

st.header("3. Now make it interactive 🪄")
st.write("It's your turn to select a year")

# Using st.selectbox
selected_year = st.selectbox('Select a year',
                             list(df.year.unique())[::-1])

# st.write("Or maybe you prefer a slider 🛝")
# slider_selected_year = st.slider("Select a year", 2010, 2019)

# st.write("Or `st.number_input`")
#selected_year = st.number_input('Enter a year',
#                                placeholder='Enter a year from 2010-2019',
#                                value=2019)

if selected_year:
    df_selected_year = df[df.year == selected_year]
    
    # Display chart
    st.bar_chart(df_selected_year,
                 x='states',
                 y='population')

st.header("4. How about a line chart? 📉")
st.write("Track changes over time")
df_line_chart = df.copy()
df_line_chart['year'] = df_line_chart['year'].astype(str)
c = (
   alt.Chart(df_line_chart)
    .mark_line()
    .encode(x=alt.X('year'), 
            y=alt.Y('population'),
            color='states',)
)
st.altair_chart(c, use_container_width=True)

st.header("5. Sprinkle in more interactivity 🪄")
states = st.multiselect("Pick your states", list(df.states.unique())[::-1], "California")
date_range = st.slider(
    "Pick your date range",
    2010, 2019, (2010, 2019))

if states:
    chart_data = df[df['states'].isin(states)]
    chart_data = chart_data[chart_data['year'].between(date_range[0],date_range[1])]
    chart_data['year'] = chart_data['year'].astype(str)

    c = (
       alt.Chart(chart_data)
        .mark_line()
        .encode(x=alt.X('year'), 
                y=alt.Y('population'),
                color='states',)
    )
    
    st.altair_chart(c, use_container_width=True)
