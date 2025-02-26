import pandas as pd

def get_rates_from_excel(file_path: str) -> pd.DataFrame:
    """
    Reads rates from an Excel file and returns a DataFrame.
    """
    return pd.read_excel(file_path)

def generate_quote(rates_df: pd.DataFrame, customer_info: dict) -> dict:
    """
    Generates a quote for a customer based on the rates DataFrame and customer info.
    """
    # Example logic to generate a quote
    quote = {"customer": customer_info, "quote_items": []}
    for index, row in rates_df.iterrows():
        quote["quote_items"].append({
            "description": row["Description"],
            "rate": row["Rate"],
            "quantity": row["Quantity"],
            "total": row["Rate"] * row["Quantity"]
        })
    return quote