import dash
import dash_cytoscape as cyto
import dash_html_components as html

import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output



elements = [{'data': {'id': 'prb_id_12642', 'label': 'probe 12642'}}, {'data': {'id': '10.139.128.1', 'label': '10.139.128.1'}}, {'data': {'id': '85.112.112.225', 'label': '85.112.112.225'}}, {'data': {'id': '85.112.127.97', 'label': '85.112.127.97'}}, {'data': {'id': '85.112.127.245', 'label': '85.112.127.245'}}, {'data': {'id': '85.112.122.13', 'label': '85.112.122.13'}}, {'data': {'id': '5.143.250.113', 'label': '5.143.250.113'}}, {'data': {'id': '178.34.130.99', 'label': '178.34.130.99'}}, {'data': {'id': '185.109.23.1', 'label': '185.109.23.1'}}, {'data': {'source': 'prb_id_12642', 'target': '10.139.128.1'}}, {'data': {'source': '10.139.128.1', 'target': '85.112.112.225'}}, {'data': {'source': '85.112.112.225', 'target': '85.112.127.97'}}, {'data': {'source': '85.112.127.97', 'target': '85.112.127.245'}}, {'data': {'source': '85.112.127.245', 'target': '85.112.122.13'}}, {'data': {'source': '85.112.122.13', 'target': '5.143.250.113'}}, {'data': {'source': '5.143.250.113', 'target': '178.34.130.99'}}, {'data': {'source': '178.34.130.99', 'target': '185.109.23.1'}},{'data': {'id': 'prb_id_17718', 'label': 'probe 17718'}}, {'data': {'id': '213.208.191.121', 'label': '213.208.191.121'}}, {'data': {'id': '77.94.163.1', 'label': '77.94.163.1'}}, {'data': {'id': '77.94.160.75', 'label': '77.94.160.75'}}, {'data': {'id': '95.167.38.237', 'label': '95.167.38.237'}}, {'data': {'id': '178.34.130.99', 'label': '178.34.130.99'}}, {'data': {'id': '185.109.23.1', 'label': '185.109.23.1'}}, {'data': {'source': 'prb_id_17718', 'target': '213.208.191.121'}}, {'data': {'source': '213.208.191.121', 'target': '77.94.163.1'}}, {'data': {'source': '77.94.163.1', 'target': '77.94.160.75'}}, {'data': {'source': '77.94.160.75', 'target': '95.167.38.237'}}, {'data': {'source': '95.167.38.237', 'target': '178.34.130.99'}}, {'data': {'source': '178.34.130.99', 'target': '185.109.23.1'}}, {'data': {'id': 'prb_id_22690', 'label': 'probe 22690'}}, {'data': {'id': '93.178.232.217', 'label': '93.178.232.217'}}, {'data': {'id': '213.130.29.26', 'label': '213.130.29.26'}}, {'data': {'id': '92.50.209.93', 'label': '92.50.209.93'}}, {'data': {'id': '178.34.130.99', 'label': '178.34.130.99'}}, {'data': {'id': '185.109.23.1', 'label': '185.109.23.1'}}, {'data': {'source': 'prb_id_22690', 'target': '93.178.232.217'}}, {'data': {'source': '93.178.232.217', 'target': '213.130.29.26'}}, {'data': {'source': '213.130.29.26', 'target': '92.50.209.93'}}, {'data': {'source': '92.50.209.93', 'target': '178.34.130.99'}}, {'data': {'source': '178.34.130.99', 'target': '185.109.23.1'}}, {'data': {'id': 'prb_id_26656', 'label': 'probe 26656'}}, {'data': {'id': '192.168.98.1', 'label': '192.168.98.1'}}, {'data': {'id': '89.106.171.133', 'label': '89.106.171.133'}}, {'data': {'id': '217.67.176.249', 'label': '217.67.176.249'}}, {'data': {'id': '217.67.176.54', 'label': '217.67.176.54'}}, {'data': {'id': '90.154.110.165', 'label': '90.154.110.165'}}, {'data': {'id': '178.34.129.99', 'label': '178.34.129.99'}}, {'data': {'id': '185.109.23.1', 'label': '185.109.23.1'}}, {'data': {'source': 'prb_id_26656', 'target': '192.168.98.1'}}, {'data': {'source': '192.168.98.1', 'target': '89.106.171.133'}}, {'data': {'source': '89.106.171.133', 'target': '217.67.176.249'}}, {'data': {'source': '217.67.176.249', 'target': '217.67.176.54'}}, {'data': {'source': '217.67.176.54', 'target': '90.154.110.165'}}, {'data': {'source': '90.154.110.165', 'target': '178.34.129.99'}}, {'data': {'source': '178.34.129.99', 'target': '185.109.23.1'}},{'data': {'id': 'prb_id_31463', 'label': 'probe 31463'}}, {'data': {'id': '192.168.118.1', 'label': '192.168.118.1'}}, {'data': {'id': '192.168.101.4', 'label': '192.168.101.4'}}, {'data': {'id': '185.214.184.193', 'label': '185.214.184.193'}}, {'data': {'id': '95.167.75.178', 'label': '95.167.75.178'}}, {'data': {'id': '95.167.75.177', 'label': '95.167.75.177'}}, {'data': {'id': '178.34.129.99', 'label': '178.34.129.99'}}, {'data': {'id': '185.109.23.1', 'label': '185.109.23.1'}}, {'data': {'source': 'prb_id_31463', 'target': '192.168.118.1'}}, {'data': {'source': '192.168.118.1', 'target': '192.168.101.4'}}, {'data': {'source': '192.168.101.4', 'target': '185.214.184.193'}}, {'data': {'source': '185.214.184.193', 'target': '95.167.75.178'}}, {'data': {'source': '95.167.75.178', 'target': '95.167.75.177'}}, {'data': {'source': '95.167.75.177', 'target': '178.34.129.99'}}, {'data': {'source': '178.34.129.99', 'target': '185.109.23.1'}}]

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": "col", "value": "hi"} 
                    ],
                    value="sepal length (cm)",
                ),
            ]
        )
    ],
    body=True,
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    cyto.Cytoscape(
    id='cytoscape-layout-6',
    elements=elements,
    style={'width': '100%', 'height': '600px'},
    layout={'name': 'breadthfirst',
            'roots': '#prb_id_12642, #prb_id_17718, #prb_id_22690, #prb_id_26656, #prb_id_31463'}
)
])

if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port = 12345)
