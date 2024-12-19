import functions
import pandas as pd
from datetime import datetime

def main():
    print("Welcome to the Stock Selection Tool!")

    # Define file names
    users_file = "users.csv"
    interactions_file = "interactions.csv"

    # User Registration or Login
    while True:
        choice = input("Do you want to [R]egister or [L]ogin? ").lower()
        if choice == 'r':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if functions.register_user(email, password, users_file):
                print("Registration successful!")
                break
            else:
                print("Registration failed. Email already exists.")
        elif choice == 'l':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if functions.authenticate_user(email, password, users_file):
                print("Login successful!")
                break
            else:
                print("Invalid credentials. Try again.")

    # Stock Data Retrieval and Analysis
    while True:
        ticker = input("Enter the stock ticker (e.g., 1155.KL): ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            # Retrieve closing prices for the given ticker and period
            data = functions.get_closing_prices(ticker, start_date, end_date)
            print("\nClosing Prices:\n", data)

            # Analyze Closing Prices
            analysis_results = functions.analyze_closing_prices(data)
            print("\nAnalysis Results:\n", analysis_results)

            # Convert analysis results to a dictionary and save
            interaction = {
                "email": email,
                "ticker": ticker,
                "start_date": start_date,
                "end_date": end_date,
                **analysis_results.to_dict()  # Convert the Series to a dictionary
            }
            functions.save_to_csv(interaction, interactions_file)
        except Exception as e:
            print(f"Error: {e}")

        # Continue or Exit
        cont = input("Do you want to analyze another stock? (yes/no): ").lower()
        if cont != 'yes':
            break

    # Display Stored Data
    show_data = input("Do you want to view stored data? (yes/no): ").lower()
    if show_data == 'yes':
        stored_data = functions.read_from_csv(interactions_file)
        print("\nStored Data:\n", stored_data)

if __name__ == "__main__":
    main()
