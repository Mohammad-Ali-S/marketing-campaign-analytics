import pandas as pd
import numpy as np

# 1. Load dataset (note: Kaggle's marketing dataset is tab-separated)
df = pd.read_csv('marketing_campaign.csv', sep='\t')

print("Initial Shape:", df.shape)

# 2. Clean missing values in 'Income'
# Some rows have missing income values; we'll fill them with the median income
df['Income'] = df['Income'].fillna(df['Income'].median())

# 3. Feature Engineering: Total Spending & Total Children
df['Total_Spent'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
df['Total_Children'] = df['Kidhome'] + df['Teenhome']

# 4. Save cleaned dataset
df.to_csv('cleaned_marketing_data.csv', index=False)
print("Marketing data cleaned and saved successfully as 'cleaned_marketing_data.csv'!")