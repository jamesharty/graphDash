import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from myproject import db
from myproject.models import Animal

animals = Animal.query.all()


###################################
############ HTML PART ############
###################################

#################################
############ Nav Bar ############
#################################
from navbar import Navbar
navbar = Navbar()

##############################
############ Body ############
##############################

body = dbc.Container([
    html.H1(children='Animal Data Display'),

    html.Div(children='''
        ID of Animal To Display
    '''),
    dcc.Input(id='input',value='',type='text'),
    html.Div(id='output-graph',children=[
        dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1], 'y': [0], 'type': 'bar', 'name': 'Water Efficiency'},
                        {'x': [1.5], 'y': [0], 'type': 'bar', 'name': 'Methane Production'},
                        {'x': [2], 'y': [0], 'type': 'bar', 'name': 'Feed Efficiency'},
                    ],
                    'layout': {
                        'title':( "Data for animal")
                    }
                }
            )]),
    html.Div(id='details', children=[
        dbc.Card(  
                    [
                        dbc.CardBody(
                            [
                                html.H4("Animal ID: ", className="card-title"),
                                html.P(
                                    dbc.ListGroup( 
                                            [
                                                dbc.ListGroupItem("Mother ID: "),
                                                dbc.ListGroupItem("Father ID: "),
                                                dbc.ListGroupItem( "Number of Siblings: "),
                                                dbc.ListGroupItem( "Diet : "),
                                                dbc.ListGroupItem( "Start Weight : "),
                                                dbc.ListGroupItem( "Final Weight : "),
                                            ]    
                                        )
                                ),
                            ]
                        ),
                    ],
                   
                )
    ]),
])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([navbar,body])
##################################################
############ Check Number Of Siblings ############
##################################################
def check_siblings(idInput):
    numberOfSiblings =-1

    for x in animals:
        id=x.animalID
        if idInput == id:
            mID=x.motherID
            fID=x.fatherID
            for y in animals:
                if y.motherID == mID or y.fatherID ==fID :
                    numberOfSiblings= numberOfSiblings +1
                
                else:
                    pass
        
            return numberOfSiblings

        else:
            pass
        
######################################
############ Update Graph ############
######################################
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')], 
)
def update_graph(input_data):
    
    for x in animals:
        id=x.animalID
        idInput =int(input_data)
        if idInput == id:
            fe =x.feedEfficiency
            mp = x.ch4_daily_mean
            we = x.waterEfficieny
               
            return dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1], 'y': [we], 'type': 'bar', 'name': 'Water Efficiency'},
                        {'x': [1.5], 'y': [mp], 'type': 'bar', 'name': 'Methane Production'},
                        {'x': [2], 'y': [fe], 'type': 'bar', 'name': 'Feed Efficiency'},
                    ],
                    'layout': {
                        'title':( "Data for animal")
                    }
                }
            )
        else:
            pass

############################################
############ Update Detail Card ############
############################################
@app.callback(
    Output(component_id='details', component_property='children'),
    [Input(component_id='input', component_property='value')], 
)
def update_card(input_data):
    for x in animals:
        id=x.animalID
        idInput =int(input_data)
        if idInput == id:
            startW = x.startWeight
            finalW = x.finalWeight
            mID = x.motherID
            fID = x.fatherID
            diet =x.diet
            numberOfSiblings= check_siblings(idInput)
            print(numberOfSiblings)
               
            return dbc.Card(  
                    [
                        dbc.CardBody(
                            [
                                html.H4("Animal ID: {}".format(input_data), className="card-title"),
                                html.P(
                                    dbc.ListGroup( 
                                            [
                                                dbc.ListGroupItem("Mother ID: {}".format(mID)),
                                                dbc.ListGroupItem("Father ID: {}".format(fID)),
                                                dbc.ListGroupItem( "Number of Siblings: {}".format(numberOfSiblings)),
                                                dbc.ListGroupItem( "Diet : {}".format(diet)),
                                                dbc.ListGroupItem( "Start Weight : {}".format(startW)),
                                                dbc.ListGroupItem( "Final Weight : {}".format(finalW)),
                                            ]
                                            
                                        )
                                ),
                            ]
                        ),
                    ],
                   
                )
        else:
            pass


if __name__ == '__main__':
    app.run_server(debug=False)