from fpdf import FPDF
import pandas as pd
import logging

logging.basicConfig(
    filename="../logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

def generate_pdf_report():
    try:
        df = pd.read_csv("../data/parsed_data.csv")
    except FileNotFoundError as e:
        logging.error(f"Data file not found: {e}")
        print("Error: Parsed data file not found. Please run parse_xml.py first.")
        return

    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Pension Plan Report", ln=True, align="C")

        for index, row in df.iterrows():
            pdf.cell(
                200, 10, txt=f"{row['Employer_Name']}: {row['Contribution_Percentage']}%", ln=True
            )

        pdf.output("../data/report.pdf")
        print("PDF report generated successfully: report.pdf")
    except Exception as e:
        logging.error(f"Error generating PDF: {e}")
        print("An error occurred while generating the PDF report. Check logs for details.")

# Uncomment for standalone testing
# generate_pdf_report()
