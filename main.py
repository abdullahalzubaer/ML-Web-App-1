import streamlit as st
import pickle
import numpy as np


# Loading the pre-trained model and the encoders

def load_model():
    with open("saved_steps.pkl", 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

# Getting the pre-trained model, and label encoders from the pickle file

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Building streamlit application
# Creating the prediction page


def show_predict_page():
    st.title("Software Developer Salary Prediction")  # show title
    st.write("""### We need some information to predict the salary""")  # show text, and can use markdown syntax

    # All different choices for the country.
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Canada",
        "Germany",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    # Add two select box for countries and education

    # Depending on what we choose in the drop down box in the app, that will
    # be selected as the country or education. Then we can work with it as much as we want.

    country = st.selectbox("Country", countries)  # Countries can be tuple or list.
    education = st.selectbox("Education Level", education)
    experience = st.slider("Years of Experience", 0, 50, 3)  # Max 50, Min 0, Default 3

    # Adding button to start prediction, assigning it to a variable "ok"
    # True if we click else False
    ok = st.button("Calculate Salary")

    if ok:  # only if ok==True, we want to start the prediction.
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])  # first column
        X[:, 1] = le_education.transform(X[:, 1])  # second column
        X = X.astype(float)  # we want float array

        salary = regressor.predict(X)  # Predicting Salary

        st.subheader(f"The estimated salary is ${salary[0]:.2f}")


show_predict_page()
