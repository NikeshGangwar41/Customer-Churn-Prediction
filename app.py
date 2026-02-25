import streamlit as st
import joblib
import numpy as np

# -------------------------
# Load model
# -------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("Bank Customer Churn Prediction")

st.write("Enter customer details:")

# -------------------------
# User Inputs
# -------------------------
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)

has_card = st.selectbox("Has Credit Card?", [0, 1])
is_active = st.selectbox("Is Active Member?", [0, 1])

salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# Geography selection
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Gender selection
gender = st.selectbox("Gender", ["Female", "Male"])

# -------------------------
# Convert Categorical Inputs
# -------------------------

# Geography Encoding
if geography == "Germany":
    geo_germany = 1
    geo_spain = 0
elif geography == "Spain":
    geo_germany = 0
    geo_spain = 1
else:  # France
    geo_germany = 0
    geo_spain = 0

# Gender Encoding
gender_male = 1 if gender == "Male" else 0

# -------------------------
# Prediction
# -------------------------
if st.button("Predict"):
    
    features = np.array([[credit_score, age, tenure, balance,
                          num_products, has_card, is_active,
                          salary, geo_germany, geo_spain,
                          gender_male]])
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"Customer is likely to EXIT ❌")
    else:
        st.success(f"Customer is likely to STAY ✅")

    st.write(f"Churn Probability: {probability:.2%}")