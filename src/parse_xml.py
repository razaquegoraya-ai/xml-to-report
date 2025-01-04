import xml.etree.ElementTree as ET
import pandas as pd
import logging
import os

# Ensure the logs directory exists
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=f"{LOG_DIR}/error.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for product in root.findall(".//Mutzar"):
            try:
                entry = {
                    "Product_Code": product.find("NetuneiMutzar/KOD-MEZAHE-YATZRAN").text,
                    "Status": product.find("NetuneiMutzar/STATUS-RESHOMA").text,
                    "Employer_Name": product.find("NetuneiMutzar/YeshutMaasik/SHEM-MAASIK").text,
                    "Contribution_Percentage": product.find("NetuneiMutzar/PerutHafrashotLePolisa/ACHUZ-HAFRASHA").text,
                }
                data.append(entry)
            except AttributeError as e:
                logging.error(f"Missing data in product: {e}")

        df = pd.DataFrame(data)
        df.to_csv("../data/parsed_data.csv", index=False)
        print("Data parsing complete. Output saved to parsed_data.csv.")

    except Exception as e:
        logging.error(f"Error parsing XML: {e}")
        print("An error occurred while parsing the XML file. Check logs for details.")

# Uncomment to test the function
# parse_xml("../data/sample.xml")
