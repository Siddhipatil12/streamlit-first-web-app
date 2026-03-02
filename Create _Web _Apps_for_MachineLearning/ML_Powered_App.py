import streamlit as st 
import pickle
#pickle prepare machine learning dataset
import numpy as np

#Title
st.title("House Price Predictor")
#user input
area = st.number_input("Enter the area (sq ft):", 500, 10000)
rooms = st.slider("Number of rooms:", 1, 10)

#load data model
model = pickle.load(open("house_price_model.pkl", "rb"))
#Predict the price
if st.button("Predict Price"):
    features = np.array([[area, rooms]])
    prediction = model.predict(features)
    st.subheader(f"Predicted Price: ${prediction[0]:,.2f}")
