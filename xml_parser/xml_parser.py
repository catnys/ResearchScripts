import xml.etree.ElementTree as ET
import csv
import os

# File paths (assumes script and XML file are in the same directory)
input_xml_file = "Ti-new-2411-arxiv.xml"
output_csv_file = "TI_all_merged_abstract_arxiv.csv"

def parse_arxiv_xml(input_file, output_file):
    file_exists = os.path.isfile(output_file)

    # Open CSV file for writing/appending
    with open(output_file, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")

        # Write header only if the file is new
        if not file_exists:
            writer.writerow(["Title", "Year", "Taken From", "Where Published", "Abstract"])

        # Define the namespace for proper XML parsing
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        # Use iterparse for large XML files (efficient memory usage)
        context = ET.iterparse(input_file, events=("start", "end"))
        _, root = next(context)  # Get root element

        for event, elem in context:
            if event == "end" and elem.tag.endswith("entry"):
                # Extract required fields safely
                title_elem = elem.find("atom:title", ns)
                published_elem = elem.find("atom:published", ns)
                abstract_elem = elem.find("atom:summary", ns)

                # Extract and clean text, handling missing elements
                title = title_elem.text.strip() if title_elem is not None else "N/A"
                published = published_elem.text.strip() if published_elem is not None else "N/A"
                abstract = abstract_elem.text.strip() if abstract_elem is not None else "N/A"

                # Extract year from published date (format: YYYY-MM-DD)
                year = published.split("-")[0] if published and published != "N/A" else "N/A"

                # Write to CSV file
                writer.writerow([title, year, "arXiv", "", abstract])

                # Free up memory by clearing processed elements
                elem.clear()

        root.clear()

# Run the function
parse_arxiv_xml(input_xml_file, output_csv_file)

print(f"✅ CSV file '{output_csv_file}' has been updated successfully!")
