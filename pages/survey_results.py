# pages/survey_results.py

from dash import html, dcc
import plotly.express as px
import pandas as pd
from pandas.api.types import CategoricalDtype

# Load your cleaned data (it's okay to load in each page file, or you can centralize in utils.py)
try:
    df = pd.read_csv('data/cleaned_mental_health_survey.csv')
    print("Cleaned data loaded successfully in survey_results.py.")
except FileNotFoundError:
    print("Error: 'cleaned_mental_health_survey.csv' not found. Make sure it's in the 'data/' directory.")
    # Create a dummy DataFrame if file not found to prevent errors
    df = pd.DataFrame(columns=['Gender', 'Age_Group', 'no_employees', 'treatment', 'benefits', 'family_history', 'mental_health_consequence', 'coworkers', 'supervisor', 'mental_vs_physical', 'work_interfere'])


# --- Re-apply CategoricalDtype for no_employees if not already done in cleaning script ---
employee_order = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
if 'no_employees' in df.columns: # Check if column exists before converting
    df['no_employees'] = df['no_employees'].astype(CategoricalDtype(categories=employee_order, ordered=True))

# --- Ensure critical columns are standardized if not already done in the cleaning script itself ---
def standardize_yes_no_like(series):
    series = series.astype(str).str.lower().str.strip()
    series = series.replace({
        'yes': 'Yes', 'no': 'No',
        'don\'t know': 'Don\'t Know', 'not sure': 'Don\'t Know',
        'some of them': 'Some', 'maybe': 'Don\'t Know',
        'unknown': 'Unknown', 'not applicable': 'Not applicable',
        'often': 'Often', 'sometimes': 'Sometimes', 'never': 'Never'
    })
    return series

cols_to_standardize = [
    'self_employed', 'family_history', 'treatment', 'remote_work',
    'tech_company', 'benefits', 'care_options', 'wellness_program',
    'seek_help', 'anonymity', 'leave', 'mental_health_consequence',
    'phys_health_consequence', 'coworkers', 'supervisor',
    'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
    'obs_consequence', 'work_interfere'
]
for col in cols_to_standardize:
    if col in df.columns:
        df[col] = standardize_yes_no_like(df[col])


# --- Create your plots for Section 1: Mental Health Insights ---
# Added template='plotly_dark' for dark mode plots
gender_fig = px.bar(df, x='Gender', title='Distribution of Gender', template='plotly_dark')
gender_fig.update_layout(xaxis_title='Gender', yaxis_title='Number of Respondents')

age_group_fig = px.bar(df, x='Age_Group', title='Distribution of Age Groups', template='plotly_dark')
age_group_fig.update_layout(xaxis_title='Age Group', yaxis_title='Number of Respondents')

company_size_fig = px.bar(df, x='no_employees', title='Distribution of Company Sizes', template='plotly_dark')
company_size_fig.update_layout(xaxis_title='Company Size', yaxis_title='Number of Respondents')

treatment_gender_fig = px.histogram(df, x='Gender', color='treatment', barmode='group',
                                    title='Treatment Seeking by Gender',
                                    category_orders={'treatment': ['Yes', 'No', 'Don\'t Know']},
                                    labels={'treatment': 'Sought Treatment'}, template='plotly_dark')
treatment_gender_fig.update_layout(xaxis_title='Gender', yaxis_title='Number of Respondents')

benefits_company_size_fig = px.histogram(df, x='no_employees', color='benefits', barmode='group',
                                         title='Mental Health Benefits by Company Size',
                                         category_orders={'no_employees': df['no_employees'].cat.categories, 'benefits': ['Yes', 'No', 'Don\'t Know']},
                                         labels={'benefits': 'Provides Benefits'}, template='plotly_dark')
benefits_company_size_fig.update_layout(xaxis_title='Company Size', yaxis_title='Number of Companies')

family_treatment_fig = px.histogram(df, x='family_history', color='treatment', barmode='group',
                                    title='Treatment Seeking by Family History of Mental Illness',
                                    category_orders={'family_history': ['Yes', 'No'], 'treatment': ['Yes', 'No', 'Don\'t Know']},
                                    labels={'family_history': 'Family History of Mental Illness', 'treatment': 'Sought Treatment'}, template='plotly_dark')
family_treatment_fig.update_layout(xaxis_title='Family History', yaxis_title='Number of Respondents')

coworkers_consequence_fig = px.histogram(df, x='mental_health_consequence', color='coworkers', barmode='group',
                                         title='Willingness to Discuss MH with Coworkers by Perceived Consequence',
                                         category_orders={'mental_health_consequence': ['Yes', 'No', 'Maybe'], 'coworkers': ['Yes', 'No', 'Some of them']},
                                         labels={'mental_health_consequence': 'Discussing MH has Negative Consequence', 'coworkers': 'Willing to Discuss with Coworkers'}, template='plotly_dark')
coworkers_consequence_fig.update_layout(xaxis_title='Perceived Negative Consequences', yaxis_title='Number of Respondents')

supervisor_consequence_fig = px.histogram(df, x='mental_health_consequence', color='supervisor', barmode='group',
                                          title='Willingness to Discuss MH with Supervisor by Perceived Consequence',
                                          category_orders={'mental_health_consequence': ['Yes', 'No', 'Maybe'], 'supervisor': ['Yes', 'No', 'Some of them']},
                                          labels={'mental_health_consequence': 'Discussing MH has Negative Consequence', 'supervisor': 'Willing to Discuss with Supervisor'}, template='plotly_dark')
