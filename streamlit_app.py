import streamlit as st
import pandas as pd 
import time
import altair as alt

st.header('My App')

@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)

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

ca_data = df.loc[df['states'] == "California"]
ca_chart_data = pd.DataFrame(ca_data, columns=["year", "population"])

c = (
   alt.Chart(ca_chart_data)
    .mark_circle()
    .encode(alt.X('year',scale=alt.Scale(domain=[2010, 2019])), y="population", tooltip=["year", "population"])
)



# c.encode(Y('population', scale=Scale(domain=[2010, 2019])))
# c.encode(X('year', scale=Scale(domain=[2010, 2019])))

ca_data['population'].min.(axis=0)
ca_data['population'].max.(axis=0)

st.altair_chart(c, use_container_width=True)

# st.write(df.loc[df['states'] == "California"])
# st.subheader("California population over time")
# st.line_chart(df.loc[df['states'] == "California"])
