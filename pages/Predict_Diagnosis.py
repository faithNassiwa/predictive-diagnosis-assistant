import streamlit as st

st.title('Predictive Diagnosis Assistant')

with st.container():
    st.subheader('Health History and Conditions')
    col1, col2 = st.columns(2)
    with col1:
        hiv_contact = st.radio('Have you had sexual intercourse with an HIV-positive partner in '
                                                    'the past 12 months?', options=['Yes', 'No'], index=1, horizontal=True)
        cancer = st.radio("Do you have an active cancer?", ['Yes', 'No'], index=1, horizontal=True)
        mood_changes = st.radio("Are you more irritable or has your mood been very unstable recently?", ['Yes', 'No'],
                                index=1, horizontal=True)
        mouth_ulcers = st.radio("Do you have painful mouth ulcers or sores?", ['Yes', 'No'], index=1, horizontal=True)
    with col2:
        ear_infection = st.radio(
            "Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection?",
            ['Yes', 'No'], index=1, horizontal=True)
        immobility = st.radio(
            "Have you been unable to move or get up for more than 3 consecutive days within the last 4 weeks?",
            ['Yes', 'No'], index=1, horizontal=True)
        kidney_problem = st.radio("Do you have a known kidney problem resulting in an inability to retain proteins?",
                                  ['Yes', 'No'], index=1, horizontal=True)
        allergy_contact = st.radio("Have you been in contact with or ate something that you have an allergy to?",
                                   ['Yes', 'No'], index=1, horizontal=True)

    st.subheader('Lifestyle and Environmental Factors')
    col3, col4 = st.columns(2)
    with col3:
        unprotected_sex = st.radio("Have you had unprotected sex with more than one partner in the last 6 months?",
                                   ['Yes', 'No'], index=1, horizontal=True)
        lung_cancer_family = st.radio("Do you have family members who have had lung cancer?", ['Yes', 'No'],
                                      index=1, horizontal=True)
        high_blood_pressure = st.radio("Are you consulting because you have high blood pressure?", ['Yes', 'No'],
                                       index=1, horizontal=True)
        agriculture_work = st.radio("Do you work in agriculture?", ['Yes', 'No'], index=1, horizontal=True)

    with col4:
        energy_drinks = st.radio("Do you consume energy drinks regularly?", ['Yes', 'No'], index=1, horizontal=True)
        mining_work = st.radio("Do you work in the mining sector?", ['Yes', 'No'], index=1, horizontal=True)
        construction_work = st.radio("Do you work in construction?", ['Yes', 'No'], index=1, horizontal=True)
        secondhand_smoke = st.radio("Are you exposed to secondhand cigarette smoke on a daily basis?",
                                    ['Yes', 'No'], index=1, horizontal=True)

    st.subheader('Symptoms and Recent Changes')
    col5, col6 = st.columns(2)
    with col5:
        chills = st.radio("Have you had chills or shivers?", ['Yes', 'No'], index=1, horizontal=True)
        red_cheeks = st.radio("Did your cheeks suddenly turn red?", ['Yes', 'No'], index=1, horizontal=True)
        weight_loss = st.radio("Have you been unintentionally losing weight or have you lost your appetite?",
                               ['Yes', 'No'], index=1, horizontal=True)
        asthma_attacks = st.radio("Have you had 2 or more asthma attacks in the past year?", ['Yes', 'No'], index=1,
                                  horizontal=True)
    with col6:
        facial_weakness = st.radio("Have you noticed weakness in your facial muscles and/or eyes?", ['Yes', 'No'],
                                   index=1, horizontal=True)
        bloated_abdomen = st.radio(
            "Do you feel your abdomen is bloated or distended (swollen due to pressure from inside)?", ['Yes', 'No'],
            index=1, horizontal=True)
        double_vision = st.radio(
            "Do you have the perception of seeing two images of a single object seen overlapping or adjacent to each other (double vision)?",
            ['Yes', 'No'], index=1, horizontal=True)
        sore_throat = st.radio("Do you have a sore throat?", ['Yes', 'No'], index=1, horizontal=True)