supervisor_consequence_fig.update_layout(xaxis_title='Perceived Negative Consequences', yaxis_title='Number of Respondents')

mental_vs_physical_fig = px.bar(df, x='mental_vs_physical', title='Employer Takes Mental Health as Seriously as Physical Health?',
                               category_orders={'mental_vs_physical': ['Yes', 'No', 'Don\'t Know']}, template='plotly_dark')
mental_vs_physical_fig.update_layout(xaxis_title='Employer Perception', yaxis_title='Number of Respondents')


# --- Calculate KPIs ---
treatment_counts = df['treatment'].value_counts() if 'treatment' in df.columns else pd.Series()
total_respondents = len(df)
percent_seeking_treatment = (treatment_counts.get('Yes', 0) / total_respondents) * 100 if total_respondents > 0 else 0
kpi_treatment_text = f"**{percent_seeking_treatment:.2f}%** of respondents sought treatment."

benefits_counts = df['benefits'].value_counts() if 'benefits' in df.columns else pd.Series()
percent_with_benefits = (benefits_counts.get('Yes', 0) / total_respondents) * 100 if total_respondents > 0 else 0
kpi_benefits_text = f"**{percent_with_benefits:.2f}%** of employers provide mental health benefits."

work_interfere_respondents = df[df['work_interfere'].isin(['Yes', 'Often', 'Sometimes', 'Never'])] if 'work_interfere' in df.columns else pd.DataFrame()
total_work_interfere_respondents = len(work_interfere_respondents)
if total_work_interfere_respondents > 0:
    interference_counts = work_interfere_respondents['work_interfere'].isin(['Yes', 'Often', 'Sometimes']).sum()
    percent_interfering = (interference_counts / total_work_interfere_respondents) * 100
    kpi_interference_text = f"**{percent_interfering:.2f}%** of relevant respondents feel mental health interferes with work."
else:
    kpi_interference_text = "No relevant data for work interference percentage."


layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1200px', 'margin': 'auto', 'padding': '20px', 'color': 'white'}, # Set default text color to white
    children=[
        html.H1(children='Mental Health Survey Insights', style={'textAlign': 'center', 'color': '#66CCFF', 'marginBottom': '20px'}),
        html.Div(children='''
            Explore key findings and trends from the 2014 Mental Health in Tech Survey.
        ''', style={'textAlign': 'center', 'color': '#BBBBBB', 'marginBottom': '40px'}),

        html.Div(
            style={'backgroundColor': '#343a40', 'padding': '25px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.3)'}, # Dark background
            children=[
                html.H2(children='📊 Key Metrics', style={'borderBottom': '1px solid #555', 'paddingBottom': '10px', 'marginBottom': '20px', 'color': '#ADD8E6'}),
                html.Div([
                    html.P(dcc.Markdown(kpi_treatment_text), style={'fontSize': '1.3em', 'margin': '10px 0', 'textAlign': 'center', 'color': '#28A745'}),
                    html.P(dcc.Markdown(kpi_benefits_text), style={'fontSize': '1.3em', 'margin': '10px 0', 'textAlign': 'center', 'color': '#007BFF'}),
                    html.P(dcc.Markdown(kpi_interference_text), style={'fontSize': '1.3em', 'margin': '10px 0', 'textAlign': 'center', 'color': '#DC3545'})
                ], style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap', 'marginBottom': '30px'}),

                html.H2(children='📈 Demographic & Workplace Overview', style={'borderBottom': '1px solid #555', 'paddingBottom': '10px', 'marginBottom': '20px', 'color': '#ADD8E6', 'marginTop': '40px'}),
                html.Div([
                    dcc.Graph(id='gender-distribution-graph', figure=gender_fig),
                    dcc.Graph(id='age-group-distribution-graph', figure=age_group_fig),
                    dcc.Graph(id='company-size-distribution-graph', figure=company_size_fig),
                ]),

                html.H2(children='💖 Treatment & Support Insights', style={'borderBottom': '1px solid #555', 'paddingBottom': '10px', 'marginBottom': '20px', 'color': '#ADD8E6', 'marginTop': '40px'}),
                html.Div([
                    dcc.Graph(id='treatment-gender-graph', figure=treatment_gender_fig),
                    dcc.Graph(id='benefits-company-size-graph', figure=benefits_company_size_fig),
                    dcc.Graph(id='family-treatment-graph', figure=family_treatment_fig),
                ]),

                html.H2(children='🗣️ Workplace Stigma & Openness', style={'borderBottom': '1px solid #555', 'paddingBottom': '10px', 'marginBottom': '20px', 'color': '#ADD8E6', 'marginTop': '40px'}),
                html.Div([
                    dcc.Graph(id='coworkers-consequence-graph', figure=coworkers_consequence_fig),
                    dcc.Graph(id='supervisor-consequence-graph', figure=supervisor_consequence_fig),
                    dcc.Graph(id='mental-vs-physical-graph', figure=mental_vs_physical_fig),
                ]),
            ]
        ),

        html.Hr(style={'margin': '60px 0', 'borderTop': '1px dashed #6c757d'}),

        html.Div(html.P("© 2025 Mental Health Tracker. Data from OSMI 2014 Survey.", style={'textAlign': 'center', 'marginTop': '50px', 'fontSize': '0.9em', 'color': '#7F8C8D'}))
    ]
)