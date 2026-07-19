"""
================================================================================
PANDAS COMPLETE REFERENCE — INTERVIEW QUICK-REVISION SCRIPT
================================================================================
Every function used across the 7-day plan, in one runnable file.
Organized by day/topic. Read top to bottom, or Ctrl+F a function name.
Run it directly: python3 pandas_cheatsheet.py
================================================================================
"""

import pandas as pd
import numpy as np
import time
from functools import reduce

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# ==============================================================================
# DAY 1 — SERIES, DATAFRAMES, READING, EXPLORING, SELECTING
# ==============================================================================
section("DAY 1: Series & DataFrame basics")

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])   # 1D labeled array
print(s)
print(s['b'])                 # label access
print(s.values)               # underlying numpy array
print(s.index)                # index labels

df = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank'],
    'age': [25, 30, 35, 40, 28, 33],
    'salary': [50000, 60000, 55000, 65000, 52000, 61000],
    'department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'Sales'],
    'city': ['Bengaluru', 'Delhi', 'Mumbai', 'Delhi', 'Bengaluru', 'Mumbai'],
    'join_date': pd.to_datetime(
        ['2021-01-15', '2020-06-23', '2019-11-01', '2022-03-10', '2021-07-19', '2020-01-05']
    ),
})

# Reading (shown as comments — no real files here):
# df = pd.read_csv('file.csv', sep=',', header=0, dtype={'age': int}, na_values=['NA'])
# df = pd.read_json('file.json')
# df = pd.read_excel('file.xlsx')
# df = pd.read_sql('SELECT * FROM table', con=engine)

section("Exploring")
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(df.dtypes)
df.info()
print(df.describe())
print(df.columns.tolist())
print(df['department'].unique())
print(df['department'].nunique())

section("Selecting: loc / iloc / at / iat")
print(df.loc[0])                       # row by label
print(df.loc[0, 'name'])               # single value by label
print(df.loc[:, 'name'])               # entire column
print(df.iloc[0])                      # row by position
print(df.iloc[0:2, 1:3])               # slice by position
print(df.at[0, 'name'])                # fast single value, label-based
print(df.iat[0, 1])                    # fast single value, position-based
print(df[df['age'] > 30])              # boolean filter
print(df[(df['age'] > 25) & (df['department'] == 'Sales')])  # multi-condition


# ==============================================================================
# DAY 2 — CLEANING
# ==============================================================================
section("DAY 2: Cleaning")

messy = pd.DataFrame({
    'name': ['  Alice ', 'BOB', 'charlie', 'Dave', 'Dave'],   # dupe row included
    'age': ['25', '30yrs', None, ' 40', '40'],
    'salary': [50000, 'N/A', 55000, 65000, 65000],
    'department': ['sales', 'SALES', 'Engineering', None, None],
})
messy = pd.concat([messy, messy.iloc[[4]]], ignore_index=True)  # extra dupe

print(messy.isna())
print(messy.isna().sum())
print(messy.notna())

# dropna variants
print(messy.dropna())
print(messy.dropna(subset=['department']))
print(messy.dropna(how='all'))
print(messy.dropna(thresh=3))

# fillna variants
print(messy['department'].fillna('Unknown'))
print(messy.ffill())
print(messy.bfill())

# duplicates
print(messy.duplicated())
print(messy.duplicated().sum())
messy_clean = messy.drop_duplicates()
print(messy_clean)
print(messy.drop_duplicates(subset=['name'], keep='first'))

# type fixing
messy_clean['age'] = messy_clean['age'].astype(str).str.extract(r'(\d+)')
messy_clean['age'] = pd.to_numeric(messy_clean['age'], errors='coerce')
messy_clean['salary'] = pd.to_numeric(messy_clean['salary'], errors='coerce')
print(messy_clean.dtypes)

# string cleaning
messy_clean['name'] = messy_clean['name'].str.strip().str.title()
messy_clean['department'] = messy_clean['department'].str.strip().str.title()
print(messy_clean['name'].str.upper())
print(messy_clean['name'].str.lower())
print(messy_clean['name'].str.contains('a', case=False))
print(messy_clean['name'].str.replace('a', '@', case=False))
print(messy_clean['name'].str.split(' '))

# renaming
messy_clean = messy_clean.rename(columns={'name': 'employee_name'})
print(messy_clean.columns.tolist())


