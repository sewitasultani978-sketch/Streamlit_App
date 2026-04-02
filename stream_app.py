import streamlit as st 
import pandas as pd 
import joblib 

model = joblib.load("car_price_model.pkl")
st.title("Car-Price-App")
st.write("Fyll i bilens information och klicka Predict för att få pris.")

df = pd.read_csv("car_price_dataset.csv", sep=";")
brand_list = sorted(df["Brand"].unique())
model_list = sorted(df["Model"].unique())
fuel_list = sorted(df["Fuel_Type"].unique())
transmission_list = sorted(df["Transmission"].unique())

brand = st.selectbox("Brand", brand_list)
model_name = st.selectbox("Model", model_list)
year = st.selectbox("Year", range(1990, 2025), index=25)
mileage = st.number_input("Mileage (km)", min_value=0, max_value=500000, value=100000, step=1000)
fuel_type = st.selectbox("Fuel Type", fuel_list)
transmission = st.selectbox("Transmission", transmission_list)
input_data = pd.DataFrame({
    "Brand": [brand],
    "Model": [model_name],
    "Year": [year],
    "Mileage": [mileage],
    "Fuel_Type": [fuel_type],
    "Transmission": [transmission]
})

if st.button("Predict Price"):
    predicted_price = model.predict(input_data)[0]
    st.write(f"Estimated Price: {predicted_price:.2f} kr") 