import pandas as pd
data={
    "name": ["Alice", "BOb", "Carol"],
    "age": [25, 30, 35]
}
df=pd.DataFrame(data)
print(df)
print(df['age'].mean())