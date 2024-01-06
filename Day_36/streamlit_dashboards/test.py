import streamlit as st
import seaborn as sns

st.header("Working with Streamlit")
st.text("I am trying some functions of streamlit.")

st.header("Head of Iris dataset")

df = sns.load_dataset('iris')
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])