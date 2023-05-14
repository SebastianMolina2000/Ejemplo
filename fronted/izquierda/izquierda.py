from dash import html
import dash_bootstrap_components as dbc
from dash import dcc, html


buscador = dbc.Container(
    [
        html.H2("LOCALIDADES"),
        dcc.Dropdown (['Usaquen', 'Chapinero', 'Santa Fe','San Cristobal','Usme','Tunjuelito','Bosa','Kennedy','Fontibón','Engativá','Suba','Barrios Unidos','Teusaquillo','Los Mártires','Antonio Nariño','Puente Aranda','La Candelaria','Rafael Uribe Uribe','Ciudad Bolívar','Sumapaz'],
        value = 'Opción 1')
            ]
        )