import pandas as pd
# Reading an Excel file
df = pd.read_excel('/Users/tanbits/Documents/GitHub/python-with-data-science/panda/excel/data.xlsx')
print("\\nRead Excel:")
print(df.head())

# Writing to an Excel file
df.to_excel('/Users/tanbits/Documents/GitHub/python-with-data-science/panda/excel/output.xlsx', index=False)
