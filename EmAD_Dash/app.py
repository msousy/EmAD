import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import time
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

from  components.main_data_tabs import *


data_tabs_callbacks(app)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",

}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("EmAD", className="display-4"),
        html.Hr(),
        html.P(
            "Anomaly detection framework for ARM based Embedded Systems", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("1. Data Preparation", href="/page-1", id="page-1-link"),
                dbc.NavLink("2. Model Raining", href="/page-2", id="page-2-link"),
                dbc.NavLink("3. Deployment", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content, dcc.Store(id="data_store")])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return taps_with_graphs
    elif pathname == "/page-2":
        return "TODO/ Model training"
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

'''Taps callbacks '''

'''Taps callbacks '''


if __name__ == "__main__":
    app.run_server(debug=True, port=4444, host='0.0.0.0')