import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv('cleaned_marketing_data.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('marketing', conn, index=False, if_exists='replace')

print("--- Marketing Database Ready ---\n")

# --- QUERY 1: Campaign Acceptance Rate Summary ---
query1 = """
SELECT 
    COUNT(ID) AS total_customers,
    SUM(AcceptedCmp1) AS accepted_cmp1,
    SUM(AcceptedCmp5) AS accepted_cmp5,
    SUM(Response) AS accepted_latest_cmp,
    ROUND(100.0 * SUM(Response) / COUNT(ID), 2) AS latest_campaign_response_pct
FROM marketing;
"""
print("Query 1: Campaign Response Rates")
print(pd.read_sql(query1, conn))
print("\n" + "="*50 + "\n")

# --- QUERY 2: Average Spending by Education Level ---
query2 = """
SELECT 
    Education,
    COUNT(ID) AS customer_count,
    ROUND(AVG(Income), 2) AS avg_income,
    ROUND(AVG(Total_Spent), 2) AS avg_total_spent
FROM marketing
GROUP BY Education
ORDER BY avg_total_spent DESC;
"""
print("Query 2: Spending Habits by Education Level")
print(pd.read_sql(query2, conn))