# ==============================================================================
# DAY 3 — TRANSFORMATION
# ==============================================================================
section("DAY 3: Transformation")

print(df[df['city'].isin(['Delhi', 'Mumbai'])])
print(df[df['age'].between(25, 35)])
print(df[~(df['department'] == 'HR')])

print(df.sort_values('salary', ascending=False))
print(df.sort_values(['department', 'salary'], ascending=[True, False]))
print(df.sort_index())

# vectorized ops (preferred — fast)
df['bonus'] = df['salary'] * 0.10
df['salary_in_k'] = df['salary'] / 1000

# apply / map (use only when vectorized isn't possible)
df['age_group'] = df['age'].apply(lambda x: 'Senior' if x >= 35 else 'Junior')
df['dept_code'] = df['department'].map({'Sales': 'S', 'Engineering': 'E', 'HR': 'H'})
df['category'] = df.apply(
    lambda row: 'Top' if row['salary'] > 60000 and row['age'] > 30 else 'Other', axis=1
)

# vectorized vs apply speed check
start = time.time()
_ = df['salary'] * 2
t_vec = time.time() - start
start = time.time()
_ = df['salary'].apply(lambda x: x * 2)
t_apply = time.time() - start
print(f"Vectorized: {t_vec:.6f}s | Apply: {t_apply:.6f}s")

df = df.drop(columns=['bonus'])                 # drop a column
df = df.assign(tax=lambda d: d['salary'] * 0.2)  # chainable column add

df['age_bucket'] = pd.cut(df['age'], bins=[0, 28, 35, 100], labels=['Young', 'Mid', 'Senior'])
df['salary_quartile'] = pd.qcut(df['salary'], q=2, labels=['Low', 'High'])
print(df[['name', 'age', 'age_bucket', 'salary', 'salary_quartile']])


# ==============================================================================
# DAY 4 — AGGREGATION
# ==============================================================================
section("DAY 4: Aggregation")

print(df.groupby('department')['salary'].mean())
print(df.groupby('department')['salary'].sum())
print(df.groupby('department').size())
print(df.groupby('department')['salary'].count())
print(df.groupby(['department', 'city'])['salary'].mean())

print(df.groupby('department')['salary'].agg(['mean', 'sum', 'count', 'min', 'max']))
print(df.groupby('department').agg({'salary': ['mean', 'sum'], 'age': ['mean', 'max']}))
print(df.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    headcount=('name', 'count')
))

df['dept_avg_salary'] = df.groupby('department')['salary'].transform('mean')
df['salary_vs_dept_avg'] = df['salary'] - df['dept_avg_salary']
print(df[['name', 'department', 'salary', 'dept_avg_salary', 'salary_vs_dept_avg']])

print(df.groupby('department').filter(lambda x: len(x) >= 2))

print(pd.pivot_table(df, values='salary', index='department', columns='city', aggfunc='mean'))
print(pd.pivot_table(df, values='salary', index='department', aggfunc=['mean', 'count']))

print(pd.crosstab(df['department'], df['city']))
print(pd.crosstab(df['department'], df['city'], normalize=True))

print(df['department'].value_counts())
print(df['department'].value_counts(normalize=True))

print(df[['age', 'salary']].corr())
print(df['age'].corr(df['salary']))


# ==============================================================================
# DAY 5 — COMBINING DATA
# ==============================================================================
section("DAY 5: Combining data")

df1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'salary': [50000, 60000]})
df2 = pd.DataFrame({'name': ['Charlie', 'Dave'], 'salary': [70000, 80000]})
print(pd.concat([df1, df2], axis=0, ignore_index=True))     # stack rows
print(pd.concat([df1, df2], axis=1))                         # stack columns

employees = pd.DataFrame({'emp_id': [1, 2, 3, 4], 'name': ['Alice', 'Bob', 'Charlie', 'Dave'],
                           'dept_id': [10, 20, 10, 30]})
departments = pd.DataFrame({'dept_id': [10, 20, 40], 'dept_name': ['Sales', 'Engineering', 'Marketing']})
salaries = pd.DataFrame({'emp_id': [1, 2, 3, 4], 'salary': [50000, 60000, 55000, 65000]})

print(pd.merge(employees, departments, on='dept_id', how='inner'))
print(pd.merge(employees, departments, on='dept_id', how='left'))
print(pd.merge(employees, departments, on='dept_id', how='right'))
print(pd.merge(employees, departments, on='dept_id', how='outer'))

