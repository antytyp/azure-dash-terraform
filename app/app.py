import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # IMPORTANT for Azure

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "40px"},
    children=[
        html.H1("Hello from Dash 🚀"),
        html.P("This Dash app is running on Azure Web App"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
