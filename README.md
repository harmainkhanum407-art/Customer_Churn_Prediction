# 📊 Customer Churn Prediction & Retention Intelligence Platform

A machine learning and customer-retention project designed to identify customers who may be at risk of leaving a service and provide useful insights for retention actions.

## 🚀 Project Overview

Customer churn happens when a customer stops using a company's product or service. Predicting churn early can help a business understand which customers need attention and take action before they leave.

This project combines **Python, Machine Learning, data analysis, and an interactive Streamlit dashboard** to create a Customer Churn Intelligence Platform.

The application provides:

- Customer churn risk analysis
- Interactive executive dashboard
- Individual customer prediction and risk assessment
- Key factors that can contribute to churn
- Recommended retention strategy
- AI-assisted retention email generation
- Batch CSV customer scanning
- Visual analysis of customer churn patterns

## 🎯 Main Objectives

1. Predict which customers are more likely to churn.
2. Analyze customer behavior and identify important risk factors.
3. Present churn information through an easy-to-understand dashboard.
4. Help businesses prioritize high-risk customers.
5. Generate practical retention suggestions for at-risk customers.
6. Demonstrate how machine learning can support customer-retention decisions.

## 🧠 How the Project Works

The project follows a simple workflow:

```text
Customer Data
      ↓
Data Preparation & Analysis
      ↓
Churn Risk / Prediction Logic
      ↓
Risk Assessment
      ↓
Key Driver Analysis
      ↓
Retention Recommendation
      ↓
AI-Assisted Retention Email
```

## 📊 Dashboard Modules

### 1. Executive Retention Dashboard

The dashboard provides a high-level view of customer retention information. It displays metrics such as:

- Total monitored customers
- Overall churn rate
- Average revenue per user
- Customer churn distribution by tenure

The project uses Plotly visualizations to make the customer data easier to understand.

### 2. Customer Predictor & AI Agent

This module allows the user to enter customer information such as:

- Customer ID
- Tenure in months
- Monthly charges
- Usage decrease
- Support tickets
- Days since last purchase
- Contract type
- Payment method

After analysis, the application presents a churn-risk assessment and explains the factors contributing to that risk.

### 3. Key Risk Drivers

The system highlights customer characteristics that may increase churn risk, for example:

- Short customer tenure
- Significant decrease in usage
- Multiple support tickets
- Month-to-month contracts

This makes the prediction easier to interpret instead of showing only a final risk value.

### 4. Retention Strategy

For customers identified as high risk, the platform provides a recommended retention approach. This demonstrates how predictive analytics can be connected to a practical business action.

### 5. AI-Assisted Retention Email

The application generates a personalized draft retention email using the customer's risk factors. The email can be reviewed by a business/user before being sent.

### 6. Batch Churn Scanner

Users can upload a CSV file and preview customer data for batch analysis. This feature is useful when working with multiple customer records rather than checking customers individually.

## 🛠️ Technologies Used

- **Python** – application and data-processing logic
- **Pandas** – data manipulation and analysis
- **NumPy** – numerical operations
- **Scikit-learn** – machine-learning workflow/components
- **Streamlit** – interactive web application and dashboard
- **Plotly** – interactive data visualization
- **HTML/CSS** – dashboard styling where required
- **JavaScript** – web-related functionality where included

## 📁 Project Structure

```text
Customer_Churn_Prediction/
│
├── app.py                 # Main Streamlit dashboard application
├── model.py               # Model/prediction-related logic
├── models.py              # Supporting model components
├── ai_agent.py            # AI-assisted retention functionality
├── main.py                # Project entry/support logic
├── customers.csv          # Customer data
├── data_generator/        # Data-generation resources
├── README.md              # Project documentation
└── Harmain_Khanum-Customer_Churn_Prediction_GitHub.zip
```

## 💡 Key Features

| Feature | Description |
|---|---|
| Churn Prediction | Identifies customers with higher churn risk |
| Risk Assessment | Presents a customer risk level and probability |
| Dashboard | Provides business-level retention insights |
| Risk Drivers | Shows factors associated with customer risk |
| Retention Strategy | Suggests an action for high-risk customers |
| AI Email | Creates a draft retention email |
| Batch Scanner | Supports CSV-based customer data review |
| Data Visualization | Uses interactive charts for analysis |

## 🔍 Example Use Case

A company notices that some customers have decreasing usage, several support tickets, and short tenure.

Instead of waiting until those customers leave, the platform can:

1. Analyze their customer information.
2. Identify customers with higher churn risk.
3. Highlight the main risk factors.
4. Recommend a retention action.
5. Generate a personalized retention email draft.

This demonstrates the complete idea of moving from **data → prediction → explanation → business action**.

## 📈 Why This Project Is Useful

Customer churn prediction is useful because businesses can use historical and current customer information to identify potential retention problems early.

The project demonstrates practical skills in:

- Machine learning
- Python programming
- Data analysis
- Data visualization
- Dashboard development
- Business problem solving
- AI-assisted automation

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/harmainkhanum407-art/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment on Windows

```powershell
venv\Scripts\activate
```

### 4. Install the required packages

Install the packages required by the project, for example:

```bash
pip install pandas numpy scikit-learn streamlit plotly requests
```

### 5. Run the dashboard

```bash
streamlit run app.py
```

The Streamlit application will then open in your browser.

## 👩‍💻 Project By

**Harmain Khanum**

BCA Student | Python | Machine Learning | Data Analysis | Software Development

## 🔗 Repository

[View the Customer Churn Prediction project on GitHub](https://github.com/harmainkhanum407-art/Customer_Churn_Prediction)

---

⭐ This project was developed as a practical BCA project to explore how machine learning and AI-assisted automation can be applied to customer retention.
