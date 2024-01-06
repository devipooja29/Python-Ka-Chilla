import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Making Containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Titanic Dataset App')
    st.text("In this project we will work on Titanic dataset.")

with data_sets:
    st.header("Titanic sank")
    st.text("In this project we will work on Titanic dataset.")

    # Importing data
    df = sns.load_dataset('Titanic')
    df = df.dropna()
    st.write(df.head(10))
    
    st.subheader("Distribution According to Class")
    st.bar_chart(df['sex'].value_counts())
    
    st.subheader("Distribution According to Class")
    st.bar_chart(df['class'].value_counts())
    
    st.bar_chart(df['age'].sample(10))
    
with features:
    st.header("These are our app features")
    st.text("Following are the features in this app:")
    st.markdown('1. **Feature 1:** Yet to decide')
    st.markdown('1. **Feature 2:** Yet to decide')
    st.markdown('1. **Feature 3:** Yet to decide')

    
with model_training:
    st.header("What happened to passengers of Titanic?")
    st.text("We will do model training.")
    # Making Columns
    input, display = st.columns(2)
    max_depth = input.slider("How many people do you know?", min_value=10, max_value=100, value=20, step=5)

# n-estimators
n_estimators = input.selectbox("How many trees should be there in a random forest", options=[50, 100, 200, 300, 'No limit'])

# Adding list of features
input.write(df.columns)

# Input features from user
input_features = input.text_input("Which feature we should use?")

# Machine Learning Model
# model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

if n_estimators == 'No limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
        
# Defining X and y
X = df[[input_features]]
y = df[['fare']]

# Fitting Model
model.fit(X,y)
pred = model.predict(X)

# Displaying Metrices
display.subheader('R Squared Error of the Model is: ')
display.write(r2_score(y, pred))
display.subheader('Mean Absolute Error of the Model is: ')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean Squared Error of the Model is: ')
display.write(mean_squared_error(y, pred))