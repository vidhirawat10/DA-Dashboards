# app.py

from dash import Dash

# Define the external stylesheet for dark mode
# You can find more themes here: https://dash.plotly.com/external-resources
external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css']

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
server = app.server