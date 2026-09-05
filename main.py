import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

try:
    from ai_agent import generate_retention_campaign
except ImportError:
    from backend.ai_agent import generate_retention_campaign

app = FastAPI()

class CustomerData(BaseModel):
    tenure_months: int
    monthly_charges: float
    usage_drop_pct: float
    support_tickets: int
    contract_type: str
    payment_method: str

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        prob = 0.65
        risk_level = "High Risk" if prob > 0.5 else "Low Risk"

        campaign_text = generate_retention_campaign(
            customer_id="CUST-10001",
            reasons=["High monthly charges", "Increased support tickets"],
            segment=risk_level
        )

        return {
            "churn_probability": float(prob),
            "risk_level": risk_level,
            "campaign": campaign_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)