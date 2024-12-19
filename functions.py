import pandas as pd
import os
import yfinance as yf

# Helper function to create a file with headers if it doesn't exist or is empty
def create_file_with_headers(filename, columns):
    if not os.path.exists(filename):
        print(f"{filename} does not exist. Creating it with headers...")
        df = pd.DataFrame(columns=columns)
        df.to_csv(filename, index=False)
    else:
        try:
            df = pd.read_csv(filename)
            if df.empty or not all(col in df.columns for col in columns):
                print(f"{filename} is empty or has incorrect columns. Recreating with headers...")
                df = pd.DataFrame(columns=columns)
                df.to_csv(filename, index=False)
        except pd.errors.EmptyDataError:
            print(f"{filename} is empty. Creating it with headers...")
            df = pd.DataFrame(columns=columns)
            df.to_csv(filename, index=False)

# Register User Function
def register_user(email, password, filename):
    create_file_with_headers(filename, ["email", "password"])  # Ensure file has required headers
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading file: {e}")
        return False

    if email in df["email"].values:
        return False  # Email already exists
    else:
        new_user = pd.DataFrame({"email": [email], "password": [password]})
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(filename, index=False)
        return True

# Authenticate User Function
def authenticate_user(email, password, filename):
    create_file_with_headers(filename, ["email", "password"])  # Ensure file has required headers
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading file: {e}")
        return False

    user = df[(df["email"] == email) & (df["password"] == password)]
    return not user.empty

# Get Closing Prices for Stock
def get_closing_prices(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    if "Close" not in data.columns:
        raise ValueError("No closing prices found for the given ticker.")
    return data["Close"]

# Analyze Closing Prices
def analyze_closing_prices(data):
    # Calculate analysis results
    average_price = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest_price = data.max()
    lowest_price = data.min()

    # Return as a pandas Series for easier formatting
    return pd.Series({
        "average_price": average_price,
        "percentage_change": percentage_change,
        "highest_price": highest_price,
        "lowest_price": lowest_price
    })

# Save User Interactions to CSV (with headers)
def save_to_csv(data, filename):
    create_file_with_headers(filename, ["email", "ticker", "start_date", "end_date", "average_price", "percentage_change", "highest_price", "lowest_price"])  # Ensure file has required headers
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Convert the interaction data to a DataFrame and append to the CSV
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(filename, index=False)

# Read and Display Interactions from CSV
def read_from_csv(filename):
    create_file_with_headers(filename, ["email", "ticker", "start_date", "end_date", "average_price", "percentage_change", "highest_price", "lowest_price"])  # Ensure file has required headers
    try:
        df = pd.read_csv(filename)
        if df.empty:
            return "No data found."
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return "No data found."
