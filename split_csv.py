import pandas as pd

def split_csv_by_country(input_file):
    try:
        # Try reading the CSV with ISO-8859-1 encoding
        df = pd.read_csv(input_file, encoding='ISO-8859-1')

        # Check if the 'Country' column exists
        if 'Country' not in df.columns:
            print("Error: 'Country' column not found in the CSV file.")
            return

        # Group by 'Country' column and save each group as a separate CSV file
        for country, group in df.groupby('Country'):
            filename = f"CSV/{country}.csv"
            group.to_csv(filename, index=False, encoding='utf-8')  # Save files in UTF-8
            print(f"File saved: {filename}")

    except UnicodeDecodeError:
        print("Error: Unable to read the file due to encoding issues. Try using a different encoding.")

# Example usage
input_csv = "data.csv"  # Replace with your actual CSV file
split_csv_by_country(input_csv)
