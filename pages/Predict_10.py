import streamlit as st
import joblib
import pandas as pd
import numpy as np
from xgboost import XGBClassifier

st.title('Predictive Diagnosis Assistant')

# Load trained model
model = joblib.load('/Users/faith/Desktop/MSDS/NEU/Semesters/Fall2023/DS5500/Project/predictive-diagnosis-assistant/trained_models/xgboost_10.joblib')

# disease mapping
mapping_dict = {1: 0, 6: 1, 7: 2, 8: 3, 13: 4, 23: 5, 27: 6, 36: 7, 44: 8, 46: 9}
disease_dict = {44: 'URTI', 46: 'Viral pharyngitis', 8: 'Anemia', 23: 'HIV (initial infection)', 27: 'Localized edema', 7: 'Anaphylaxis', 36: 'Pulmonary embolism', 13: 'Influenza', 6: 'Bronchitis', 1: 'Allergic sinusitis'}


def get_key_by_value(dict, search_value):
    for key, value in dict.items():
        if value == search_value:
            return key
    return None  # Return None if the value is not found

def convert_number_to_disease(num, mapping_dict=mapping_dict, disease_dict=disease_dict):
    # Check if the number is in the mapping dictionary
    if num in mapping_dict.values():
        # Get the corresponding number from the mapping dictionary
        mapped_num = get_key_by_value(mapping_dict, num)
        # Now get the disease name using this number
        disease_name = disease_dict.get(mapped_num, "Unknown Disease")
        return disease_name
    else:
        return "Unknown Disease"


def boolean_format(input_text):
    return 1 if input_text == 'Yes' else 0


def convert_rash_color_to_value(color):
    # Mapping of rash colors to their numeric values
    color_to_value = {
        '0': 0, 'pale': 1, 'pink': 2, 'red': 3, 'yellow': 4
    }

    return color_to_value.get(color, 0)  # Returns 0 if color is not found


def convert_affected_region_to_value(region):
    # Mapping of regions to their numeric values
    region_to_value = {
        '0': 0, 'ankle(L)': 1, 'ankle(R)': 2, 'back of the neck': 3, 'belly': 4,
        'bottom lip(R)': 5, 'buttock(L)': 6, 'buttock(R)': 7, 'cervical spine': 8,
        'cheek(L)': 9, 'cheek(R)': 10, 'commissure(L)': 11, 'commissure(R)': 12,
        'dorsal aspect of the hand(R)': 13, 'epigastric': 14, 'flank(L)': 15,
        'flank(R)': 16, 'forehead': 17, 'iliac fossa(L)': 18, 'iliac fossa(R)': 19,
        'internal cheek(L)': 20, 'internal cheek(R)': 21, 'labia minora(L)': 22,
        'labia minora(R)': 23, 'lumbar spine': 24, 'nose': 25, 'palace': 26, 'penis': 27,
        'posterior chest wall(L)': 28, 'posterior chest wall(R)': 29, 'scrotum': 30,
        'shoulder(L)': 31, 'shoulder(R)': 32, 'side of the neck(L)': 33,
        'side of the neck(R)': 34, 'testicle(L)': 35, 'testicle(R)': 36, 'thigh(L)': 37,
        'thigh(R)': 38, 'thoracic spine': 39, 'thyroid cartilage': 40,
        'under the tongue': 41, 'upper lip(R)': 42
    }

    return region_to_value.get(region, 0)  # Returns 0 if region is not found


def convert_location_to_value(location):
    # Mapping of locations to their numeric values
    location_to_value = {
        '0': 0, 'ankle(L)': 1, 'ankle(R)': 2, 'calf(L)': 3, 'calf(R)': 4,
        'cheek(L)': 5, 'cheek(R)': 6, 'dorsal aspect of the foot(L)': 7,
        'dorsal aspect of the foot(R)': 8, 'forehead': 9, 'nose': 10,
        'nowhere': 11, 'posterior aspect of the ankle(L)': 12,
        'posterior aspect of the ankle(R)': 13, 'sole(L)': 14, 'sole(R)': 15,
        'thigh(L)': 16, 'thigh(R)': 17, 'tibia(L)': 18, 'tibia(R)': 19,
        'toe (1)(L)': 20, 'toe (1)(R)': 21, 'toe (2)(R)': 22
    }

    return location_to_value.get(location, 0)  # Returns 0 if region is not found


