from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

def run_dashboard():
    # Load parsed data
    try:
        df = pd.read_csv("data/parsed_data.csv")

        # Strip whitespace from column names
        df.columns = df.columns.str.strip()

    except FileNotFoundError:
        print("Parsed data file not found. Run parse_xml.py first.")
        return

    # Create the dashboard app
    app = Dash(__name__)

    # Bar chart for total savings by employee
    fig_savings = px.bar(
        df,
        x="Employee_Name",
        y="Total_Savings",
        title="Total Savings by Employee",
        labels={"Employee_Name": "Employee", "Total_Savings": "Total Savings"},
    )

    # Pie chart for policy statuses
    fig_status = px.pie(
        df,
        names="Status",
        title="Policy Status Distribution",
    )

    app.layout = html.Div([
        html.H1("Pension Plan Dashboard"),
        dcc.Graph(figure=fig_savings),
        dcc.Graph(figure=fig_status),
    ])

    app.run_server(debug=True)

if __name__ == "__main__":
    run_dashboard()
