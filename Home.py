import streamlit as st
import joblib
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from utils import *
import os

st.title('Predictive Diagnosis Assistant')

# Load trained model
<<<<<<< HEAD
model_top_20 = joblib.load(os.path.abspath('trained_models/xgboost_10.joblib'))
model_49 = joblib.load(os.path.abspath('trained_models/xgboost_49.joblib'))
=======
model_top_20 = joblib.load('/Users/kelly/Desktop/DS5500/predictive-diagnosis-assistant/trained_models/xgboost_10.joblib')
>>>>>>> 0786616 (102 features)

# Load test data
test_df = pd.read_csv('data/subset_test.csv')

# Preprocessing
test_df["What color is the rash?"] = test_df["What color is the rash?"].apply(lambda x: int(convert_rash_color_to_value(x)))
test_df["Where is the swelling located?"] = test_df["Where is the swelling located?"].apply(lambda x: int(convert_location_to_value(x)))
test_df["Where is the affected region located?"] = test_df["Where is the affected region located?"].apply(lambda x: int(convert_affected_region_to_value(x)))
test_df["Do your lesions peel off?"] = test_df["Do your lesions peel off?"].apply(lambda x: int(convert_lesion_peel_off_to_value(x)))
test_df["Is the lesion (or are the lesions) larger than 1cm?"] = test_df["Is the lesion (or are the lesions) larger than 1cm?"].apply(lambda x: int(convert_lesion_size_to_value(x)))

# Define session state for pagination
if 'page_index' not in st.session_state:
    st.session_state.page_index = 0

# Number of rows per page
rows_per_page = 20


# Function to process a subset of DataFrame
def process_data(df_subset):
    results = {
        'Patient ID': [],
        'Age': [],
        'Gender': [],
        'Pathology': [],
        '20 MIF Predictions': [],
        '102 MIF Predictions': []
    }

    for index, row in df_subset.iterrows():
        results['Patient ID'].append(index)
        results['Age'].append(row['AGE'])
        results['Gender'].append(row['SEX'])
        results['Pathology'].append(row['PATHOLOGY'])
        results['20 MIF Predictions'].append(get_20_mif_prediction(model_top_20, row))
        results['102 MIF Predictions'].append(get_102_mif_prediction(model_49, row))

    return pd.DataFrame(results)


# Display current page and process data for that page
start_row = st.session_state.page_index * rows_per_page
end_row = start_row + rows_per_page
current_page_df = test_df.iloc[start_row:end_row]
current_page_results_df = process_data(current_page_df)
st.dataframe(current_page_results_df)
# Convert DataFrame to HTML without the index
#html = current_page_results_df.to_html(index=False)
# Display the DataFrame in Streamlit without the index
#st.write(html, unsafe_allow_html=True)
st.write('')

# Pagination buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.empty()
with col2:
    if st.button('Previous'):
        if st.session_state.page_index > 0:
            st.session_state.page_index -= 1
with col3:
    st.empty()
with col4:
    if st.button('Next'):
        if st.session_state.page_index < len(test_df) // rows_per_page:
            st.session_state.page_index += 1

st.write('MIF > Most Important Features/Symptoms')