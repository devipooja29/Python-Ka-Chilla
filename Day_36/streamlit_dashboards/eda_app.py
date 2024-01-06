# Importing libraries
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Webapp title
st.markdown('''
            # Exploratory Data Analysis (EDA) Web Application
            This app has been developed by Pooja Dinani while learning from Codanics.
            ''')

# Displaying Option for Upload File
with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    st.sidebar.markdown("[Example csv file](https://www.kaggle.com/c/titanic/data)")
    
# Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input Dataframe**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example dataset
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input Dataframe**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)