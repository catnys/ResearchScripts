import bibtexparser
import csv

def parse_bibtex(bibtex_file, output_csv):
    with open(bibtex_file, 'r', encoding='utf-8') as f:
        bib_database = bibtexparser.load(f)
    
    extracted_data = []
    for entry in bib_database.entries:
        title = entry.get('title', '').strip()
        year = entry.get('year', '').strip()
        abstract = entry.get('abstract', '').strip()
        taken_from = "ScienceDirect"
        where_published = entry.get('publisher', entry.get('journal', '')).strip()
        
        extracted_data.append([title, year, abstract, taken_from, where_published])
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Title", "Year", "Abstract", "Taken From", "Where Published"])
        writer.writerows(extracted_data)
    
    print(f"Data successfully written to {output_csv}")


parse_bibtex("sciencedirect.bib", "output.csv")
