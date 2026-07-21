import pandas as pd 
df = pd.read_csv("./data.csv")
# print(df.loc[1])
# print(df.iloc[1])
print(df.iloc[1]['Calories'])

import random
import pandas as pd

# 1. Generate the 100-row sample CSV file
cities = [
    'bangalore',
    'mumbai',
    'delhi',
    'chennai',
    'kolkata',
    'hyderabad',
    'pune',
]
data = {
    'id': list(range(1, 101)),
    'city': [random.choice(cities) for _ in range(100)],
    'score': [random.randint(50, 100) for _ in range(100)],
}

df = pd.DataFrame(data)
df.to_csv('/content/sdata.csv', index=False)

# 2. Run your chunking program
chunk = 10
first_chunk = True

for i in pd.read_csv('/content/sdata.csv', chunksize=chunk):
  i['uppercity'] = i['city'].str.upper()
  i.to_csv('/content/newdata.csv', mode='a', index=False, header=first_chunk)
  first_chunk = False

# 3. Verify the output
result_df = pd.read_csv('/content/newdata.csv')
print(f'Total rows in newdata.csv: {len(result_df)}')
result_df.head()