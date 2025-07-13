import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(file_path):
    """
    Load a dataset from a CSV file and return it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


df = load_dataset(r"E:\GitHub\nintedo_sales_project\data\raw\vgsales.csv")

df.info()

# Check for missing values
missing_values = df.isnull().sum()
print(
    "Missing values number:\n",
    missing_values.sort_values(ascending=False)
    if not missing_values.empty
    else "No missing values found.",
)

# Fill missing values
df["Publisher"] = df["Publisher"].fillna("Unknown")

# Convert "Year" to integer
df.dropna(subset=["Year"], inplace=True)
df["Year"] = df["Year"].astype(str)

df.describe()

# Check for outliers in sales columns
sales_columns = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
for i, column in enumerate(sales_columns):
    ax[i // 2, i % 2].hist(df[column], bins="auto")
    ax[i // 2, i % 2].set_title(column)
fig.tight_layout()
plt.show()


# Check data cons
# Does Global_Sales always equal the sum of regional sales?
df["Global_Sales_Calculated"] = df[sales_columns].sum(axis=1).round(2)
discrepancies = df[df["Global_Sales"] != df["Global_Sales_Calculated"]]
if not discrepancies.empty:
    print("Global_Sales discrepancies:")
    print(discrepancies)
else:
    print("No discrepancies found in Global_Sales calculation.")
