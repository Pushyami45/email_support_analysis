import pandas as pd
import re

# Load dataset
df = pd.read_csv("dataset.csv")

# Simple text-based categorization
def categorize_email(subject, body):
    text = (subject + " " + body).lower()

    if any(word in text for word in ["bill", "payment", "invoice", "pricing"]):
        return "Billing Issue"
    elif any(word in text for word in ["login", "password", "access", "reset"]):
        return "Login/Access Issue"
    elif any(word in text for word in ["api", "integration", "developer"]):
        return "API/Integration Query"
    elif any(word in text for word in ["urgent", "immediate", "asap", "critical"]):
        return "Urgent Support"
    elif any(word in text for word in ["subscription", "plan", "renewal"]):
        return "Subscription Query"
    else:
        return "General Query"

# Apply categorization
df["category"] = df.apply(lambda row: categorize_email(row["subject"], row["body"]), axis=1)

# Analytics
print("\n📊 Email Category Counts:")
print(df["category"].value_counts())

print("\n📊 Emails per Sender:")
print(df["sender"].value_counts())

# Save results
df.to_csv("categorized_emails.csv", index=False)
print("\n✅ Categorized emails saved to categorized_emails.csv")
