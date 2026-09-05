import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import joblib
import os

def train_and_save_pipeline(data_path="data/customers.csv", model_dir="models"):
    os.makedirs(model_dir, exist_ok=True)
    df = pd.read_csv(data_path)
    
    # Feature Selection & Encoding
    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]
    
    X = pd.get_dummies(X, columns=["contract_type", "payment_method"], drop_first=True)
    
    # Model Training
    model = xgb.XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42)
    model.fit(X, y)
    
    # Save Trained Model & Feature List
    joblib.dump(model, os.path.join(model_dir, "churn_model.pkl"))
    joblib.dump(list(X.columns), os.path.join(model_dir, "model_features.pkl"))
    print("Model and features saved successfully in 'models/' directory.")

def analyze_customer(customer_data: dict, model_dir="models"):
    model = joblib.load(os.path.join(model_dir, "churn_model.pkl"))
    features = joblib.load(os.path.join(model_dir, "model_features.pkl"))
    
    df_raw = pd.DataFrame([customer_data])
    df_encoded = pd.get_dummies(df_raw, columns=["contract_type", "payment_method"])
    
    for col in features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[features]
    
    prob = float(model.predict_proba(df_encoded)[0][1])
    prob_pct = round(prob * 100, 2)
    
    # SHAP Explainer
    explainer = shap.TreeExplainer(model)
    shap_vals = explainer.shap_values(df_encoded)[0]
    
    top_reasons = []
    feature_impacts = dict(zip(features, shap_vals))
    sorted_impacts = sorted(feature_impacts.items(), key=lambda x: x[1], reverse=True)
    
    for feat, impact in sorted_impacts[:3]:
        if impact > 0:
            val = customer_data.get(feat, df_encoded[feat].values[0])
            top_reasons.append(f"{feat.replace('_', ' ').title()} ({val}) increased churn risk")
            
    # Risk Segmentation & Prescriptive Actions
    if prob >= 0.70:
        segment = "High Risk"
        action = "Dispatch Account Manager immediately; offer 20% renewal discount and priority support resolution."
    elif prob >= 0.35:
        segment = "Medium Risk"
        action = "Trigger automated re-engagement email series and provide product walkthrough invitation."
    else:
        segment = "Low Risk"
        action = "Standard retention path; enroll in upsell/loyalty program."
        
    return {
        "churn_probability": prob_pct,
        "segment": segment,
        "reasons": top_reasons if top_reasons else ["Balanced account metrics"],
        "recommended_action": action
    }

if __name__ == "__main__":
    train_and_save_pipeline()