import xml.etree.ElementTree as ET
import pandas as pd
import logging
import os

# Ensure the logs directory exists
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
LOG_FILE = os.path.join(LOG_DIR, "error.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

def parse_xml(file_path):
    try:
        logging.info(f"Parsing XML file: {file_path}")
        tree = ET.parse(file_path)
        root = tree.getroot()

        logging.info("XML file loaded successfully. Extracting data...")
        data = []

        # Extracting data for 'Mutzar'
        for product in root.findall(".//Mutzar"):
            try:
                product_code = product.findtext(".//NetuneiMutzar/KOD-MEZAHE-YATZRAN", default="N/A")
                status = product.findtext(".//NetuneiMutzar/STATUS-RESHOMA", default="N/A")
                employer_name = product.findtext(".//NetuneiMutzar/YeshutMaasik/SHEM-MAASIK", default="N/A")
                contribution_percentage = product.findtext(".//NetuneiMutzar/PerutHafrashotLePolisa/ACHUZ-HAFRASHA", default="N/A")
                employee_name = product.findtext(".//NetuneiMutzar/YeshutLakoach/SHEM-PRATI", default="N/A")
                policy_number = product.findtext(".//HeshbonotOPolisot/HeshbonOPolisa/MISPAR-POLISA-O-HESHBON", default="N/A")
                plan_name = product.findtext(".//HeshbonotOPolisot/HeshbonOPolisa/SHEM-TOCHNIT", default="N/A")
                total_savings = product.findtext(".//BlockItrot/Yitrot/PerutYitrot/TOTAL-CHISACHON-MTZBR", default="N/A")

                entry = {
                    "Product_Code": product_code,
                    "Status": status,
                    "Employer_Name": employer_name,
                    "Contribution_Percentage": contribution_percentage,
                    "Employee_Name": employee_name,
                    "Policy_Number": policy_number,
                    "Plan_Name": plan_name,
                    "Total_Savings": total_savings,
                }
                data.append(entry)

                logging.debug(f"Extracted data: {entry}")

            except AttributeError as e:
                logging.error(f"Error processing a product: {e}")
                continue

        # Save to CSV
        if data:
            output_path = "data/parsed_data.csv"
            df = pd.DataFrame(data)
            df.to_csv(output_path, index=False)
            logging.info(f"Data parsing complete. Output saved to {output_path}.")
            print(f"Data parsing complete. Output saved to {output_path}.")
        else:
            logging.warning("No data found in the XML file.")
            print("No data found in the XML file.")

    except FileNotFoundError as e:
        logging.error(f"XML file not found: {e}")
        print(f"Error: File not found at {file_path}. Check the file path.")
    except ET.ParseError as e:
        logging.error(f"Error parsing XML structure: {e}")
        print(f"Error: XML parsing failed. Ensure the XML file is correctly formatted.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    XML_FILE = "data/sample.xml"
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()  # Create the log file if it doesn't exist
    parse_xml(XML_FILE)
