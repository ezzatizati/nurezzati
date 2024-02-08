import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.svm import SVR
import pickle 

st.write("#Advertising Sales Prediction App")
st.write("This app predicts the **Advertising Sales** !")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.0, 300.0, 0.7)
    Radio = st.sidebar.slider('Radio', 0.0, 50.0, 1.0)
    Newspaper = st.sidebar.slider('Newspaper', 0.0, 200.0, 0.3)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)
modelAdvertising = pickle.load(open("modelAdvertising.h5", "rb"))
prediction = modelAdvertising.predict(df)


st.subheader('Prediction')
st.write(prediction)
