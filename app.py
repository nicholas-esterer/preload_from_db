import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dbm
import json
import reset_db

COLUMNS=['dogs','cats']

app=dash.Dash(__name__)
server=app.server

with dbm.open('assets/test.db','c') as some_db:
    len_keys=len(some_db.keys()) 
if len_keys == 0:
    reset_db.reset_db()

with dbm.open('assets/test.db','c') as some_db:

    app.layout=html.Div(id='main',children=[
        dash_table.DataTable(
            id='data-table',
            columns=[{
                'name': n,
                'id': n
            } for n in COLUMNS],
            data=[json.loads(some_db[k]) for k in some_db.keys()]
        )])


if __name__ == "__main__":
    app.run_server(debug=True)
