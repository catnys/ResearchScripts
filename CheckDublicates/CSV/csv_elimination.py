import pandas as pd
import re

def normalize_title(title):
    if pd.isna(title):
        return ""
    title = title.strip().lower()  # Convert to lowercase and strip spaces
    title = re.sub(r'[^\w\s]', '', title)  # Remove punctuation
    title = re.sub(r'\s+', ' ', title)  # Normalize whitespace
    return title

def check_duplicates(csv_file, output_file):
    # Load the CSV file
    df = pd.read_csv(csv_file, delimiter=';')
    
    # Normalize titles
    df['Normalized Title'] = df['Title'].apply(normalize_title)
    
    # Find duplicate titles
    duplicates = df[df.duplicated(subset=['Normalized Title'], keep=False)]
    
    num_duplicates = len(duplicates)  # Count duplicate entries
    print(f"Total duplicate titles found: {num_duplicates}")
    
    if not duplicates.empty:
        print("Duplicate titles found. Saving to output file...")
        duplicates[['Title', 'Year', 'Taken From']].to_csv(output_file, sep=';', index=False)
        print(f"Duplicates saved to {output_file}")
    else:
        print("No duplicate titles found.")

# Example usage
csv_file = "your_file.csv"  # Replace with your actual file path
output_file = "duplicates.txt"  # Replace with desired output file name
check_duplicates(csv_file, output_file)
