import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State, MATCH, ALL
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server

anagrafica = pd.read_csv('data/dati_anagrafica_clean.csv')
scavo = pd.read_csv('data/dati_scavo_clean.csv')
bibliografia = pd.read_csv('data/dati_bibliografici_clean.csv')
collezionista = pd.read_csv('data/dati_collezionisti_clean.csv')
abbr_archivi = pd.read_csv('data/abbreviazioni_archivi.csv')
abbr_biblio = pd.read_csv('data/abbreviazioni_bibliografia.csv')
abbr_tipologie = pd.read_csv('data/abbreviazioni_tipologie.csv')

anagrafica.set_index('ID',inplace=True)
collezionista.set_index('ID',inplace=True)
scavo.set_index('ID',inplace=True)
bibliografia.set_index('ID',inplace=True)

dropdown_style = {
    'display':'none'
}

style_button = {
  'borderTop': '3px solid #d21f1b',
}

ricerca_anagrafica = ['ID','Reperto','Materiale','Cronologia','Nazione','Città','Museo/Collezionista','# inv.','Modalità di Acquisizione']
ricerca_scavo = ['Toponimo', 'Regio', 'Anno', 'Soprintendente', 'Architetto Direttore']
ricerca_collezione = ['Nazione', 'Città', 'Collezionista', 'Modalità di Acquisizione', 'Venditore', 'Nome', 'Nazione 2', 'Città 2']

children_tabs = []

children_tabs.append(dcc.Tab(id='tab1',label='Anagrafica',children=[html.Div(id='output-anagrafica'),html.Div(id='output-anagrafica-2')],selected_style=style_button))
children_tabs.append(dcc.Tab(id='tab2',label='Scavo',children=[html.Div(id='output-scavi'),html.Div(id='output-scavi-2')],selected_style=style_button))
children_tabs.append(dcc.Tab(id='tab3',label='Collezionisti',children=[html.Div(id='output-collezionisti'),html.Div(id='output-collezionisti-2')],selected_style=style_button))
children_tabs.append(dcc.Tab(id='tab4',label='Bibliografia',children=[html.Div(id='output-biblio'),html.Div(id='output-biblio-2')],selected_style=style_button))

