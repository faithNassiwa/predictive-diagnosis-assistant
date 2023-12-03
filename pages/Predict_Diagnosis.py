import streamlit as st
import joblib
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from utils import *

st.title('Predictive Diagnosis Assistant')

# Load trained model
model_top_20 = joblib.load('/Users/faith/Desktop/MSDS/NEU/Semesters/Fall2023/DS5500/Project/predictive-diagnosis-assistant/trained_models/xgboost_10.joblib')
model_49 = joblib.load('/Users/faith/Desktop/MSDS/NEU/Semesters/Fall2023/DS5500/Project/predictive-diagnosis-assistant/trained_models/xgboost_49.joblib')

# Load test data
test_df = pd.read_csv('data/subset_test.csv')

# Preprocessing
test_df["What color is the rash?"] = test_df["What color is the rash?"].apply(lambda x: int(convert_rash_color_to_value(x)))
test_df["Where is the swelling located?"] = test_df["Where is the swelling located?"].apply(lambda x: int(convert_location_to_value(x)))
test_df["Where is the affected region located?"] = test_df["Where is the affected region located?"].apply(lambda x: int(convert_affected_region_to_value(x)))
test_df["Do your lesions peel off?"] = test_df["Do your lesions peel off?"].apply(lambda x: int(convert_lesion_peel_off_to_value(x)))
test_df["Is the lesion (or are the lesions) larger than 1cm?"] = test_df["Is the lesion (or are the lesions) larger than 1cm?"].apply(lambda x: int(convert_lesion_size_to_value(x)))

# Initialize the results dictionary with empty lists for each key
results = {
    'Patient ID': [],
    'Age': [],
    'Gender': [],
    'Pathology': [],
    '20 MIF Predictions': [],
    '102 MIF Predictions': []
}

# Populate dictionary with Patient details, Prognosis and Model Predictions
for index, row in test_df.iterrows():
    results['Patient ID'].append(index)
    results['Age'].append(row['AGE'])
    results['Gender'].append(row['SEX'])
    results['Pathology'].append(row['PATHOLOGY'])
    results['20 MIF Predictions'].append(get_20_mif_prediction(model_top_20, row))
    results['102 MIF Predictions'].append(get_102_mif_prediction(model_49, row))

# Create a DataFrame from the results dictionary
results_df = pd.DataFrame(results)

# Define session state for pagination
if 'page_index' not in st.session_state:
    st.session_state.page_index = 0

# Define the number of rows per page
rows_per_page = 20


# Function to display the current page of the DataFrame
def display_page(df, page_index, rows_per_page):
    start_row = page_index * rows_per_page
    end_row = start_row + rows_per_page
    return df.iloc[start_row:end_row]


# Display the DataFrame for the current page
st.dataframe(display_page(results_df, st.session_state.page_index, rows_per_page))

# Pagination buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Previous'):
        if st.session_state.page_index > 0:
            st.session_state.page_index -= 1

with col2:
    if st.button('Next'):
        if st.session_state.page_index < len(results_df) // rows_per_page:
            st.session_state.page_index += 1

