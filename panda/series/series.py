import pandas as pd
print("-------------------------------------------")
print("----------Creating a Series-------------")

print("-------------------------------------------")
# Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])
print("Series:")
print(series)

print("-------------------------------------------")
print("----------Creating a DataFrame-------------")
# Creating a DataFrame
print("-------------------------------------------")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\\nDataFrame:")
print(df)


print("-------------------------------------------")
print("----------Viewing Data:--------------------")
print("-------------------------------------------")


print("\\nFirst few rows:")
print(df.head())

print("\\nLast few rows:")
print(df.tail())

print("\\nDataFrame shape:")
print(df.shape)

print("-------------------------------------------")
print("-------Data Types and Conversion:----------")
print("-------------------------------------------")

print("\\nData types:")
print(df.dtypes)

# Converting data types
df['Age'] = df['Age'].astype(float)
print("\\nConverted data types:")
print(df.dtypes)


print("-------------------------------------------")
print("-----------5. Data Cleaning----------------")
print("-------------------------------------------")

# Handling missing data
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 'b', 'c', 'd']
})

print("\\nOriginal DataFrame with missing values:")
print(df)

# Fill missing values
df_filled = df.fillna({'A': 0, 'B': 'unknown'})
print("\\nDataFrame after filling missing values:")
print(df_filled)

# Drop missing values
df_dropped = df.dropna()
print("\\nDataFrame after dropping missing values:")
print(df_dropped)


print("-------------------------------------------")
print("-----------Data Transformation:------------")
print("-------------------------------------------")

# Applying transformations
df['A_squared'] = df['A'] ** 2
print("\\nDataFrame with transformed column:")
print(df)
