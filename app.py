import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



#import fronted
from fronted.navegador.navegador import navegador
from fronted.izquierda.izquierda import buscador
from fronted.derecha.derecha import resultado


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [  
        dbc.Row(
            [
                dbc.Col(navegador, md=12 , style={'background-color':'blue'} ),
                dbc.Col(buscador, md=12, style={'background-color'}),
                dbc.Col(resultado, md=8, style={'background-color':'red'}),
                
            ]
        ),
        
    ]
    
)



if __name__ == '__main__':
    app.run_server(debug=True)