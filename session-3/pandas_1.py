import pandas as pd

df = pd.read_excel("sample_excel_1.xlsx")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()
print(df)

# Find the mean of the 'weight' column
mean_weight = df['Weight'].mean()
df['Weight_diff'] = df['Weight'] - mean_weight
print(df)

# Mapping dictionary
fruit_map = {
    'Apple': 0,
    'Banana': 1,
    'Orange': 2
}
df['Fruit_mapped'] = df['Fruit'].map(fruit_map)
print(df)

# Write the DataFrame to an Excel file
df.to_excel("new_fruit_data.xlsx", index=False)