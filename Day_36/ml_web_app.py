# Importing libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Web app title
st.title("Explore Different ML Models and Datasets")
st.write("Let's see which ML model works well to which dataset, select dataset and ML model from sidebar options.")

# Creating selectbox for datasets
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)

# Creating selectbox for ML models
classifier_name = st.sidebar.selectbox(
    'Select Classifier',
    ('KNN', 'SVM', 'Random Forest')
)

# Defining function for loading dataset
def get_dataset(dataset_name):
    data = None
    if dataset_name == 'Iris':
        data = datasets.load_iris()
    elif dataset_name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    x = data.data
    y = data.target
    return x, y

# Calling defined function
X, y = get_dataset(dataset_name)

# Printing shape of dataset
st.write("Shape of dataset:", X.shape)
st.write("Number of classes:", len(np.unique(y)))

# Defining function parameters of classifiers
def add_parameter_ui(classifier_name):
    params = dict()
    if classifier_name == 'SVM':
        C = st.sidebar.slider("C", 0.01, 10.0)
        params['C'] = C
    elif classifier_name == 'KNN':
        K = st.sidebar.slider("K", 1, 15)
        params['K'] = K
    else:
        max_depth = st.sidebar.slider("Max Depth", 2, 15)
        n_estimators = st.sidebar.slider("Number of Estimators", 1, 100)
        params['max_depth'] = max_depth
        params['n_estimators'] = n_estimators
    return params

# Calling the defined function
params = add_parameter_ui(classifier_name)

# Defining function for classifiers with parameters
def get_classifier(classifier_name, params):
    clf = None
    if classifier_name == 'SVM':
        clf = SVC(C=params['C'])
    elif classifier_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'],
                                     max_depth=params['max_depth'], random_state=1234)
    return clf

# Calling the function
clf = get_classifier(classifier_name, params)

# Spliting dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Training the classifier
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Printing accuracy
acc = accuracy_score(y_test, y_pred)
st.write(f'Classifier: {classifier_name}')
st.write(f'Accuracy: {acc}')

# Adding plot
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2,
            c=y, alpha=0.8,
            cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

st.pyplot(fig)