from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# ---------- Dummy data ----------
np.random.seed(42)
df = pd.DataFrame({
    "day": pd.date_range("2025-01-01", periods=30),
    "sales": np.random.randint(50, 300, 30),
    "profit": np.random.normal(80, 20, 30),
})

# ---------- App setup ----------
app = Dash(__name__)
server = app.server  # REQUIRED for Azure / gunicorn

# ---------- Layout ----------
app.layout = html.Div(
    style={"width": "800px", "margin": "40px auto", "fontFamily": "Arial"},
    children=[
        html.H1("Interactive Sales Dashboard"),

        dcc.Dropdown(
            id="metric-dropdown",
            options=[
                {"label": "Sales", "value": "sales"},
                {"label": "Profit", "value": "profit"},
            ],
            value="sales",
            clearable=False,
            style={"width": "200px"},
        ),

        dcc.Graph(id="time-series-chart"),

        html.Div(id="summary", style={"marginTop": "20px"}),
    ],
)

# ---------- Callback ----------
@app.callback(
    Output("time-series-chart", "figure"),
    Output("summary", "children"),
    Input("metric-dropdown", "value"),
)
def update_chart(metric):
    fig = px.line(
        df,
        x="day",
        y=metric,
        markers=True,
        title=f"{metric.capitalize()} over time",
    )

    avg_value = df[metric].mean()

    summary = f"Average {metric}: {avg_value:.2f}"

    return fig, summary


# ---------- Local dev ----------
if __name__ == "__main__":
    app.run_server(debug=True)
