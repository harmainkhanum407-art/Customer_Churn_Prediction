import os
from dotenv import load_dotenv

load_dotenv()

def generate_retention_campaign(customer_id: str, reasons: list, segment: str) -> str:
    reasons_text = "\n".join([f"- {r}" for r in reasons]) if reasons else "- High risk of churn observed."
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Try OpenAI if valid key exists
    if api_key and api_key.startswith("sk-"):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            prompt = f"Write a personalized customer retention email for {customer_id}.\nRisk level: {segment}.\nIssues:\n{reasons_text}"
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM API Error: {e}")

    # Guarantees a full email template if API key is missing or fails
    return f"""Subject: Urgent: Special Renewal Offer & Support for Account {customer_id}

Dear Valued Customer,

We noticed recent friction regarding your account and want to ensure you are getting full value from our platform.

Based on your account activity, we flagged the following area(s) for immediate support:
{reasons_text}

We have assigned a dedicated Account Manager to your account and applied an exclusive 20% renewal discount on your next billing cycle.

Please reply directly to this email to get your open items resolved right away.

Best regards,  
Customer Retention Team"""