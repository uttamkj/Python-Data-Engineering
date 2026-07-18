# Generating 100 sample records for a finance dashboard with random values
# Simulate the imperfect data as you requested
# Create initial finance data with duplicates, null values, and wrong date formats
#kaggle website for sample data


#VVIP info*********************this code is only to prepare sample data so please ignore the code its not part of your syllabus.************************


import pandas as pd
import numpy as np

#ignore the below it is used to create sample data , for you you ll be extractiug data from csv files.

imperfect_data = {
    'Date': pd.date_range('2025-03-07 00:00:00', periods=100, freq='H').append(pd.date_range('2025-03-07 00:00:00', periods=5, freq='H')),
    'Revenue': np.random.randint(1000, 5000, size=105),
    'Expenses': np.random.randint(500, 2000, size=105),
    'COGS': np.random.randint(300, 1500, size=105),
    'Operating_Expenses': np.random.randint(200, 1000, size=105),
    'Depreciation': np.random.randint(50, 200, size=105),
    'Amortization': np.random.randint(50, 200, size=105),
    'Cash_Inflows': np.random.randint(1000, 3000, size=105),
    'Cash_Outflows': np.random.randint(500, 2500, size=105),
    'AR': np.random.randint(100, 1500, size=105),
    'AP': np.random.randint(100, 1500, size=105),
}

#import data from csv
#Assume we are reading data from a path into a df
#df = pd.read_csv('/content/finance.csv')


# Convert to DataFrame
df_imperfect = pd.DataFrame(imperfect_data)

# Add some null values
null_rows = np.random.choice(df_imperfect.index, size=15, replace=False)
df_imperfect.loc[null_rows, 'Revenue'] = np.nan
df_imperfect.loc[null_rows, 'Expenses'] = np.nan
df_imperfect.loc[null_rows, 'Operating_Expenses'] = np.nan
df_imperfect.loc[null_rows, 'COGS'] = np.nan

# Add some string column and introduce "unknown" value
df_imperfect['Department'] = ['Sales', 'Marketing', 'Finance', 'HR', 'Legal'] * 21
df_imperfect.loc[10:20, 'Department'] = np.nan  # Some nulls for Department

# Introduce wrong date formats by manually changing some Date values
wrong_dates = df_imperfect.loc[20:30, 'Date']
wrong_dates = wrong_dates.apply(lambda x: x.replace(hour=15) if x.hour == 0 else x)  # Change some hours
df_imperfect.loc[20:30, 'Date'] = wrong_dates

df_imperfect.to_csv('/content/data.csv')


#print(df_imperfect.to_csv())



#layers: Bronze (raw data) :   Medallion architecture
data = pd.read_csv('/content/data.csv')
data.info()



#  Silver (cleaned and standardized data)
data['Revenue'] = data['Revenue'].fillna(data['Revenue'].mean())
data['Expenses'] = data['Expenses'].fillna(data['Expenses'].mean())
data['COGS'] = data['COGS'].fillna(data['COGS'].mean())
data['Operating_Expenses'] = data['Operating_Expenses'].fillna(data['Operating_Expenses'].mean())
data['Department'] = data['Department'].fillna('unknown')
data.info()


# Gold (aggregated data ready for business analytics)
data['total_revenue'] = data['Revenue']
data['total_expense'] = data['Expenses']
data['profit'] = data['Revenue'] - data['Expenses']
data['gross_margin'] = (data['Revenue'] - data['COGS'])/data['Revenue']
data['operating_income'] = data['Revenue'] - data['Operating_Expenses']
data['EBITDA'] = data['operating_income'] + data['Depreciation'] + data['Amortization']
data['accounts_receivables'] = data['AR']
data['accounts_payables'] = data['AP']
data['year_over_year_growth'] = data['Revenue'] * 0.05

data.info()


data.to_parquet('/content/finance_data.parquet')
data.to_csv('/content/finance_data.csv')
