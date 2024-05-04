import streamlit as st
import pandas as pd 
import time
import altair as alt

st.header('My first Streamlit app 🎈')

@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)

df = load_data()

st.subheader("1. Inspect the data 🔍")
st.caption("`st.data_editor` allows us to display AND edit data")
st.data_editor(df)

# Year selection
# Using st.number_input
#selected_year = st.number_input('Enter a year',
#                                placeholder='Enter a year from 2010-2019',
#                                value=2019)

st.subheader("2. Get started with a simple bar chart 📊")
st.caption("Let's chart US state population data from the year 2019")

st.bar_chart(df[['year','states','population']],
            x='states',
            y='population')



st.subheader("Compare populations in different US states in a single year")

# Using st.selectbox
selected_year = st.selectbox('Select a year',
                             list(df.year.unique())[::-1])

# Display data subset
df_selected_year = df[df.year == selected_year]
# st.dataframe(df_selected_year, height=250, use_container_width=True)

# Display chart
st.bar_chart(df_selected_year,
             x='states',
             y='population')

st.subheader("Compare US state populations over time")
states = st.multiselect("Pick your states", list(df.states.unique())[::-1])
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
    # st.data_editor(chart_data[["states","population","year"]])

# st.write(chart_data)

# ca_data = df.loc[df['states'] == "California"]
# ca_chart_data = pd.DataFrame(ca_data, columns=["year", "population"])
# ca_chart_data['year'] = ca_chart_data['year'].astype(str)

# c = (
#    alt.Chart(ca_chart_data)
#     .mark_line()
#     .encode(x=alt.X('year:T'), 
#             y=alt.Y('population',scale=alt.Scale(domain=[37000000,40000000])))
# )

# # st.write(ca_data['population'].min())
# # st.write(ca_data['population'].max())
    #chart_data = chart_data[(chart_data['year'] >= daterange[0]) & (chart_data['year'] <= daterange[1])]

# st.subheader("California population over time")
# st.altair_chart(c, use_container_width=True)

    # c = (
    #    alt.Chart(chart_data)
    #     .mark_line()
    #     .encode(x=alt.X('year:T'), 
    #             y=alt.Y('population',scale=alt.Scale(domain=[30000000,50000000])))
    # )
