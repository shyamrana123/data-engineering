import pandas as pd

# Create a sample sales dataset

sales = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer": ["John", "Sam", "Raj", "Alex", "Sophia"],
    "country": ["Portugal", "Spain", "Nepal", "Portugal", "UK"],
    "amount": [120, 250, 180, 320, 90]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(sales)

print("Original dataset:")
print(df)

#Save as CSV
df.to_csv("sales.csv", index = False)

#Save as JSON
df.to_json("sales.json", orient = "records", indent=4)

#Save as Parquet
df.to_parquet("sales.parquet", index= False)

print("\nFiles created successfully")


#What does this code do?
#- pd.DataFrame(sales) creates a table from our dictionary.
#- to_csv() saves the table as CSV.
#- to_json() saves it as JSON.
#- to_parquet() saves it in Parquet format.