import streamlit as st
import joblib
import numpy as np
from xgboost import XGBClassifier
from utils import *
import os

st.title('Predictive Diagnosis Assistant')

# Load trained model
model = joblib.load(os.path.abspath('trained_models/xgboost_49.joblib'))


def medical_questionnaire():
    with (st.form("medical_questionnaire")):
        st.subheader("Medical History")
        hiv_exposure = st.radio("Have you had sexual intercourse with an HIV-positive partner in the past 12 months?", ['Yes', 'No'], index=1)
        active_cancer = st.radio("Do you have an active cancer?", ['Yes', 'No'], index=1)
        ulcers_sores = st.radio("Do you have painful mouth ulcers or sores?", ['Yes', 'No'], index=1)
        ear_infection = st.radio("Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection?", ['Yes', 'No'], index=1)
        mobility = st.radio("Have you been unable to move or get up for more than 3 consecutive days within the last 4 weeks?", ['Yes', 'No'], index=1)
        inability_retain_protein = st.radio("Do you have a known kidney problem resulting in an inability to retain proteins?", ['Yes', 'No'], index=1)
        allergy_exposure = st.radio("Have you been in contact with or ate something that you have an allergy to?", ['Yes', 'No'], index=1)
        chills_shivers = st.radio("Have you had chills or shivers?", ['Yes', 'No'], index=1)
        food_allergy = st.radio("Do you have a known severe food allergy?", ['Yes', 'No'], index=1)
        high_blood_pressure = st.radio("Are you consulting because you have high blood pressure?", ['Yes', 'No'], index=1)
        red_cheeks = st.radio("Did your cheeks suddenly turn red?", ['Yes', 'No'], index=1)
        weight_loss = st.radio("Have you been unintentionally losing weight or have you lost your appetite?", ['Yes', 'No'], index=1)
        NOACs = st.radio("Are you taking any new oral anticoagulants (NOACs)?", ['Yes', 'No'], index=1)
        unprotected_sex = st.radio("Have you had unprotected sex with more than one partner in the last 6 months?", ['Yes', 'No'], index=1)
        lymph_nodes = st.radio("Have you ever had surgery to remove lymph nodes?", ['Yes', 'No'], index=1)
        facial_muscles = st.radio("Have you noticed weakness in your facial muscles and/or eyes?", ['Yes', 'No'], index=1)
        asthma_attacks = st.radio("Have you had 2 or more asthma attacks in the past year?", ['Yes', 'No'], index=1)
        antipsychotic_medication = st.radio("Have you started or taken any antipsychotic medication within the last 7 days?", ['Yes', 'No'], index=1)
        lung_cancer = st.radio("Do you have family members who have had lung cancer?", ['Yes', 'No'], index=1)
        death_feeling = st.radio("Do you feel like you are dying or were you afraid that you were about to die?", ['Yes', 'No'], index=1)
        bloated_swollen_abdomen = st.radio("Do you feel your abdomen is bloated or distended (swollen due to pressure from inside)?", ['Yes', 'No'], index=1)
        burning_sensation_in_stomach = st.radio("Do you have a burning sensation that starts in your stomach then goes up into your throat, and can be associated with a bitter taste in your mouth?", ['Yes', 'No'], index=1)
        cluster_headaches = st.radio("Have any of your family members been diagnosed with cluster headaches?", ['Yes', 'No'], index=1)
        lesions_peel = st.radio("Do your lesions peel off?", ['Yes', 'No'], index=1)
        sensation_in_feet = st.radio("Do you have numbness, loss of sensation, or tingling in the feet?", ['Yes', 'No'], index=1)
        intravenous_intramuscular_route = st.radio("Have you been treated in the hospital recently for nausea, agitation, intoxication or aggressive behavior and received medication via an intravenous or intramuscular route?", ['Yes', 'No'], index=1)
        gas_ability = st.radio("Have you been able to pass stools or gas since your symptoms increased?", ['Yes', 'No'], index=1)
        irregular_heartbeat  = st.radio("Do you feel your heart is beating very irregularly or in a disorganized pattern?", ['Yes', 'No'], index=1)
        face_paralysis = st.radio("Have you had weakness or paralysis on one side of the face, which may still be present or completely resolved?", ['Yes', 'No'], index=1)
        nose_throat_itchy = st.radio("Is your nose or the back of your throat itchy?", ['Yes', 'No'], index=1)
        sight_problems = st.radio("Do you have the perception of seeing two images of a single object seen overlapping or adjacent to each other (double vision)?", ['Yes', 'No'], index=1)
        menstrual_period = st.radio("Did you have your first menstrual period before the age of 12?", ['Yes', 'No'], index=1)
        premature_birth = st.radio("Were you born prematurely or did you suffer any complication at birth?", ['Yes', 'No'], index=1)
        hyperthyroidism = st.radio("Have you been diagnosed with hyperthyroidism?", ['Yes', 'No'], index=1)
        cystic_fibrosis = st.radio("Do you have cystic fibrosis?", ['Yes', 'No'], index=1)
        vomit = st.radio("Have you vomited several times or have you made several efforts to vomit?", ['Yes', 'No'], index=1)
        sore_throat = st.radio("Do you have a sore throat?", ['Yes', 'No'], index=1)
        sti_exposure = st.radio("Have you ever had a sexually transmitted infection?", ['Yes', 'No'], index=1)
        symptoms_after_eating = st.radio("Do you have symptoms that get worse after eating?", ['Yes', 'No'], index=1)
        chronic_kidney_failure = st.radio("Do you have chronic kidney failure?", ['Yes', 'No'], index=1)
        hiv = st.radio("Are you infected with the human immunodeficiency virus (HIV)?", ['Yes', 'No'], index=1)
        muscle_spams = st.radio("Do you have annoying muscle spasms in your face, neck, or any other part of your body?", ['Yes', 'No'], index=1)
        OSA = st.radio("Have you ever been diagnosed with obstructive sleep apnea (OSA)?", ['Yes', 'No'], index=1)
        similar_symptoms = st.radio("Have you been in contact with a person with similar symptoms in the past 2 weeks?", ['Yes', 'No'], index=1)
        liver_cirrhosis = st.radio("Do you have liver cirrhosis?", ['Yes', 'No'], index=1)
        symptoms_at_night = st.radio("Are your symptoms more prominent at night?", ['Yes', 'No'], index=1)
        symptoms_progression = st.radio("Do you find that your symptoms have worsened over the last 2 weeks and that progressively less effort is required to cause the symptoms?", ["Yes", "No"], index=1)
        symptoms_increased = st.radio("Are the symptoms or pain increased with coughing, with an effort like lifting a weight or from forcing a bowel movement?", ['Yes', 'No'], index=1)
        lesions_redness = st.radio("Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?", ['Yes', 'No'], index=1)
        voice_tone = st.radio("Have you noticed that the tone of your voice has become deeper, softer or hoarse?", ['Yes', 'No'], index=1)
        difficulty_speaking = st.radio("Do you have difficulty articulating words/speaking?", ['Yes', 'No'], index=1)
        ebola_exposure = st.radio("In the last month, have you been in contact with anyone infected with the Ebola virus?", ['Yes', 'No'], index=1)
        calcium_blockers_medication = st.radio("Do you take a calcium channel blockers (medication)?", ['Yes', 'No'], index=1)
        lesions_1cm = st.radio("Is the lesion (or are the lesions) larger than 1cm?", ['Yes', 'No'], index=1)
        intravenous_drug_use = st.radio("Are you currently using intravenous drugs?", ['Yes', 'No'], index=1)
        pneumothorax_family = st.radio("Have any of your family members ever had a pneumothorax?", ['Yes', 'No'], index=1)
        pneumothorax = st.radio("Have you ever had a spontaneous pneumothorax?", ['Yes', 'No'], index=1)
        excessive_tears = st.radio("Do you feel that your eyes produce excessive tears?", ['Yes', 'No'], index=1)
        whooping_cough = st.radio("Does the person have a whooping cough?", ['Yes', 'No'], index=1)
        tiredness = st.radio("Do you feel so tired that you are unable to do your usual activities or are you stuck in your bed all day long?", ['Yes', 'No'], index=1)
        jaw_weakness = st.radio("Do you have pain or weakness in your jaw?", ['Yes', 'No'], index=1)
        depression = st.radio("Have you ever been diagnosed with depression?", ['Yes', 'No'], index=1)
        recent_asthma = st.radio("Have you been hospitalized for an asthma attack in the past year?", ['Yes', 'No'], index=1)
        nose_polyps = st.radio("Do you have polyps in your nose?", ['Yes', 'No'], index=1)
        crohns_disease = st.radio("Do you suffer from Crohn’s disease or ulcerative colitis (UC)?", ['Yes', 'No'], index=1)
        pain_location = st.radio("Do you have pain somewhere, related to your reason for consulting?", ['Yes', 'No'], index=1)
        chest_pain = st.radio("Do you have chest pain even at rest?", ['Yes', 'No'], index=1)
        dialysis = st.radio("Do you currently undergo dialysis?", ['Yes', 'No'], index=1)
        vaccinations = st.radio("Are your vaccinations up to date?", ['Yes', 'No'], index=1)
        family_allergies = st.radio("Do you have any close family members who suffer from allergies(any type),hay fever or eczema?", ['Yes', 'No'], index=1)
        copd = st.radio("Have you had one or several flare ups of chronic obstructive pulmonary disease(COPD) in the past year?", ['Yes', 'No'], index=1)
        poor_circulation = st.radio("Do you have a problem with poor circulation?", ['Yes', 'No'], index=1)
        itchy_eyes = st.radio("Do you have severe itching in one or both eyes?", ['Yes', 'No'], index=1)
        anemia = st.radio("Have you ever had a diagnosis of anemia?", ['Yes', 'No'], index=1)
        chronic_anxiety = st.radio("Do you suffer from chronic anxiety?", ['Yes', 'No'], index=1)
        blood_vessels = st.radio("Do you take medication that dilates your blood vessels?", ['Yes', 'No'], index=1)
        heart_defect = st.radio("Do you have a known heart defect?", ['Yes', 'No'], index=1)
        chronic_sinusitis = st.radio("Have you been diagnosed with chronic sinusitis?", ['Yes', 'No'], index=1)
        foreward_movement = st.radio("Do you have pain that improves when you lean forward?", ['Yes', 'No'], index=1)
        Rheumatoid_Arthritis = st.radio("Do you have Rheumatoid Arthritis?", ['Yes', 'No'], index=1)
        diarrhea_stool_frequency =st.radio ("Have you had diarrhea or an increase in stool frequency?", ['Yes', 'No'], index=1)
        croup = st.radio("Have you or any member of your family ever had croup?", ['Yes', 'No'], index=1)
        saliva_production =st.radio ("Have you noticed that you produce more saliva than usual?", ['Yes', 'No'], index=1)
        fluid_in_lungs =st.radio ("Have you ever had fluid in your lungs?", ['Yes', 'No'], index=1)
        pericarditis = st.radio("Have you ever had a pericarditis?", ['Yes', 'No'], index=1)
        vomit_after_coughing = st.radio("Did you vomit after coughing?", ['Yes', 'No'], index=1)
        pain_increase_movement = st.radio("Do you have pain that is increased with movement?", ['Yes', 'No'], index=1)
        immunosuppressed = st.radio("Are you immunosuppressed?", ['Yes', 'No'], index=1)
        construction = st.radio("Do you work in construction?", ['Yes', 'No'], index=1)
        decrease_appetite = st.radio("Do you have a decrease in appetite?", ['Yes', 'No'], index=1)

        # Lifestyle and Environmental Factors
        st.subheader("Lifestyle and Environmental Factors")

        mood_stability = st.radio("Are you more irritable or has your mood been very unstable recently?", ['Yes', 'No'], index=1)
        energy_drinks_consumption = st.radio("Do you consume energy drinks regularly?", ['Yes', 'No'], index=1)
        coffee_tea_consumption = st.radio("Do you regularly drink coffee or tea?", ['Yes', 'No'], index=1)
        cigarette_smoke_exposure = st.radio("Are you exposed to secondhand cigarette smoke on a daily basis?", ['Yes', 'No'], index=1)
        poor_diet = st.radio("Do you have a poor diet?", ['Yes', 'No'], index=1)
        decongestants = st.radio("Have you recently taken decongestants or other substances that may have stimulant effects?", ['Yes', 'No'], index=1)
        agriculture = st.radio("Do you work in agriculture?", ['Yes', 'No'], index=1)
        mining_sector = st.radio("Do you work in the mining sector?", ['Yes', 'No'], index=1)
        hormones_intake = st.radio("'Do you currently take hormones?",['Yes', 'No'], index=1 )
        out_of_breath = st.radio("Do you feel out of breath with minimal physical effort?", ['Yes', 'No'], index=1 )

        # Multiple Choice Questions
        st.subheader("Additional Details")
        rash_color_options = ['0', 'pale', 'pink', 'yellow', 'red']
        rash_color = st.selectbox("What color is the rash?", rash_color_options)

        swelling_location_options = ['0', 'cheek(L)', 'tibia(L)', 'nowhere', 'dorsal aspect of the foot(R)', 'nose', 'calf(R)', 'dorsal aspect of the foot(L)', 'calf(L)', 'sole(L)', 'posterior aspect of the ankle(L)', 'sole(R)', 'tibia(R)', 'cheek(R)', 'posterior aspect of the ankle(R)', 'ankle(L)', 'forehead', 'thigh(R)', 'ankle(R)', 'thigh(L)', 'toe (1)(R)', 'toe (1)(L)', 'toe (2)(R)']
        swelling_location = st.selectbox("Where is the swelling located?", swelling_location_options)

        predict_49 = st.form_submit_button('Predict 49')
        if predict_49:
            # Process responses
            responses = process_responses_49(hiv_exposure, active_cancer, mood_stability, ulcers_sores, ear_infection,
                                             mobility, inability_retain_protein, allergy_exposure, chills_shivers, food_allergy,
                                             high_blood_pressure, red_cheeks, weight_loss,  NOACs, unprotected_sex, lymph_nodes,
                                             facial_muscles, asthma_attacks, antipsychotic_medication, lung_cancer,
                                             hormones_intake, death_feeling, bloated_swollen_abdomen, burning_sensation_in_stomach,
                                             cluster_headaches, lesions_peel, sensation_in_feet, intravenous_intramuscular_route,
                                             energy_drinks_consumption, gas_ability, irregular_heartbeat, family_allergies,
                                             face_paralysis, decongestants, nose_throat_itchy, sight_problems, menstrual_period,
                                             coffee_tea_consumption, premature_birth, hyperthyroidism, cystic_fibrosis, vomit,
                                             copd, poor_circulation, pneumothorax, itchy_eyes, symptoms_progression, anemia, chronic_anxiety,
                                             agriculture, blood_vessels, heart_defect, out_of_breath, chronic_sinusitis,
                                             foreward_movement, Rheumatoid_Arthritis, diarrhea_stool_frequency, croup,
                                             saliva_production, fluid_in_lungs, pericarditis, vomit_after_coughing,
                                             pain_increase_movement, sore_throat, sti_exposure, symptoms_after_eating,
                                             chronic_kidney_failure, hiv, muscle_spams, OSA, mining_sector,
                                             similar_symptoms, liver_cirrhosis, symptoms_at_night, symptoms_increased,
                                             lesions_redness, voice_tone, difficulty_speaking,ebola_exposure, calcium_blockers_medication,
                                             lesions_1cm, intravenous_drug_use, immunosuppressed, pneumothorax_family,
                                             excessive_tears, whooping_cough, tiredness, jaw_weakness, depression,
                                             recent_asthma, nose_polyps, crohns_disease, construction, pain_location,
                                             chest_pain, dialysis, poor_diet, vaccinations, cigarette_smoke_exposure,
                                             decrease_appetite, rash_color, swelling_location)

            # Generate prediction
            prediction = model.predict(responses)

            # Display the prediction
            st.write(f"**Predicted Diagonsis:** {convert_48_diseases(prediction[0])}")

            # Class probability
            pred_class_prob = model.predict_proba(responses)
            top_3_disease = np.argsort(-pred_class_prob, axis=1)[:, :3]
            top3_diseases_prob = {}
            # Extract the probabilities at these indices
            for indices in top_3_disease:
                for i in indices:
                    top3_diseases_prob[convert_48_diseases(i)] = pred_class_prob[0][i]

            st.write(f"**Top 3 Possible Diagnoses:**")
            for key, value in top3_diseases_prob.items():
                st.write(f"- {key}: `{value * 100:.2f}`%")


medical_questionnaire()

