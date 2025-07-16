# pages/stress_analyzer.py

from dash import html, dcc
import pandas as pd
import numpy as np

# Load your cleaned data (if needed for dropdown options, like Country)
try:
    df = pd.read_csv('data/cleaned_mental_health_survey.csv')
except FileNotFoundError:
    print("Warning: 'cleaned_mental_health_survey.csv' not found. Some dropdowns might be empty.")
    df = pd.DataFrame({'Country': []}) # Create an empty DataFrame to avoid errors

layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1200px', 'margin': 'auto', 'padding': '20px', 'color': 'white'}, # Set default text color to white for dark mode
    children=[
        html.H1(children='Personalized Stress Analyzer', style={'textAlign': 'center', 'color': '#66CCFF', 'marginBottom': '20px'}), # Lighter blue for heading
        html.Div(children='''
            Input your lifestyle and mental health data below to get personalized feedback on your stress level.
            Click "Analyze My Stress" to see your results.
        ''', style={'textAlign': 'center', 'color': '#BBBBBB', 'marginBottom': '30px'}), # Lighter grey for subtitle

        html.Div([ # Main container for the two columns
            # Left Column: Inputs
            html.Div(
                style={'flex': 1, 'padding': '20px', 'marginRight': '15px', 'backgroundColor': '#343a40', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.3)'}, # Dark background for input section
                children=[
                    html.H3("1. Personal Info", style={'marginTop': '20px', 'color': '#ADD8E6'}), # Light blue for subheadings
                    html.Div([
                        html.Label("Age:", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}), # Lighter text
                        dcc.Slider(
                            id='input-age',
                            min=15, max=70, step=1, value=30,
                            marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(15, 71, 5)}, # Marks for sliders
                            tooltip={"placement": "bottom", "always_visible": True},
                            className='dark-slider' # Custom class if needed for specific slider styling
                        ),
                    ], style={'marginBottom': '25px'}),

                    html.Div([
                        html.Label("Gender:", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Dropdown(
                            id='input-gender',
                            options=[
                                {'label': 'Male', 'value': 'Male'},
                                {'label': 'Female', 'value': 'Female'},
                                {'label': 'Non-binary', 'value': 'Non-binary'},
                                {'label': 'Prefer not to say', 'value': 'Prefer not to say'}
                            ],
                            value='Male',
                            clearable=False,
                            style={'backgroundColor': '#454d55', 'color': 'white'}, # Dark dropdown background
                            className='dark-dropdown' # For specific CSS if needed
                        ),
                    ], style={'marginBottom': '25px'}),

                    html.Div([
                        html.Label("Work Role (Optional):", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Input(
                            id='input-work-role',
                            type='text',
                            placeholder='e.g., Software Engineer',
                            style={'width': '100%', 'padding': '8px', 'border': '1px solid #6c757d', 'borderRadius': '4px', 'backgroundColor': '#454d55', 'color': 'white'}, # Dark input field
                        ),
                    ], style={'marginBottom': '25px'}),

                    html.Div([
                        html.Label("Country (Optional):", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Dropdown(
                            id='input-country',
                            options=[{'label': country, 'value': country} for country in df['Country'].unique()] if not df.empty else [],
                            placeholder='Select your country',
                            style={'backgroundColor': '#454d55', 'color': 'white'},
                            className='dark-dropdown'
                        ),
                    ], style={'marginBottom': '25px'}),

                    html.H3("2. Lifestyle & Behavior", style={'marginTop': '30px', 'color': '#ADD8E6'}),
                    html.Div([
                        html.Label("Sleep Hours per day:", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Slider(id='input-sleep', min=0, max=12, step=0.5, value=7, marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(0, 13)}, tooltip={"placement": "bottom", "always_visible": True}, className='dark-slider'),
                    ], style={'marginBottom': '25px'}),
                    html.Div([
                        html.Label("Work Hours per day:", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Slider(id='input-work-hours', min=0, max=16, step=0.5, value=8, marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(0, 17)}, tooltip={"placement": "bottom", "always_visible": True}, className='dark-slider'),
                    ], style={'marginBottom': '25px'}),
                    html.Div([
                        html.Label("Screen Time per day (hours):", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Slider(id='input-screen-time', min=0, max=16, step=0.5, value=6, marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(0, 17)}, tooltip={"placement": "bottom", "always_visible": True}, className='dark-slider'),
                    ], style={'marginBottom': '25px'}),
                    html.Div([
                        html.Label("Physical Activity (minutes per day):", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Slider(id='input-activity', min=0, max=120, step=5, value=30, marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(0, 121, 15)}, tooltip={"placement": "bottom", "always_visible": True}, className='dark-slider'),
                    ], style={'marginBottom': '25px'}),
                    html.Div([
                        html.Label("Caffeine Intake (cups per day):", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.Slider(id='input-caffeine', min=0, max=10, step=1, value=2, marks={i: {'label': str(i), 'style': {'color': '#AAAAAA'}} for i in range(0, 11)}, tooltip={"placement": "bottom", "always_visible": True}, className='dark-slider'),
                    ], style={'marginBottom': '25px'}),

                    html.H3("3. Mental Health Questionnaire", style={'marginTop': '30px', 'color': '#ADD8E6'}),
                    html.Div([
                        html.Label("Do you feel stressed more than usual?", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.RadioItems(id='q-stressed', options=['Never', 'Sometimes', 'Often', 'Always'], value='Sometimes', inline=True, labelStyle={'display': 'inline-block', 'marginRight': '20px', 'color': '#BBBBBB'}),
                    ], style={'marginBottom': '15px'}),
                    html.Div([
                        html.Label("Do you feel your mental health interferes with your work/study?", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.RadioItems(id='q-interfere', options=['Yes', 'No', 'Sometimes'], value='No', inline=True, labelStyle={'display': 'inline-block', 'marginRight': '20px', 'color': '#BBBBBB'}),
                    ], style={'marginBottom': '15px'}),
                    html.Div([
                        html.Label("Do you have trouble sleeping or concentrating?", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.RadioItems(id='q-sleep-well', options=['Yes', 'No', 'Sometimes'], value='Yes', inline=True, labelStyle={'display': 'inline-block', 'marginRight': '20px', 'color': '#BBBBBB'}),
                    ], style={'marginBottom': '15px'}),
                    html.Div([
                        html.Label("Are you aware of your company/institution's mental health policies?", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.RadioItems(id='q-policies', options=['Yes', 'No'], value='No', inline=True, labelStyle={'display': 'inline-block', 'marginRight': '20px', 'color': '#BBBBBB'}),
                    ], style={'marginBottom': '15px'}),
                    html.Div([
                        html.Label("Would you talk to a supervisor or peer about your mental health?", style={'fontWeight': 'bold', 'marginBottom': '5px', 'display': 'block', 'color': '#E0E0E0'}),
                        dcc.RadioItems(id='q-talk-to-someone', options=['Yes', 'No'], value='Yes', inline=True, labelStyle={'display': 'inline-block', 'marginRight': '20px', 'color': '#BBBBBB'}),
                    ], style={'marginBottom': '30px'}),

                    html.Button('Analyze My Stress', id='analyze-button', n_clicks=0,
                                style={'marginTop': '20px', 'marginBottom': '30px', 'backgroundColor': '#28A745', 'color': 'white', 'padding': '12px 25px', 'border': 'none', 'borderRadius': '5px', 'cursor': 'pointer', 'fontSize': '1.2em', 'fontWeight': 'bold', 'display': 'block', 'margin': 'auto'}),
                ]
            ),

            # Right Column: Results
            html.Div(
                style={'flex': 1, 'padding': '20px', 'marginLeft': '15px', 'backgroundColor': '#343a40', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.3)'}, # Dark background for results section
                children=[
                    html.H3("🎯 Your Stress Score & Category", style={'textAlign': 'center', 'marginTop': '40px', 'color': '#ADD8E6'}),
                    html.Div(id='stress-score-output', style={'marginTop': '10px', 'textAlign': 'center'}),
                    html.Div(id='risk-category-output', style={'fontSize': '1.8em', 'fontWeight': 'bold', 'textAlign': 'center', 'marginBottom': '30px', 'color': '#FFF'}),

                    html.H3("📉 Summary of Risk Factors", style={'textAlign': 'center', 'color': '#ADD8E6'}),
                    html.Ul(id='risk-factors-output', style={'listStyleType': 'disc', 'paddingLeft': '40px', 'textAlign': 'left', 'maxWidth': '600px', 'margin': 'auto', 'marginBottom': '30px', 'color': '#E0E0E0'}),
                    html.H3("💡 Personalized Recommendations", style={'textAlign': 'center', 'color': '#ADD8E6'}),
                    html.Ul(id='recommendations-output', style={'listStyleType': 'disc', 'paddingLeft': '40px', 'textAlign': 'left', 'maxWidth': '600px', 'margin': 'auto', 'marginBottom': '30px', 'color': '#E0E0E0'}),

                    html.H3("🌐 Comparison with Survey Data", style={'textAlign': 'center', 'color': '#ADD8E6', 'marginTop': '40px'}),
                    html.Div(id='comparison-graph-output', style={'marginTop': '20px', 'marginBottom': '30px'})
                ]
            )
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'marginTop': '30px'}), # Flex container for columns

        html.Div(html.P("© 2025 Mental Health Tracker. Data from OSMI 2014 Survey.", style={'textAlign': 'center', 'marginTop': '50px', 'fontSize': '0.9em', 'color': '#7F8C8D'}))
    ]
)