import streamlit as st
import pandas as pd
import seaborn as sns
import plotly_express as px
from sklearn.ensemble import RandomForestClassifier

st.write('''
         # Random Forest Classifier App
         This app predicts the **Iris flower** type based on its sepal length, sepal width, petal length and petal width.
         ''')

st.sidebar.header("User Input Paramters")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 0.1, 5.5, 2.1)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

iris = sns.load_dataset('iris')
st.subheader('Iris Dataset')
st.write(iris.head(10))

# st.subheader('Streamlit with Seaborn')
# plot1 = sns.barplot(data=iris, x='species', y='sepal_width')
# st.pyplot(plot1.figure)

st.subheader('Streamlit with Plotly')
fig = px.scatter(iris, x='sepal_length', y= 'petal_length', color= 'species')
st.plotly_chart(fig)

fig1 = px.box(iris, x='species', y= 'petal_length', color= 'species')
st.plotly_chart(fig1)

X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris['species']

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict(df)
prediction_proba = model.predict_proba(df)
st.subheader("Class labels and their corresponding index number")
st.write(iris['species'].unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
