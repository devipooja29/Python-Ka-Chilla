import pandas as pd
import ydata_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns


df = sns.load_dataset('titanic')
pr = df.profile_report()

st_profile_report(pr)
