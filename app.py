import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="Multiple Disease Prediction System", layout="wide")

# --------------------------------------------------
# Load Models (portable paths)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(
    open(os.path.join(BASE_DIR, "models", "diabetes_model.sav"), "rb")
)

heart_disease_model = pickle.load(
    open(os.path.join(BASE_DIR, "models", "heart_disease_model.sav"), "rb")
)

parkinsons_model = pickle.load(
    open(os.path.join(BASE_DIR, "models", "parkinsons_model.sav"), "rb")
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Home",
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Prediction",
        ],
        icons=["house", "activity", "heart", "person"],
        default_index=0,
    )

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if selected == "Home":
    st.markdown(
        "<h1 style='text-align:center; color:#008080;'>Welcome to Multiple Disease Prediction System</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            background-image:url('https://images.unsplash.com/photo-1544022618-7d5f4db7b098');
            background-size:cover;
            padding:40px;
            border-radius:15px;
            text-align:center;
            color:white;">
            <h2>AI powered health prediction</h2>
            <p>Predict Diabetes, Heart Disease & Parkinson’s using Machine Learning</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# DIABETES PREDICTION
# --------------------------------------------------
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
        SkinThickness = st.number_input("Skin Thickness")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function")

    with col2:
        Glucose = st.number_input("Glucose Level")
        Insulin = st.number_input("Insulin Level")
        Age = st.number_input("Age", min_value=1)

    with col3:
        BloodPressure = st.number_input("Blood Pressure")
        BMI = st.number_input("BMI")

    if st.button("Diabetes Test Result"):
        prediction = diabetes_model.predict(
            [[
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]]
        )

        if prediction[0] == 1:
            st.error("The person is diabetic")
        else:
            st.success("The person is not diabetic")

# --------------------------------------------------
# HEART DISEASE PREDICTION
# --------------------------------------------------
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1)
        trestbps = st.number_input("Resting Blood Pressure")
        restecg = st.number_input("Resting ECG")

    with col2:
        sex = st.number_input("Sex (0 = Female, 1 = Male)")
        chol = st.number_input("Serum Cholesterol")
        thalach = st.number_input("Max Heart Rate")

    with col3:
        cp = st.number_input("Chest Pain Type")
        fbs = st.number_input("Fasting Blood Sugar > 120")
        exang = st.number_input("Exercise Induced Angina")

    oldpeak = st.number_input("ST Depression")
    slope = st.number_input("Slope")
    ca = st.number_input("Major Vessels")
    thal = st.number_input("Thal")

    if st.button("Heart Disease Test Result"):
        prediction = heart_disease_model.predict(
            [[
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]]
        )

        if prediction[0] == 1:
            st.error("The person has heart disease")
        else:
            st.success("The person does not have heart disease")

# --------------------------------------------------
# PARKINSONS PREDICTION
# --------------------------------------------------
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    inputs = []
    cols = st.columns(5)

    labels = [
        "Fo", "Fhi", "Flo", "Jitter%", "Jitter Abs",
        "RAP", "PPQ", "DDP", "Shimmer", "Shimmer dB",
        "APQ3", "APQ5", "APQ", "DDA", "NHR",
        "HNR", "RPDE", "DFA", "Spread1", "Spread2",
        "D2", "PPE"
    ]

    for i, label in enumerate(labels):
        with cols[i % 5]:
            inputs.append(st.number_input(label))

    if st.button("Parkinson's Test Result"):
        prediction = parkinsons_model.predict([inputs])

        if prediction[0] == 1:
            st.error("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")