# Function to collect responses from the form
def process_responses(swollen_lymph_nodes, hiv_intercourse, taking_noacs, chronic_copd, heart_failure,
                      diagnosis_of_anemia, had_sti, skin_issues, taken_antipsychotics, unprotected_sex,
                      itchy_nose_throat, recent_surgery, take_stimulant_drugs, exposed_to_smoke, immunosuppressed,
                      pain_related, severe_eye_itching,rash_color, swelling_location, affected_region ):
    # This function should collect all responses from the form
    # and format them in the way your model expects (e.g., as a list or array)
    data = {
        "Do you have swollen or painful lymph nodes?": int(boolean_format(swollen_lymph_nodes)) ,
        "Have you had sexual intercourse with an HIV-positive partner in the past 12 months?": int(boolean_format(hiv_intercourse)),
        "Are you taking any new oral anticoagulants ((NOACs)?": int(boolean_format(taking_noacs)),
        "Have you had unprotected sex with more than one partner in the last 6 months?": int(
            boolean_format(unprotected_sex)),
        "Is your nose or the back of your throat itchy?": int(boolean_format(itchy_nose_throat)),
        "Are you immunosuppressed?": int(boolean_format(immunosuppressed)),
        "Have you had surgery within the last month?": int(boolean_format(recent_surgery)),
        "Do you have a chronic obstructive pulmonary disease (COPD)?": int(boolean_format(chronic_copd)),
        "Do you regularly take stimulant drugs?": int(boolean_format(take_stimulant_drugs)),
        "Are you exposed to secondhand cigarette smoke on a daily basis?": int(boolean_format(exposed_to_smoke)),
        "Do you have heart failure?": int(boolean_format(heart_failure)),
        "What color is the rash?": int(convert_rash_color_to_value(rash_color)),
        "Have you ever had a diagnosis of anemia?": int(boolean_format(diagnosis_of_anemia)),
        "Where is the swelling located?": int(convert_location_to_value(swelling_location)),
        "Have you ever had a sexually transmitted infection?": int(boolean_format(had_sti)),
        "Where is the affected region located?": int(convert_affected_region_to_value(affected_region)),
        "Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?": int(boolean_format(skin_issues)),
        "Have you started or taken any antipsychotic medication within the last 7 days?": int(boolean_format(taken_antipsychotics)),
        "Do you have pain somewhere, related to your reason for consulting?": int(boolean_format(pain_related)),
        "Do you have severe itching in one or both eyes?": int(boolean_format(severe_eye_itching))
    }
    features = pd.DataFrame(data, index=[0])
    return features


