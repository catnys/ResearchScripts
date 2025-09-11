import csv

# Girdi ve çıktı dosya yolları
to_exclude_path = "Abstrackr_formatter/To_Exclude_3cat.csv"
output_path = "Abstrackr_formatter/output_from_exclude.csv"

# Hedef başlıklar (abstrackr formatı)
headers = [
    "pmid",
    "refman",
    "title",
    "abstract",
    "authors",
    "journal",
    "publication_date",
    "keywords"
]

def convert_to_abstrackr_format(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in reader:
            writer.writerow({
                "pmid": "",
                "refman": "",
                "title": row.get("Title", "").strip(),
                "abstract": row.get("Abstract", "").strip(),
                "authors": "",
                "journal": row.get("Taken From", "").strip(),
                "publication_date": row.get("Year", "").strip(),
                "keywords": row.get("Where Published", "").strip()
            })

if __name__ == "__main__":
    convert_to_abstrackr_format(to_exclude_path, output_path)
    print(f"Dönüşüm tamamlandı. Çıktı dosyası: {output_path}")
