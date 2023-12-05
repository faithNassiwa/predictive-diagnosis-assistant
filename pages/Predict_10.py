import streamlit as st
import joblib
import numpy as np
from xgboost import XGBClassifier
from utils import *
import os

st.title('Predictive Diagnosis Assistant')
# Load trained model
model = joblib.load(os.path.abspath('trained_models/xgboost_10.joblib'))


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
            responses = process_responses_20(swollen_lymph_nodes, hiv_intercourse, taking_noacs, chronic_copd, heart_failure,
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

            st.write(f"**Top 3 Possible Diagnoses:**")
            for key, value in top3_diseases_prob.items() :
                st.write(f"- {key}: `{value*100:.2f}`%")


medical_questionnaire()

