#  Customer Churn Prediction System

## 🌟 Project Overview

This project implements a complete **Techno-Functional Customer Churn Prediction System**. It uses machine learning to identify customers at high risk of leaving (churning) and translates the raw prediction probability into **actionable business risk categories (Low, Medium, High)**.

The goal is to enable the Customer Success team to execute targeted, proactive retention strategies *before* the customer is lost.

---

## Live Application:

The most crucial output is the live, interactive web application.

➡️ **[View the Live Churn Prediction App Here](https://customer-churn-prediction-system-yg3dsgenxvvjvjpbi7fmc3.streamlit.app)** ⬅️

*Built and deployed using Streamlit Community Cloud.*

---

##  Functional Insights:

The model uses **Logistic Regression** not just for prediction, but for its **interpretability**. By analyzing the coefficients, we identified the key drivers of customer behavior:

| Category | Strongest Predictors (High Risk) | Strongest Retention Factors (Low Risk) |
| :--- | :--- | :--- |
| **Commitment** | **Month-to-month contract** (Highest risk factor) | **Two-year contract** (Strongest retention factor) |
| **Support/Value**| Lack of **Tech Support** | Use of **Tech Support** |
| **Demographics**| **Senior Citizen** status | Long **Tenure** (high months as customer) |

### **Risk-Action Matrix**

The application automates business decisions based on the predicted probability:

| Risk Level | Probability Threshold | Action Triggered |
| :--- | :--- | :--- |
| **Low (Green)** | $\le 30\%$ | Monitor. |
| **Medium (Yellow)** | $30\% - 60\%$ | Automated follow-up email/survey. |
| **High (Red)** | $> 60\%$ | **Proactive Action Triggered:** Auto-assign to Customer Success Team for personalized outreach. |

---

## 🛠️ Technical Implementation

### **Data & Modeling**

* **Dataset:** Telco Customer Churn dataset.
* **Model:** **Logistic Regression**. Chosen for its stability and interpretability (coefficient analysis).
* **Metrics:** Focused on achieving high **Precision** (minimizing false positives to avoid wasting retention efforts) and **Recall** (minimizing false negatives to catch as many at-risk customers as possible).

### **Architecture & Deployment:**

customer-churn-predictor/
├── app/
│   └── app.py            # Streamlit Application Code (Live App Interface)
├── models/
│   └── churn_predictor_log_reg.pkl # Trained ML Model (Logistic Regression)
├── notebooks/
│   └── 1.0_Data_Exploration.ipynb  # EDA, Preprocessing, and Model Training
├── data/
│   └── WA_Fn-UseC_...csv   # Raw Dataset
└── requirements.txt      # Lists all Python dependencies for the deployment server

### **How to Run Locally**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Srijita-3/Customer-Churn-Prediction-System.git](https://github.com/Srijita-3/Customer-Churn-Prediction-System.git)
    cd Customer-Churn-Prediction-System
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # macOS/Linux
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit application:**
    ```bash
    streamlit run app/app.py
    ```
    The application will open in your default web browser at `http://localhost:8501`.

---
