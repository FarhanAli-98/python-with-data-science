import pandas as pd


print("-------------------------------------------")
print("----------Reading a CSV file---------------")
print("-------------------------------------------")


# Reading a CSV file
df = pd.read_csv('/Users/nomixe/Documents/python/panda/csv/data.csv')
print("\\nRead CSV:")
print(df.head())

# Writing to a CSV file
df.to_csv('/Users/nomixe/Documents/python/panda/csv/output.csv', index=False)

print("-------------------------------------------")
print("----------Creating a DataFrame-------------")
print("-------------------------------------------")