app.layout = html.Div(children = [
    html.H1(children=[html.I('Memorabilia Pompeiana')], style={'font-family':'Futura','color':'#d21f1b'}),
    html.H3(children=['Antichità da Pompei nelle collezioni europee (1748-1830)'],style={'font-family':'Futura','color':'#d21f1b','margin-top':'-1.5%'}),
    html.P(children=['Autore: SILVIO LA PAGLIA - Web Designer: CHIARA PUGLIESE - Photo Editor: PASQUALE BUCCIERO'],style={'font-family':'Futura'}),
    html.Div([
        html.H5('Ricerca per anagrafica:'),
        html.Span('Seleziona il campo di ricerca: '),
        dcc.Dropdown(id='ricerca_anagrafica', options=[{'label': i, 'value': i} for i in ricerca_anagrafica]),
        html.Span(id='2',children='ID reperto: ',style={'display':'none'}),
        dcc.Dropdown(id='id_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.index if i!='Missing Value'],style=dropdown_style),
        html.Span(id='3',children='Reperto: ',style={'display':'none'}),
        dcc.Dropdown(id='reperto_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.Reperto.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='4',children='Materiale: ',style={'display':'none'}),
        dcc.Dropdown(id='materiale_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.Materiale.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='5',children='Cronologia: ',style={'display':'none'}),
        dcc.Dropdown(id='cronologia_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.Cronologia.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='6',children='Nazione: ',style={'display':'none'}),
        dcc.Dropdown(id='nazione_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.Nazione.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='7',children='Città: ',style={'display':'none'}),
        dcc.Dropdown(id='citta_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica.Città.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='8',children='Museo/Collezionista: ',style={'display':'none'}),
        dcc.Dropdown(id='museo_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica['Museo / Collezionista'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='9',children='# inventario: ',style={'display':'none'}),
        dcc.Dropdown(id='inv_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica['# inv.'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='10',children='Modalità di acquisizione: ',style={'display':'none'}),
        dcc.Dropdown(id='acquis_anagrafica', options=[{'label': i, 'value': i} for i in anagrafica['Modalità di Acquisizione'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Hr(style={'borderColor':'#d21f1b'}),
        html.H5('Ricerca per scavo:'),
        html.Span('Seleziona il campo di ricerca: '),
        dcc.Dropdown(id='ricerca_scavo', options=[{'label': i, 'value': i} for i in ricerca_scavo]),
        html.Span(id='11',children='Toponimo: ',style={'display':'none'}),
        dcc.Dropdown(id='toponimo', options=[{'label': i, 'value': i} for i in scavo.Toponimo.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='12',children='Regio: ',style={'display':'none'}),
        dcc.Dropdown(id='regio', options=[{'label': i, 'value': i} for i in scavo.Regio.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='13',children='Anno: ',style={'display':'none'}),
        dcc.Dropdown(id='anno_scavo', options=[{'label': i, 'value': i} for i in scavo.Anno.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='14',children='Soprintendente: ',style={'display':'none'}),
        dcc.Dropdown(id='soprintendente', options=[{'label': i, 'value': i} for i in scavo.Soprintendente.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='15',children='Architetto Direttore: ',style={'display':'none'}),
        dcc.Dropdown(id='architetto', options=[{'label': i, 'value': i} for i in scavo['Architetto Direttore'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Hr(style={'borderColor':'#d21f1b'}),
        html.H5('Ricerca per collezione:'),
        html.Span('Seleziona il campo di ricerca: '),
        dcc.Dropdown(id='ricerca_collezione', options=[{'label': i, 'value': i} for i in ricerca_collezione]),
        html.Span(id='16',children='Nazione: ',style={'display':'none'}),
        dcc.Dropdown(id='nazione_coll', options=[{'label': i, 'value': i} for i in collezionista.Nazione.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='17',children='Città: ',style={'display':'none'}),
        dcc.Dropdown(id='citta_coll', options=[{'label': i, 'value': i} for i in collezionista.Città.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='18',children='Collezionista: ',style={'display':'none'}),
        dcc.Dropdown(id='collezionista', options=[{'label': i, 'value': i} for i in collezionista.Collezionista.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='19',children='Modalità di Acquisizione: ',style={'display':'none'}),
        dcc.Dropdown(id='acq_coll', options=[{'label': i, 'value': i} for i in collezionista['Modalità di Acquisizione'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='20',children='Venditore: ',style={'display':'none'}),
        dcc.Dropdown(id='venditore_coll', options=[{'label': i, 'value': i} for i in collezionista.Venditore.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='21',children='Nome: ',style={'display':'none'}),
        dcc.Dropdown(id='nome_coll', options=[{'label': i, 'value': i} for i in collezionista.Nome.unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='22',children='Città 2: ',style={'display':'none'}),
        dcc.Dropdown(id='citta2_coll', options=[{'label': i, 'value': i} for i in collezionista['Città 2'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Span(id='23',children='Nazione 2: ',style={'display':'none'}),
        dcc.Dropdown(id='nazione2_coll', options=[{'label': i, 'value': i} for i in collezionista['Nazione 2'].unique() if i!='Missing Value'],style=dropdown_style),
        html.Hr(style={'borderColor':'#d21f1b'}),
        html.Br(),
    ],style={'width':'30%','float':'left'}),
    html.Div(children=[
        html.H5('Risultati della ricerca:'),
        dcc.Dropdown(id='risultati_ricerca',options=[],style={'display':'none'}),
        html.Br(),
        dcc.Tabs(children=children_tabs),
        #html.Div(id='output-anagrafica'),
        #html.Div(id='output-scavi'),
        #html.Div(id='output-collezionisti'),
        #html.Div(id='output-biblio'),
        #html.Div(id='output-anagrafica-2'),
        #html.Div(id='output-scavi-2'),
        #html.Div(id='output-collezionisti-2'),
        #html.Div(id='output-biblio-2')
    ],style={'width':'65%','float':'right'}),
    html.Div(children=[
        html.Div(children=[
            html.H5('Abbreviazioni:',style={'text':'center'}),
            dcc.Dropdown(id='scegli_abbr', options=[{'label': i, 'value': i} for i in ['Abbreviazioni Archivi','Abbreviazioni Bibliografiche','Abbreviazioni Tipologie']]),
            html.Br(),
            dcc.Dropdown(id='archivi', options=[{'label': i, 'value': i} for i in abbr_archivi.Abbreviazione.unique()],style=dropdown_style),
            dcc.Dropdown(id='biblio', options=[{'label': i, 'value': i} for i in abbr_biblio.Abbreviazione.unique()],style=dropdown_style),
            dcc.Dropdown(id='tipologie', options=[{'label': i, 'value': i} for i in abbr_tipologie.Abbreviazione.unique()],style=dropdown_style),
        ],style={'float':'right','width':'30%'}),
        html.Div(children=[
            html.H5('Risultato abbreviazione:'),
            html.Span(id='abbr_archivi',style={'display':'none'}),
            html.Span(id='abbr_biblio',style={'display':'none'}),
            html.Span(id='abbr_tipologie',style={'display':'none'}),
        ],style={'float':'left','width':'60%','margin-left':'3%'}),
        
    ],style={'display':'flex','width':'100%'}),
    html.Div(children=[html.P(children=['*Dati aggiornati al 31/12/2022'],style={'background-color':'#cdcdcd','margin':'2%','padding':'0.5%'})])
]) 

@app.callback(
    Output(component_id='archivi', component_property='style'),
    Output(component_id='biblio', component_property='style'),
    Output(component_id='tipologie', component_property='style'),
    Input(component_id='scegli_abbr', component_property='value')
)

def show_abbr(scelta):
    
    display = {'display':'none'}
    current_state = dash.callback_context.triggered
    
    if scelta is None:
        return display,display,display
    
    if current_state[0]['value'] == 'Abbreviazioni Archivi':
        return {'display':'block'},display,display

    if current_state[0]['value'] == 'Abbreviazioni Bibliografiche':
        return display,{'display':'block'},display
    
    if current_state[0]['value'] == 'Abbreviazioni Tipologie':
        return display,display,{'display':'block'}
    
@app.callback(
    Output(component_id='abbr_archivi',component_property='children'),
    Output(component_id='abbr_biblio',component_property='children'),
    Output(component_id='abbr_tipologie',component_property='children'),
    Output(component_id='abbr_archivi',component_property='style'),
    Output(component_id='abbr_biblio',component_property='style'),
    Output(component_id='abbr_tipologie',component_property='style'),
    Input(component_id='archivi',component_property='value'),
    Input(component_id='biblio',component_property='value'),
    Input(component_id='tipologie',component_property='value')
)

def show_abbr2(arch,bib,tip):
    
    current_state = dash.callback_context.triggered
    results = []
    display_no = {'display':'none'}
    display_yes = {'display':'block','margin':'1%'}
    
    if arch is None and bib is None and tip is None:
        return results, results, results, display_no, display_no, display_no
    
    id_abbr = current_state[0]['value']

    archivi = abbr_archivi[['Abbreviazione','Archivio']]
    biblio = abbr_biblio[['Abbreviazione','Bibliografia']]
    tipologie = abbr_tipologie[['Abbreviazione','Tipo']]

    archivi.set_index('Abbreviazione',inplace=True)
    biblio.set_index('Abbreviazione',inplace=True)
    tipologie.set_index('Abbreviazione',inplace=True)
    
    if current_state[0]['prop_id'] == 'archivi.value':
        
        val = archivi['Archivio'].loc[id_abbr]
        return val, results, results, display_yes, display_no, display_no
    
    if current_state[0]['prop_id'] == 'biblio.value':
        
        val = biblio['Bibliografia'].loc[id_abbr]
        return val, results, results, display_yes, display_no, display_no    
    
    if current_state[0]['prop_id'] == 'tipologie.value':
        
        val = tipologie['Tipo'].loc[id_abbr]
        return val, results, results, display_yes, display_no, display_no    
    
@app.callback(
    Output(component_id='2', component_property='style'),
    Output(component_id='3', component_property='style'),
    Output(component_id='4', component_property='style'),
    Output(component_id='5', component_property='style'),
    Output(component_id='6', component_property='style'),
    Output(component_id='7', component_property='style'),
    Output(component_id='8', component_property='style'),
    Output(component_id='9', component_property='style'),
    Output(component_id='10', component_property='style'),
    Output(component_id='id_anagrafica', component_property='style'),
    Output(component_id='reperto_anagrafica', component_property='style'),
    Output(component_id='materiale_anagrafica', component_property='style'),
    Output(component_id='cronologia_anagrafica', component_property='style'),
    Output(component_id='nazione_anagrafica', component_property='style'),
    Output(component_id='citta_anagrafica', component_property='style'),
    Output(component_id='museo_anagrafica', component_property='style'),
    Output(component_id='inv_anagrafica', component_property='style'),
    Output(component_id='acquis_anagrafica', component_property='style'),
    Output(component_id='11', component_property='style'),
    Output(component_id='12', component_property='style'),
    Output(component_id='13', component_property='style'),
    Output(component_id='14', component_property='style'),
    Output(component_id='15', component_property='style'),
    Output(component_id='toponimo', component_property='style'),
    Output(component_id='regio', component_property='style'),
    Output(component_id='anno_scavo', component_property='style'),
    Output(component_id='soprintendente', component_property='style'),
    Output(component_id='architetto', component_property='style'),
    Output(component_id='16', component_property='style'),
    Output(component_id='17', component_property='style'),
    Output(component_id='18', component_property='style'),
    Output(component_id='19', component_property='style'),
    Output(component_id='20', component_property='style'),
    Output(component_id='21', component_property='style'),
    Output(component_id='22', component_property='style'),
    Output(component_id='23', component_property='style'),
    Output(component_id='nazione_coll', component_property='style'),
    Output(component_id='citta_coll', component_property='style'),
    Output(component_id='collezionista', component_property='style'),
    Output(component_id='acq_coll', component_property='style'),
    Output(component_id='venditore_coll', component_property='style'),
    Output(component_id='nome_coll', component_property='style'),
    Output(component_id='citta2_coll', component_property='style'),
    Output(component_id='nazione2_coll', component_property='style'),
    Input(component_id='ricerca_anagrafica', component_property='value'),
    Input(component_id='ricerca_scavo', component_property='value'),
    Input(component_id='ricerca_collezione', component_property='value')
)

def show_output(value_anag, value_scavo, value_collezione):

    display = {'display':'none'}
    current_state = dash.callback_context.triggered
    
    if value_anag is None and value_scavo is None and value_collezione is None:
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    # 'Reperto','Materiale','Cronologia','Nazione','Città','Museo/Collezionista','# inv.',
    # 'Modalità di Acquisizione'
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == 'ID':
        return {'display':'block'},display,display,display,display,display,display,display,display,\
                {'display':'block'},display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == 'Reperto':
        return display,{'display':'block'},display,display,display,display,display,display,display,\
                display,{'display':'block'},display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == 'Materiale':
        return display,display,{'display':'block'},display,display,display,display,display,display,\
                display,display,{'display':'block'},display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == 'Cronologia':
        return display,display,display,{'display':'block'},display,display,display,display,display,\
                display,display,display,{'display':'block'},display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display

    if current_state[0]['prop_id'] == 'ricerca_angrafica.value' and current_state[0]['value'] == 'Nazione':
        return display,display,display,display,{'display':'block'},display,display,display,display,\
                display,display,display,display,{'display':'block'},display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_angrafica.value' and current_state[0]['value'] == 'Città':
        return display,display,display,display,display,{'display':'block'},display,display,display,\
                display,display,display,display,display,{'display':'block'},display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value']== 'Museo/Collezionista':
        return display,display,display,display,display,display,{'display':'block'},display,display,\
                display,display,display,display,display,display,{'display':'block'},display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == '# inv.':
        return display,display,display,display,display,display,display,{'display':'block'},display,\
                display,display,display,display,display,display,display,{'display':'block'},display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display

    if current_state[0]['prop_id'] == 'ricerca_anagrafica.value' and current_state[0]['value'] == 'Modalità di Acquisizione':
        return display,display,display,display,display,display,display,display,{'display':'block'},\
                display,display,display,display,display,display,display,display,{'display':'block'},\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_scavo.value' and current_state[0]['value'] == 'Toponimo':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                {'display':'block'}, display, display, display, display,\
                {'display':'block'}, display, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_scavo.value' and current_state[0]['value'] == 'Regio':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, {'display':'block'}, display, display, display,\
                display, {'display':'block'}, display, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_scavo.value' and current_state[0]['value'] == 'Anno':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, {'display':'block'}, display, display,\
                display, display, {'display':'block'}, display, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_scavo.value' and current_state[0]['value'] == 'Soprintendente':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, {'display':'block'}, display,\
                display, display, display, {'display':'block'}, display,\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_scavo.value' and current_state[0]['value'] == 'Architetto Direttore':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, {'display':'block'},\
                display, display, display, display, {'display':'block'},\
                display, display, display, display,display, display, display, display,\
                display, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Nazione':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                {'display':'block'}, display, display, display,display, display, display, display,\
                {'display':'block'}, display, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Città':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, {'display':'block'}, display, display,display, display, display, display,\
                display, {'display':'block'}, display, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Collezionista':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, {'display':'block'}, display,display, display, display, display,\
                display, display, {'display':'block'}, display,display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Modalità di Acquisizione':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, {'display':'block'},display, display, display, display,\
                display, display, display, {'display':'block'},display, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Venditore':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display, {'display':'block'}, display, display, display,\
                display, display, display, display, {'display':'block'}, display, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Nome':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display, display, {'display':'block'}, display, display,\
                display, display, display, display, display, {'display':'block'}, display, display
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Nazione 2':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display, display, display, {'display':'block'}, display,\
                display, display, display, display, display, display, {'display':'block'}, display
    
    
    if current_state[0]['prop_id'] == 'ricerca_collezione.value' and current_state[0]['value'] == 'Città 2':
        return display,display,display,display,display,display,display,display,display,\
                display,display,display,display,display,display,display,display,display,\
                display, display, display, display, display,\
                display, display, display, display, display,\
                display, display, display, display, display, display, display, {'display':'block'},\
                display, display, display, display, display, display, display, {'display':'block'}

        
@app.callback(
    Output(component_id='output-anagrafica',component_property='children'),
    Output(component_id='output-scavi',component_property='children'),
    Output(component_id='output-collezionisti',component_property='children'),
    Output(component_id='output-biblio',component_property='children'),
    Output(component_id='risultati_ricerca',component_property='style'),
    Output(component_id='risultati_ricerca',component_property='options'),
    Output(component_id='output-anagrafica',component_property='style'),
    Output(component_id='output-scavi',component_property='style'),
    Output(component_id='output-collezionisti',component_property='style'),
    Output(component_id='output-biblio',component_property='style'),
    Output(component_id='output-anagrafica-2',component_property='style'),
    Output(component_id='output-scavi-2',component_property='style'),
    Output(component_id='output-collezionisti-2',component_property='style'),
    Output(component_id='output-biblio-2',component_property='style'),
    Input(component_id='ricerca_scavo', component_property='value'),
    Input(component_id='toponimo', component_property='value'),
    Input(component_id='regio', component_property='value'),
    Input(component_id='anno_scavo', component_property='value'),
    Input(component_id='soprintendente', component_property='value'),
    Input(component_id='architetto', component_property='value'),
    Input(component_id='ricerca_anagrafica', component_property='value'),
    Input(component_id='id_anagrafica',component_property='value'),
    Input(component_id='reperto_anagrafica', component_property='value'),
    Input(component_id='materiale_anagrafica', component_property='value'),
    Input(component_id='cronologia_anagrafica', component_property='value'),
    Input(component_id='nazione_anagrafica', component_property='value'),
    Input(component_id='citta_anagrafica', component_property='value'),
    Input(component_id='museo_anagrafica', component_property='value'),
    Input(component_id='inv_anagrafica', component_property='value'),
    Input(component_id='acquis_anagrafica', component_property='value'),
    Input(component_id='ricerca_collezione', component_property='value'),
    Input(component_id='nazione_coll',component_property='value'),
    Input(component_id='citta_coll', component_property='value'),
    Input(component_id='collezionista', component_property='value'),
    Input(component_id='acq_coll', component_property='value'),
    Input(component_id='venditore_coll', component_property='value'),
    Input(component_id='nome_coll', component_property='value'),
    Input(component_id='citta2_coll', component_property='value'),
    Input(component_id='nazione2_coll', component_property='value')
)

def show_id(ric_s,topon,reg,anno_scav,soprin,arch,
            ric_a,id_a,rep_a,materiale_a,cronologia_a,nazione_a,citta_a,museo_a,inv_a,acquis_a,
            ric_c,naz_col,citta_col,coll,acq_col,venditore,nome_coll,citta2,naz2):
    
    current_state = dash.callback_context.triggered
   
    outputs_anag = []
    outputs_scavi = []
    outputs_coll = []
    outputs_biblio = []
    
    display = {'display':'none'}
    display1 = {'display':'none'}
    display2 = {'display':'none'}
    display3 = {'display':'none'}
    display7 = {'display':'none'}
    
    display4 = {'display':'none'}
    display5 = {'display':'none'}
    display6 = {'display':'none'}
    display8 = {'display':'none'}
    
    options = []
    
    if id_a is None and rep_a is None and materiale_a is None and cronologia_a is None and nazione_a is None and citta_a is None and museo_a is None and inv_a is None and acquis_a is None\
    and topon is None and reg is None and anno_scav is None and soprin is None and arch is None and\
    naz_col is None and citta_col is None and coll is None and acq_col is None and venditore is None and nome_coll is None and citta2 is None and naz2 is None:
        return outputs_anag,outputs_scavi,outputs_coll,outputs_biblio,display,[],display1,display2,display3,display7,display4,display5,display6,display8
    
    if current_state[0]['prop_id'] == 'id_anagrafica.value':
        
        id_a = current_state[0]['value']
        
        display = {'display':'none'}
        display1 = {'display':'block'}
        display2 = {'display':'block'}
        display3 = {'display':'block'}
        display7 = {'display':'block'}
        
        display4 = {'display':'none'}
        display5 = {'display':'none'}
        display6 = {'display':'none'}
        display8 = {'display':'none'}
        
        info = anagrafica.loc[[id_a]]
        scavi = scavo.loc[[id_a]]
        collezionisti = collezionista.loc[[id_a]]
        biblio = bibliografia.loc[[id_a]]

        outputs_anag.append(html.Br())
        info_c = info.columns
        # Create figure
        fig = go.Figure()

        # Constants
        img_width = 500
        img_height = 500
        scale_factor = 0.5

        # Add invisible scatter trace.
        # This trace is added to help the autoresize logic work.
        fig.add_trace(
            go.Scatter(
                x=[0, img_width * scale_factor],
                y=[0, img_height * scale_factor],
                mode="markers",
                marker_opacity=0
            )
        )

        # Configure axes
        fig.update_xaxes(
            visible=False,
            range=[0, img_width * scale_factor]
        )

        fig.update_yaxes(
            visible=False,
            range=[0, img_height * scale_factor],
            # the scaleanchor attribute ensures that the aspect ratio stays constant
            scaleanchor="x"
        )

        # Add image
        fig.add_layout_image(
            dict(
                x=0,
                sizex=img_width * scale_factor,
                y=img_height * scale_factor,
                sizey=img_height * scale_factor,
                xref="x",
                yref="y",
                opacity=1.0,
                layer="below",
                sizing="stretch",
                source="assets/DB Images/"+id_a+".jpg")
        )

        # Configure other layout
        fig.update_layout(
            width=img_width * scale_factor,
            height=img_height * scale_factor,
            margin={"l": 1, "r": 1, "t": 1, "b": 1},
            paper_bgcolor="Black"
        )
        
        img = []
        img.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'25%', 'width':'25%','float':'left','border': '2px solid #555'}))
        #img.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
        outputs_anag.append(html.Br())
        
        info_anag = []
        
        for index, row in info.iterrows():
            for c in info_c:
                if row[c]=='Missing Value' or row[c]=='...':
                    continue
                info_anag.append(html.Span(str(c)+': ',style={'font-weight': 'bold'}))
                info_anag.append(html.Span(str(row[c])))
                info_anag.append(html.Br())
        
        img.append(html.Div(children=info_anag,style={'margin-left':'2%','float':'right'}))
        outputs_anag.append(html.Div(children=img,style={'display':'flex'}))
        outputs_anag.append(html.Hr(style={'borderColor':'#d21f1b'}))

        info_scavi = []

        if len(scavi)!=0:
            
            scavi_c = scavi.columns
            id_scavo = 0
            outputs_scavi.append(html.Br())
            for index, row in scavi.iterrows():  
                id_scavo = row['ID SCAVO']
                for c in scavi_c:
                    if row[c]=='Missing Value' or row[c]=='...' or c == 'ID SCAVO':
                        continue
        
                    info_scavi.append(html.Span(str(c)+ ': ',style={'font-weight': 'bold'}))
                    info_scavi.append(html.Span(''+row[c]))
                        
                    info_scavi.append(html.Br())
                
                info_scavi.append(html.Hr(style={'borderColor':'#d21f1b'}))
                
            img2 = []
            img2.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'25%', 'width':'25%','float':'left','border': '2px solid #555'}))
            #img2.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
            img2.append(html.Div(children=info_scavi,style={'margin-left':'2%','float':'right'}))
            outputs_scavi.append(html.Div(children=img2,style={'display':'flex'}))
            
            
        info_coll = []

        if len(collezionisti)!=0:

            outputs_coll.append(html.Br())

            coll_c = collezionisti.columns
            id_collezionista = 0
            
            for index, row in collezionisti.iterrows():
                id_collezionista = row['ID COLLEZIONISTA']
                for c in coll_c:
                    if row[c]=='Missing Value' or row[c]=='...' or c == 'ID COLLEZIONISTA':
                        continue
                    info_coll.append(html.Span(str(c)+ ': ',style={'font-weight': 'bold'}))
                    info_coll.append(html.Span(''+row[c] + ' '))
                    info_coll.append(html.Br())
                    
                info_coll.append(html.Hr(style={'borderColor':'#d21f1b'})) 

            img3 = []
            img3.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'25%', 'width':'25%','float':'left','border': '2px solid #555'}))
            #img3.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
            img3.append(html.Div(children=info_coll,style={'margin-left':'2%','float':'right'}))
            outputs_coll.append(html.Div(children=img3,style={'display':'flex'}))
            
 
        outputs_biblio.append(html.Br())
        s = biblio['Bibliografia'].str.split('\n')
        img4 = []
        info_bib = []
        img4.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'25%', 'width':'25%','float':'left','border': '2px solid #555'}))
        
        for b in s[0]:
            if b == 'Missing Value':
                info_bib.append(html.P('Non ci sono dati disponibili.'))
                break
            info_bib.append(dcc.Markdown(b))

        img4.append(html.Div(children=info_bib,style={'margin-left':'2%','float':'right'}))
        outputs_biblio.append(html.Div(children=img4,style={'display':'flex'}))

    if current_state[0]['prop_id'] == 'reperto_anagrafica.value':
        
        rep_a = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        
        info = anagrafica[anagrafica['Reperto']==rep_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'materiale_anagrafica.value':
        
        materiale_a = current_state[0]['value']
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Materiale']==materiale_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'cronologia_anagrafica.value':
        
        cronologia_a = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Cronologia']==cronologia_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'nazione_anagrafica.value':
        
        nazione_a = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Nazione']==nazione_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'citta_anagrafica.value':
        
        citta = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Città']==citta_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'museo_anagrafica.value':
        
        museo = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Museo / Collezionista']==museo_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'inv_anagrafica.value':
        
        inv_a = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['# inv.']==inv_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'acquis_anagrafica.value':
        
        acquis_a = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = anagrafica[anagrafica['Modalità di Acquisizione']==acquis_a]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    
    if current_state[0]['prop_id'] == 'toponimo.value':
        
        toponimo = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = scavo[scavo['Toponimo']==toponimo]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
    
    if current_state[0]['prop_id'] == 'regio.value':
        
        regio = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = scavo[scavo['Regio']==regio]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'anno_scavo.value':
        
        anno = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = scavo[scavo['Anno']==anno]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'soprintendente.value':
        
        soprintendente = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = scavo[scavo['Soprintendente']==soprintendente]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'architetto.value':
        
        architetto = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = scavo[scavo['Architetto Direttore']==architetto]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
    
    if current_state[0]['prop_id'] == 'nazione_coll.value':
        
        naz = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Nazione']==naz]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
    
    if current_state[0]['prop_id'] == 'citta_coll.value':
        
        cit = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Città']==cit]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'collezionista.value':
        
        coll = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Collezionista']==coll]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'acq_coll.value':
        
        acq = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Modalità di Acquisizione']==acq]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'venditore_coll.value':
        
        vend = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Venditore']==ven]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'nome_coll.value':
        
        nome = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Nome']==nome]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'citta2_coll.value':
        
        c2 = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Città 2']==c2]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]
        
    if current_state[0]['prop_id'] == 'nazione2_coll.value':
        
        n2 = current_state[0]['value']
        
        display = {'display':'block'}
        display1 = {'display':'none'}
        display2 = {'display':'none'}
        display3 = {'display':'none'}
        display7 = {'display':'none'}
        display4 = {'display':'block'}
        display5 = {'display':'block'}
        display6 = {'display':'block'}
        display8 = {'display':'block'}
        outputs_anag = []
        outputs_scavi = []
        outputs_coll = []
        outputs_biblio = []
        info = collezionista[collezionista['Nazione 2']==n2]
        index_a = info.index
        
        options = [{'label': i, 'value': i} for i in index_a.unique()]

    return outputs_anag,outputs_scavi,outputs_coll,outputs_biblio,display,options,display1,display2,display3,display7,display4,display5,display6,display8
    

@app.callback(
    Output(component_id='output-anagrafica-2',component_property='children'),
    Output(component_id='output-scavi-2',component_property='children'),
    Output(component_id='output-collezionisti-2',component_property='children'),
    Output(component_id='output-biblio-2',component_property='children'),
    Input(component_id='risultati_ricerca',component_property='value')
)    

def show_output2(id_a):
    
    outputs_anag = []
    outputs_scavi = []
    outputs_coll = []
    outputs_biblio = []
    
    if id_a is None:
        return outputs_anag,outputs_scavi,outputs_coll,outputs_biblio
    
    if id_a != None:
        
    
        info = anagrafica.loc[[id_a]]
        scavi = scavo.loc[[id_a]]
        collezionisti = collezionista.loc[[id_a]]
        biblio = bibliografia.loc[[id_a]]

        info_c = info.columns
        
        # Create figure
        fig = go.Figure()

        # Constants
        img_width = 600
        img_height = 600
        scale_factor = 0.5

        # Add invisible scatter trace.
        # This trace is added to help the autoresize logic work.
        fig.add_trace(
            go.Scatter(
                x=[0, img_width * scale_factor],
                y=[0, img_height * scale_factor],
                mode="markers",
                marker_opacity=0
            )
        )

        # Configure axes
        fig.update_xaxes(
            visible=False,
            range=[0, img_width * scale_factor]
        )

        fig.update_yaxes(
            visible=False,
            range=[0, img_height * scale_factor],
            # the scaleanchor attribute ensures that the aspect ratio stays constant
            scaleanchor="x"
        )

        # Add image
        fig.add_layout_image(
            dict(
                x=0,
                sizex=img_width * scale_factor,
                y=img_height * scale_factor,
                sizey=img_height * scale_factor,
                xref="x",
                yref="y",
                opacity=1.0,
                layer="below",
                sizing="stretch",
                source="assets/DB Images/"+id_a+".jpg")
        )

        # Configure other layout
        fig.update_layout(
            width=img_width * scale_factor,
            height=img_height * scale_factor,
            margin={"l": 1, "r": 1, "t": 1, "b": 1},
            paper_bgcolor="Black"
        )
        
        img = []
        img.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'20%', 'width':'20%','float':'left','border': '2px solid #555'}))
        #img.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
        outputs_anag.append(html.Br())
        
        info_anag = []

        for index, row in info.iterrows():
            for c in info_c:
                if row[c]=='Missing Value' or row[c]=='...':
                    continue
                info_anag.append(html.Span(c+ ': ',style={'font-weight': 'bold'}))
                info_anag.append(html.Span(str(row[c])))
                info_anag.append(html.Br())
            
        img.append(html.Div(children=info_anag,style={'margin-left':'2%','float':'right'}))
        outputs_anag.append(html.Div(children=img,style={'display':'flex'}))
        outputs_anag.append(html.Hr(style={'borderColor':'#d21f1b'}))

        scavi_c = scavi.columns
        
        info_scavi = []
        outputs_scavi.append(html.Br())
        for index, row in scavi.iterrows():   
            
            for c in scavi_c:
                
                if row[c]=='Missing Value' or row[c]=='...' or c == 'ID SCAVO':
                    continue
                info_scavi.append(html.Span(c+ ': ',style={'font-weight': 'bold'}))
                info_scavi.append(html.Span(str(row[c])))
                info_scavi.append(html.Br())
            info_scavi.append(html.Hr(style={'borderColor':'#d21f1b'}))
        
        img2 = []
        img2.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'20%', 'width':'20%','float':'left','border': '2px solid #555'}))
        #img2.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
        img2.append(html.Div(children=info_scavi,style={'margin-left':'2%','float':'right'}))
        outputs_scavi.append(html.Div(children=img2,style={'display':'flex'}))

        coll_c = collezionisti.columns
        info_coll = []
        outputs_coll.append(html.Br())
        for index, row in collezionisti.iterrows():
            for c in coll_c:
                if row[c]=='Missing Value' or row[c]=='...' or c == 'ID COLLEZIONISTA':
                    continue
                info_coll.append(html.Span(c+ ': ',style={'font-weight': 'bold'}))
                info_coll.append(html.Span(str(row[c]) + ' '))
                info_coll.append(html.Br())
            info_coll.append(html.Hr(style={'borderColor':'#d21f1b'}))
        
        img3 = []
        img3.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'20%', 'width':'20%','float':'left','border': '2px solid #555'}))
        #img3.append(html.Div(children=dcc.Graph(figure=fig),style={'float':'left'}))
        img3.append(html.Div(children=info_coll,style={'margin-left':'2%','float':'right'}))
        outputs_coll.append(html.Div(children=img3,style={'display':'flex'}))

        outputs_biblio.append(html.Br())
        s = biblio['Bibliografia'].str.split('\n')
        img4 = []
        info_bib = []
        img4.append(html.Img(src="assets/DB Images/"+id_a+".jpg", style={'height':'25%', 'width':'25%','float':'left','border': '2px solid #555'}))
        
        for b in s[0]:
            if b == 'Missing Value':
                info_bib.append(html.P('Non ci sono dati disponibili.'))
                break
            info_bib.append(dcc.Markdown(b))

        img4.append(html.Div(children=info_bib,style={'margin-left':'2%','float':'right'}))
        outputs_biblio.append(html.Div(children=img4,style={'display':'flex'}))
    
    return outputs_anag,outputs_scavi,outputs_coll,outputs_biblio
    

if __name__ == '__main__':
    app.run_server()