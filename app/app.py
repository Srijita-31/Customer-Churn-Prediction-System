import streamlit as st
import pandas as pd
import joblib
import os

# --- 1. CONFIGURATION AND MODEL LOADING ---

# Define paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'churn_predictor_log_reg.pkl')

# Load the trained model
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file not found! Please ensure 'churn_predictor_log_reg.pkl' is in the 'models' folder.")
    st.stop()
    
# --- 2. STREAMLIT APP LAYOUT AND INTERFACE ---

st.set_page_config(layout="centered")
st.title(" Customer Churn Prediction System")
st.subheader("Predicting 'At-Risk' Customers for Proactive Retention")

with st.expander("Functional Insights (from Model Analysis)"):
    st.markdown(
        """
        This prediction model is based on Logistic Regression. Key functional insights:
        - **High Retention:** Two-year contracts and use of technical support services (TechSupport_Yes).
        - **High Risk:** Month-to-month contracts, Senior Citizen status, and lack of online security/backup services.
        """
    )

# --- 3. INPUT FORM ---

st.sidebar.header("Customer Profile Input")

# Create inputs for the most important functional features
tenure = st.sidebar.slider("Tenure (Months as customer)", 0, 72, 24)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=18.0, max_value=118.0, value=70.0)

# The new Senior Citizen input
is_senior = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"]) 

contract_type = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])

# --- 4. PREDICTION LOGIC (MIMIC ENCODING) ---

# Updated function definition to include the new variable
def make_prediction(tenure, monthly_charges, contract_type, internet_service, tech_support, is_senior): 
    
    # 1. Create a dictionary where all features from the training set are initialized to 0
    # This ensures all 45+ expected features are present.
    feature_dict = {}
    for col in model.feature_names_in_:
        feature_dict[col] = 0
        
    # 2. Convert to DataFrame (essential for the model)
    input_data = pd.DataFrame([feature_dict])

    # 3. Set the numerical features
    input_data['tenure'] = tenure
    input_data['MonthlyCharges'] = monthly_charges
    
    # 4. Set the simple binary feature
    if is_senior == "Yes":
        input_data['SeniorCitizen'] = 1

    # 5. Set the one-hot encoded features
    if contract_type == "One year":
        input_data['Contract_One year'] = 1
    elif contract_type == "Two year":
        input_data['Contract_Two year'] = 1

    if internet_service == "Fiber optic":
        input_data['InternetService_Fiber optic'] = 1
    elif internet_service == "No":
        input_data['InternetService_No'] = 1

    if tech_support == "Yes":
        input_data['TechSupport_Yes'] = 1
    elif tech_support == "No internet service":
        input_data['TechSupport_No internet service'] = 1
        
    # NOTE: To hit 60%+, you may also need to manually set the 'No' dummy variables for 
    # other services (like OnlineSecurity_No) to 1 here, as they are not input fields.
    # For this final test, we rely on the Senior Citizen factor.

    # 6. Use the model to predict the probability of churn (1)
    churn_probability = model.predict_proba(input_data)[:, 1][0]
    
    return churn_probability

# --- 5. DISPLAY RESULTS ---

if st.button("Analyze Customer Risk"):
    # Updated function call to include the new variable
    churn_prob = make_prediction(tenure, monthly_charges, contract_type, internet_service, tech_support, is_senior)
    
    risk_level = ""
    if churn_prob < 0.3:
        risk_level = "Low Risk (Green)"
        st.success(f" Prediction: {risk_level}")
    elif churn_prob < 0.6:
        risk_level = "Medium Risk (Yellow)"
        st.warning(f"Prediction: {risk_level}")
    else:
        risk_level = "High Risk (Red)"
        st.error(f" Prediction: {risk_level}")
        
    st.metric(
        label="Probability of Churn", 
        value=f"{churn_prob*100:.2f}%"
    )
    
    # Functional Action Trigger
    if risk_level == "High Risk (Red)":
        st.info("""
        **Proactive Action Triggered:** Auto-assigning to Customer Success Team 
        with a recommendation to offer a **Contract Upgrade** or a **Premium Tech Support Trial**.
        """)