

from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv("final_data.csv")

fig = px.line(data, x="date", y = "sales")
fig.update_layout(title_text = "Pink Morsel sales of Souls Food", title_x = 0.5)

app.layout = html.Div([
    dcc.Graph(
        id="sales_graph",
        figure=fig
    ),

    html.Label("Filter by region"),
    dcc.RadioItems(["North", "South", "East", "West"], id="region")
    
]

)

@callback(
    Output("sales_graph","figure")
    Input("region","value")
    )


if __name__ == '__main__':
    app.run(debug=True)
