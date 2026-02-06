# 🩺 Multiple Disease Prediction System

A Machine Learning–based web application that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson’s Disease** using user-provided medical data.  
The application is built with **Streamlit** for the frontend and trained ML models for prediction.

---

## 🚀 Features

- 🔹 Predicts **Diabetes**, **Heart Disease**, and **Parkinson’s Disease**
- 🔹 User-friendly web interface using Streamlit
- 🔹 Real-time predictions based on input parameters
- 🔹 Modular and scalable project structure
- 🔹 Easy to run locally

---

## 🧠 Diseases Covered

1. **Diabetes Prediction**
2. **Heart Disease Prediction**
3. **Parkinson’s Disease Prediction**

Each prediction uses a pre-trained Machine Learning model stored locally.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn  
- **Model Storage:** Pickle (`.sav` files)  
- **IDE:** VS Code  

---

## 📁 Project Structure

Multiple-Disease-Prediction-System/
│
├── app.py # Main Streamlit application
├── models/ # Trained ML models
│ ├── diabetes_model.sav
│ ├── heart_disease_model.sav
│ └── parkinsons_model.sav
│
├── .gitignore
├── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jainpoornimar/Multiple-Disease-Prediction-System.git
cd Multiple-Disease-Prediction-System
2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

3️⃣ Install dependencies
pip install streamlit scikit-learn streamlit-option-menu

▶️ Run the Application
streamlit run app.py


Then open your browser and go to:

http://localhost:8501



📌 Future Enhancements

Add more diseases

Improve UI/UX design

Deploy the app on Streamlit Cloud

Add authentication (login/register)

Improve model accuracy

👩‍💻 Author

Poornima 

GitHub: @jainpoornimar

Portfolio: https://jainpoornimar.github.io/portfolio/

⭐ Acknowledgements

Streamlit Documentation

Scikit-learn Community

Open-source datasets used for training
