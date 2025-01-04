from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import logging

logging.basicConfig(
    filename="../logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

def run_dashboard():
    try:
        df = pd.read_csv("../data/parsed_data.csv")
    except FileNotFoundError as e:
        logging.error(f"Data file not found: {e}")
        print("Error: Parsed data file not found. Please run parse_xml.py first.")
        return

    app = Dash(__name__)

    fig = px.bar(
        df,
        x="Employer_Name",
        y="Contribution_Percentage",
        title="Employer Contributions",
        labels={"Employer_Name": "Employer", "Contribution_Percentage": "Contribution %"},
    )

    app.layout = html.Div([
        html.H1("Pension Plan Dashboard"),
        dcc.Graph(figure=fig)
    ])

    app.run_server(debug=True)

# Uncomment for standalone testing
# run_dashboard()
