from dash import Dash, html, dcc, callback, Output, Input, dash_table

app = Dash(__name__)

app.layout = html.Main()

if __name__ == '__main__': 
    app.run(debug=True)