def medical_questionnaire():
    with st.form("medical_questionnaire"):
        # Medical History
        st.subheader("Medical History")
        swollen_lymph_nodes = st.radio("Do you have swollen or painful lymph nodes?", ['Yes', 'No'], index=1)
        hiv_intercourse = st.radio("Have you had sexual intercourse with an HIV-positive partner in the past 12 months?", ['Yes', 'No'], index=1)
        taking_noacs = st.radio("Are you taking any new oral anticoagulants (NOACs)?", ['Yes', 'No'], index=1)
        chronic_copd = st.radio("Do you have a chronic obstructive pulmonary disease (COPD)?", ['Yes', 'No'], index=1)
        heart_failure = st.radio("Do you have heart failure?", ['Yes', 'No'], index=1)
        diagnosis_of_anemia = st.radio("Have you ever had a diagnosis of anemia?", ['Yes', 'No'], index=1)
        had_sti = st.radio("Have you ever had a sexually transmitted infection?", ['Yes', 'No'], index=1)
        skin_issues = st.radio("Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?", ['Yes', 'No'], index=1)
        taken_antipsychotics = st.radio("Have you started or taken any antipsychotic medication within the last 7 days?", ['Yes', 'No'], index=1)

        # Lifestyle and Environmental Factors
        st.subheader("Lifestyle and Environmental Factors")
        unprotected_sex = st.radio("Have you had unprotected sex with more than one partner in the last 6 months?", ['Yes', 'No'], index=1)
        itchy_nose_throat = st.radio("Is your nose or the back of your throat itchy?", ['Yes', 'No'], index=1)
        recent_surgery = st.radio("Have you had surgery within the last month?", ['Yes', 'No'], index=1)
        take_stimulant_drugs = st.radio("Do you regularly take stimulant drugs?", ['Yes', 'No'], index=1)
        exposed_to_smoke = st.radio("Are you exposed to secondhand cigarette smoke on a daily basis?", ['Yes', 'No'], index=1)

        # Social History
        st.subheader("Social History")
        immunosuppressed = st.radio("Are you immunosuppressed?", ['Yes', 'No'], index=1)
        pain_related = st.radio("Do you have pain somewhere, related to your reason for consulting?", ['Yes', 'No'], index=1)
        severe_eye_itching = st.radio("Do you have severe itching in one or both eyes?", ['Yes', 'No'], index=1)

        # Multiple Choice Questions
        st.subheader("Additional Details")
        rash_color_options = ['0', 'pale', 'pink', 'yellow', 'red']
        rash_color = st.selectbox("What color is the rash?", rash_color_options)

        swelling_location_options = ['0', 'cheek(L)', 'tibia(L)', 'nowhere', 'dorsal aspect of the foot(R)', 'nose', 'calf(R)', 'dorsal aspect of the foot(L)', 'calf(L)', 'sole(L)', 'posterior aspect of the ankle(L)', 'sole(R)', 'tibia(R)', 'cheek(R)', 'posterior aspect of the ankle(R)', 'ankle(L)', 'forehead', 'thigh(R)', 'ankle(R)', 'thigh(L)', 'toe (1)(R)', 'toe (1)(L)', 'toe (2)(R)']
        swelling_location = st.selectbox("Where is the swelling located?", swelling_location_options)

        affected_region_options = ['0', 'internal cheek(L)', 'flank(L)', 'ankle(R)', 'thoracic spine', 'iliac fossa(L)', 'epigastric', 'nose',
                                   'cervical spine', 'commissure(L)', 'thyroid cartilage', 'forehead', 'ankle(L)', 'side of the neck(R)', 'bottom lip(R)',
                                   'penis', 'iliac fossa(R)', 'shoulder(R)', 'buttock(L)', 'cheek(L)', 'labia minora(R)', 'side of the neck(L)', 'belly',
                                   'internal cheek(R)', 'palace', 'back of the neck', 'upper lip(R)', 'shoulder(L)', 'lumbar spine', 'posterior chest wall(R)',
                                   'posterior chest wall(L)', 'flank(R)']
        affected_region = st.selectbox("Where is the affected region located?", affected_region_options)

        predict_10 = st.form_submit_button('Predict 10')

        if predict_10:
            # Process responses
            responses = process_responses(swollen_lymph_nodes, hiv_intercourse, taking_noacs, chronic_copd, heart_failure,
                      diagnosis_of_anemia, had_sti, skin_issues, taken_antipsychotics, unprotected_sex,
                      itchy_nose_throat, recent_surgery, take_stimulant_drugs, exposed_to_smoke, immunosuppressed,
                      pain_related, severe_eye_itching,rash_color, swelling_location, affected_region)

            # Generate prediction
            prediction = model.predict(responses)

            # Display the prediction
            st.write(f"**Predicted Diagonsis:** {convert_number_to_disease(prediction[0])}")

            # Class probability
            pred_class_prob = model.predict_proba(responses)
            top_3_disease = np.argsort(-pred_class_prob, axis=1)[:, :3]
            top3_diseases_prob = {}
            # Extract the probabilities at these indices
            for indices in top_3_disease:
                for i in indices:
                    top3_diseases_prob[convert_number_to_disease(i)] = pred_class_prob[0][i]

            st.write(f"**Top 3 Possible Diagnoses**")
            for key, value in top3_diseases_prob.items() :
                st.write(f"**{key}: `{value}`%**")

medical_questionnaire()

