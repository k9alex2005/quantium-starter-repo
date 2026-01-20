

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv("final_data.csv")

fig = px.line(data, x="date", y = "sales")
fig.update_layout(title_text = "Pink Morsel sales of Souls Food", title_x = 0.5)

app.layout = html.Div([
    dcc.Graph(
        id="pink morsel sales by date",
        figure=fig
    )
]

)

if __name__ == '__main__':
    app.run(debug=True)
