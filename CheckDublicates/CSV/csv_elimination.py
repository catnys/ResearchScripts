import pandas as pd
import re

def normalize_title(title):
    if pd.isna(title):
        return ""
    title = title.strip().lower()  # Convert to lowercase and strip spaces
    title = re.sub(r'[^\w\s]', '', title)  # Remove punctuation
    title = re.sub(r'\s+', ' ', title)  # Normalize whitespace
    return title

def check_duplicates(csv_file, output_duplicates, output_cleaned):
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
        duplicates[['Title', 'Year', 'Taken From']].to_csv(output_duplicates, sep=';', index=False)
        print(f"Duplicates saved to {output_duplicates}")
    else:
        print("No duplicate titles found.")
    
    # Remove duplicates and save cleaned file
    cleaned_df = df.drop_duplicates(subset=['Normalized Title'], keep='first').drop(columns=['Normalized Title'])
    cleaned_df.to_csv(output_cleaned, sep=';', index=False)
    print(f"Cleaned dataset without duplicates saved to {output_cleaned}")

# Example usage
csv_file = "my_excel.csv"  # Replace with your actual file path
output_duplicates = "arxiv_duplicates.txt"  # File to save duplicate papers
output_cleaned = "arxiv_cleaned_papers.csv"  # File to save papers without duplicates

check_duplicates(csv_file, output_duplicates, output_cleaned)
