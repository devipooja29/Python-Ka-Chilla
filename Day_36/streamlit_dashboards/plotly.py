# Importing libraries
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Making app with streamlit and plotly")

# Importing dataset
df = px.data.gapminder()

# Printing data
st.write(df)
st.write(df.columns)

# Printing statistical summary
st.write(df.describe())

# Data management
year_option = df['year'].unique().tolist()
year = st.selectbox("Which year should we plot?", year_option, 0)
df = df[df['year']== year]

# Ploting
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='country', hover_name='country',
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90])
fig.update_layout(width=800, height=400)
st.write(fig)