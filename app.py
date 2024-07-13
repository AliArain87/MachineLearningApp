import streamlit as st
import pickle 


st.title("Machine Learning App🙄")


def load_model():
        model = pickle.load(open('model.pkl', 'rb'))
        return model

with st.sidebar:
    st.title("Sidebar")
    st.header("This app will predict your diabetes status (Dedicate to Sher Afzal)")
    check = st.checkbox("Load Model")

if check:
    load_model()
    st.warning("Model Loaded Successfully")
   



#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age


    ## User Input
    Pregnancies = st.number_input("Enter Pregnancies", min_value=0, max_value=20, value=3)
    Glucose = st.number_input("Enter Glucose", min_value=0, max_value=200, value=110)
    BloodPressure = st.number_input("Enter BloodPressure", min_value=70, max_value=180, value=120)
    SkinThickness = st.number_input("Enter SkinThickness", min_value=0, max_value=50, value=20)
    Insulin = st.number_input("Enter Insulin", min_value=0, max_value=600, value=100)
    BMI = st.number_input("Enter BMI", min_value=0, max_value=60, value=30)
    DiabetesPedigreeFunction = st.number_input("Enter DiabetesPedigreeFunction", min_value=0, max_value=2, value=1)
    Age = st.number_input("Enter Age", min_value=25, max_value=87, value=30)



## Prediction
btn = st.button("Predict")

if btn:
    data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    model = load_model()
    prediction = model.predict(data)
    if prediction == 1:
        st.write("Diabetic")
        # recommendation
        st.warning("Please consult with your doctor")
        st.error("Please take care of your health")
        # show the dr name and his contact detials
        st.info("Dr. Sher Afzal")
        st.info("📞Contact: 123-456-789")
    else:
        st.write("Not Diabetic")