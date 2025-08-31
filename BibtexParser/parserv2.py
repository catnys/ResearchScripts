import re
import pandas as pd

def parse_bibtex(bibtex_text):
    """Extracts relevant fields from BibTeX entries."""
    patterns = {
        "title": r"title\s*=\s*\{(.+?)\}",
        "year": r"year\s*=\s*\{(.+?)\}",
        "abstract": r"abstract\s*=\s*\{(.+?)\}"
    }
    
    entries = []
    for entry in bibtex_text.split("\n\n@"):  # Split individual entries
        data = {
            "title": "", 
            "year": "", 
            "abstract": "", 
            "taken_from": "ACM/Scopus/Elsevier/IEEE..",  # Indicates the platform, so fill out on the data based on you
            "where_published": ""  # Empty field
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, entry, re.DOTALL)
            if match:
                extracted_text = match.group(1).replace("\n", " ")
                data[key] = extracted_text
        
        entries.append(data)
    
    return entries

def convert_bibtex_to_csv(input_file, output_file):
    """Reads a BibTeX file, extracts relevant data, and saves it as a CSV file."""
    with open(input_file, "r", encoding="utf-8") as file:
        bibtex_text = file.read()
    
    parsed_entries = parse_bibtex(bibtex_text)
    df = pd.DataFrame(parsed_entries)
    
    df.to_csv(output_file, sep=";", index=False)
    print(f"CSV file saved as {output_file}")

# Example usage
input_bibtex_file = "all_merged_acm.bib"  # Change this to your actual BibTeX file name
output_csv_file = "output-abstract.csv"
convert_bibtex_to_csv(input_bibtex_file, output_csv_file)
