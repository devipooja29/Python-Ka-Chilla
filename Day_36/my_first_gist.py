import streamlit as st
from streamlit_embedcode import github_gist

link = "https://gist.github.com/devipooja29/7c29d045e22bdfb1093b83184d2a27da"

st.title('''
         Embed Github Gist''')

github_gist(link)