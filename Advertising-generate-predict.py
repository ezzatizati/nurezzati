import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.svm import SVR

st.write("#Advertising Sales Prediction App")
st.write("This app predicts the **Advertising Sales** !")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 4.3, 7.9, 5.4)
    Radio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
    data = {'TV': TV,
            'Radio': Radio,
            'Newpaper': Newspaper,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


prediction = modelSVRAdvertising.predict(df)
prediction_proba = modelSVRAdvertising.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
