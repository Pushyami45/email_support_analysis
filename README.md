# email_support_analysis
# 📧 Email Support Analysis

This project analyzes support emails and classifies them into categories such as **Billing Issue, Login/Access Issue, API/Integration Query, Urgent Support, Subscription Query, and General Query**.  
It also provides simple analytics like the number of emails per category and the number of emails per sender.


## 📂 Dataset
- File: `dataset.csv`
- Columns:
  - **sender** → Email address of the sender  
  - **subject** → Subject line of the email  
  - **body** → Full email text  
  - **sent_date** → Timestamp of the email  


## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/email-support-analysis.git
   cd email-support-analysis
2. Install dependencies:
   pip install -r requirements.txt
3. Run the script:
   python main.py
📊 Output
  A new file categorized_emails.csv will be generated with an additional column category.
   Console output will display:
    📌 Number of emails per category
    📌 Number of emails per sender

🛠 Categories
  The emails are classified into the following categories:
   ->Billing Issue
   ->Login/Access Issue
   ->Integration Query
   ->Urgent Support
   ->Subscription Query  
   ->General Query

✅ Example Output

     Email Category      Counts
    Billing Issue            5
    Login/Access Issue       4
    API/Integration Query    3
    Urgent Support           3
    Subscription Query       2
    General Query            3

**Emails per Sender**

  eve@startup.io       7
  alice@example.com    5
  diana@client.co      4