# 3-table chained merge
result = (
    employees
    .merge(departments, on='dept_id', how='left')
    .merge(salaries, on='emp_id', how='left')
)
print(result)

# merging many tables with reduce
tables = [employees, departments, salaries]
result2 = reduce(lambda left, right: pd.merge(left, right, how='left'), tables)
print(result2)

# reshaping
wide = pd.DataFrame({'name': ['Alice', 'Bob'], 'jan_sales': [100, 150], 'feb_sales': [120, 130]})
long = pd.melt(wide, id_vars='name', value_vars=['jan_sales', 'feb_sales'],
               var_name='month', value_name='sales')
print(long)
print(long.pivot(index='name', columns='month', values='sales'))

# MultiIndex
df_multi = df.set_index(['department', 'name'])
print(df_multi.loc['Sales'])
print(df_multi.xs('Sales', level='department'))


# ==============================================================================
# DAY 6 — I/O, PERFORMANCE, JSON, DATETIME
# ==============================================================================
section("DAY 6: I/O, performance, JSON, datetime")

# writing out (paths shown, safe to run)
df.to_csv('./out.csv', index=False)
df.to_parquet('./out.parquet', index=False)     # needs pyarrow
# df.to_sql('table', con=engine, if_exists='replace', index=False)

df_from_parquet = pd.read_parquet('/tmp/out.parquet')
print(df_from_parquet.dtypes)
df_from_parquet_cols = pd.read_parquet('/tmp/out.parquet', columns=['name', 'salary'])
print(df_from_parquet_cols.head())

# chunked reading pattern (shown, not run — no huge file here)
# for chunk in pd.read_csv('huge.csv', chunksize=100_000):
#     process(chunk)

print(df.memory_usage(deep=True))
before = df.memory_usage(deep=True).sum()
df['department'] = df['department'].astype('category')
after = df.memory_usage(deep=True).sum()
print(f"Memory before: {before}, after category conversion: {after}")

df['age'] = pd.to_numeric(df['age'], downcast='integer')

# nested JSON flattening
nested = [
    {'id': 1, 'name': 'Alice', 'address': {'city': 'Bengaluru', 'zip': '560001'}},
    {'id': 2, 'name': 'Bob', 'address': {'city': 'Delhi', 'zip': '110001'}},
]
flat = pd.json_normalize(nested)
print(flat)

# datetime
df['year'] = df['join_date'].dt.year
df['month'] = df['join_date'].dt.month
df['day_of_week'] = df['join_date'].dt.day_name()
df['days_since_join'] = (pd.Timestamp.today() - df['join_date']).dt.days
print(df[['name', 'join_date', 'year', 'month', 'day_of_week', 'days_since_join']])

ts = df.set_index('join_date').sort_index()
print(ts.resample('YE')['salary'].mean())     # yearly average ('YE' = year end)
df_sorted = df.sort_values('join_date')
df_sorted['rolling_avg_salary'] = df_sorted['salary'].rolling(window=2).mean()
print(df_sorted[['join_date', 'salary', 'rolling_avg_salary']])


# ==============================================================================
# DAY 7 — PLOTTING (matplotlib backend via pandas .plot())
# ==============================================================================
section("DAY 7: Plotting (calls shown — uncomment to actually render)")

# df['salary'].plot(kind='line')
# df['department'].value_counts().plot(kind='bar')
# df['age'].plot(kind='hist')
# df.plot(kind='scatter', x='age', y='salary')
# import matplotlib.pyplot as plt; plt.show()
print("Plotting calls: .plot(kind='line'/'bar'/'hist'/'scatter') — see comments above")

print("\nDONE — full reference executed without errors.")



import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [32, 75, 34, 77],
    'Humidity': [80, 60, 70, 65],
    'Wind Speed': [10, 15, 12, 14]
}

df = pd.DataFrame(data)
print(df)

newdf = df.pivot(index = 'Date', columns = 'City', values = ['Temperature','Humidity','Wind Speed'])
print(newdf)

#normalize

import pandas as pd


data1 = {
    'id':123,
    'name':'krish',
    'address':{
        'street':'123 main st',
        'city':'bangalore',
        'state':'karnataka'
    }
}

df = pd.json_normalize(data1)
print(df)
