import pandas as pd

data = {
    'A': [1,2,2,3,3,4],
    'B': [5,6,6,7,8,8]
}

df = pd.DataFrame(data)
print("Original Data:\n",df.to_string(index=False))

print("\nDublicate Rows:\n",df[df.duplicated()].to_string(index=False))

df.drop_duplicates(subset=['A'], keep='first', inplace=True)
print("\nDataFrame after removing dublicates based on column:\n",df.to_string(index=False))