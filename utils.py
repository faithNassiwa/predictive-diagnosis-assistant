import pandas as pd
import numpy as np

most_important_102_features = ['Have you had sexual intercourse with an HIV-positive partner in the past 12 '
 'months?',
 'Do you have an active cancer?',
 'Are you more irritable or has your mood been very unstable recently?',
 'Do you have painful mouth ulcers or sores?',
 'Are you currently being treated or have you recently been treated with an '
 'oral antibiotic for an ear infection?',
 'Have you been unable to move or get up for more than 3 consecutive days '
 'within the last 4 weeks?',
 'Do you have a known kidney problem resulting in an inability to retain '
 'proteins?',
 'Have you been in contact with or ate something that you have an allergy to?',
 'Have you had chills or shivers?',
 'Do you have a known severe food allergy?',
 'Are you consulting because you have high blood pressure?',
 'Did your cheeks suddenly turn red?',
 'Have you been unintentionally losing weight or have you lost your appetite?',
 'Are you taking any new oral anticoagulants ((NOACs)?',
 'Have you had unprotected sex with more than one partner in the last 6 '
 'months?',
 'Have you ever had surgery to remove lymph nodes?',
 'Have you noticed weakness in your facial muscles and/or eyes?',
 'Have you had 2 or more asthma attacks in the past year?',
 'Have you started or taken any antipsychotic medication within the last 7 '
 'days?',
 'Do you have family members who have had lung cancer?',
 'Do you currently take hormones?',
 'Do you feel like you are dying or were you afraid that you were about do '
 'die?',
 'Do you feel your abdomen is bloated or distended (swollen due to pressure '
 'from inside)?',
 'Do you have a burning sensation that starts in your stomach then goes up '
 'into your throat, and can be associated with a bitter taste in your mouth?',
 'Have any of your family members been diagnosed with cluster headaches?',
 'Do your lesions peel off?',
 'Do you have numbness, loss of sensation or tingling in the feet?',
 'Have you been treated in hospital recently for nausea, agitation, '
 'intoxication or aggressive behavior and received medication via an '
 'intravenous or intramuscular route?',
 'Do you consume energy drinks regularly?',
 'Have you been able to pass stools or gas since your symptoms increased?',
 'Do you feel your heart is beating very irregularly or in a disorganized '
 'pattern?',
 'Do you have any close family members who suffer from allergies (any type), '
 'hay fever or eczema?',
 'Have you had weakness or paralysis on one side of the face, which may still '
 'be present or completely resolved?',
 'Have you recently taken decongestants or other substances that may have '
 'stimulant effects?',
 'Is your nose or the back of your throat itchy?',
 'Do you have the perception of seeing two images of a single object seen '
 'overlapping or adjacent to each other (double vision)?',
 'Did you have your first menstrual period before the age of 12?',
 'Do you regularly drink coffee or tea?',
 'Were you born prematurely or did you suffer any complication at birth?',
 'Have you been diagnosed with hyperthyroidism?',
 'Do you have cystic fibrosis?',
 'Have you vomited several times or have you made several efforts to vomit?',
 'Have you had one or several flare ups of chronic obstructive pulmonary '
 'disease (COPD) in the past year?',
 'Do you have a problem with poor circulation?',
 'Have you ever had a spontaneous pneumothorax?',
 'Do you have severe itching in one or both eyes?',
 'Do you find that your symptoms have worsened over the last 2 weeks and that '
 'progressively less effort is required to cause the symptoms?',
 'Have you ever had a diagnosis of anemia?',
 'Do you suffer from chronic anxiety?',
 'Do you work in agriculture?',
 'Do you take medication that dilates your blood vessels?',
 'Do you have a known heart defect?',
 'Do you feel out of breath with minimal physical effort?',
 'Have you been diagnosed with chronic sinusitis?',
 'Do you have pain that improves when you lean forward?',
 'Do you have Rheumatoid Arthritis?',
 'Have you had diarrhea or an increase in stool frequency?',
 'Have you or any member of your family ever had croup?',
 'Have you noticed that you produce more saliva than usual?',
 'Have you ever had fluid in your lungs?',
 'Have you ever had a pericarditis?',
 'Did you vomit after coughing?',
 'Do you have pain that is increased with movement?',
 'Do you have a sore throat?',
 'Have you ever had a sexually transmitted infection?',
 'Do you have symptoms that get worse after eating?',
 'Do you have chronic kidney failure?',
 'Are you infected with the human immunodeficiency virus (HIV)?',
 'Do you have annoying muscle spasms in your face, neck or any other part of '
 'your body?',
 'Have you ever been diagnosed with obstructive sleep apnea (OSA)?',
 'Do you work in the mining sector?',
 'Have you been in contact with a person with similar symptoms in the past 2 '
 'weeks?',
 'Do you have liver cirrhosis?',
 'Are your symptoms more prominent at night?',
 'Are the symptoms or pain increased with coughing, with an effort like '
 'lifting a weight or from forcing a bowel movement?',
 'Do you have any lesions, redness or problems on your skin that you believe '
 'are related to the condition you are consulting for?',
 'Have you noticed that the tone of your voice has become deeper, softer or '
 'hoarse?',
 'Do you have difficulty articulating words/speaking?',
 'In the last month, have you been in contact with anyone infected with the '
 'Ebola virus?',
 'Do you take a calcium channel blockers (medication)?',
 'Is the lesion (or are the lesions) larger than 1cm?',
 'Are you currently using intravenous drugs?',
 'Are you immunosuppressed?',
 'Have any of your family members ever had a pneumothorax?',
 'Do you feel that your eyes produce excessive tears?',
 'Does the person have a whooping cough?',
 'Do you feel so tired that you are unable to do your usual activities or are '
 'you stuck in your bed all day long?',
 'What color is the rash?',
 'Do you have pain or weakness in your jaw?',
 'Have you ever been diagnosed with depression?',
 'Where is the swelling located?',
 'Have you been hospitalized for an asthma attack in the past year?',
 'Do you have polyps in your nose?',
 'Do you suffer from Crohn’s disease or ulcerative colitis (UC)?',
 'Do you work in construction?',
 'Do you have pain somewhere, related to your reason for consulting?',
 'Do you have chest pain even at rest?',
 'Do you currently undergo dialysis?',
 'Do you have a poor diet?',
 'Are your vaccinations up to date?',
 'Are you exposed to secondhand cigarette smoke on a daily basis?',
 'Do you have a decrease in appetite?']

most_important_20_features = ["Do you have swollen or painful lymph nodes?" ,
        "Have you had sexual intercourse with an HIV-positive partner in the past 12 months?",
        "Are you taking any new oral anticoagulants ((NOACs)?",
        "Have you had unprotected sex with more than one partner in the last 6 months?",
        "Is your nose or the back of your throat itchy?",
        "Are you immunosuppressed?",
        "Have you had surgery within the last month?",
        "Do you have a chronic obstructive pulmonary disease (COPD)?",
        "Do you regularly take stimulant drugs?",
        "Are you exposed to secondhand cigarette smoke on a daily basis?",
        "Do you have heart failure?",
        "What color is the rash?",
        "Have you ever had a diagnosis of anemia?",
        "Where is the swelling located?",
        "Have you ever had a sexually transmitted infection?",
        "Where is the affected region located?",
        "Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?",
        "Have you started or taken any antipsychotic medication within the last 7 days?",
        "Do you have pain somewhere, related to your reason for consulting?",
        "Do you have severe itching in one or both eyes?"]



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
def process_responses_20(swollen_lymph_nodes, hiv_intercourse, taking_noacs, chronic_copd, heart_failure,
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


def convert_lesion_peel_off_to_value(peel_off):
    peel_off_to_value = {
        '0': 0,
        'N': 1,
        'Y': 2
    }

    return peel_off_to_value.get(peel_off, 0)  # Returns 0 if peel off is not found


def convert_lesion_size_to_value(lesion_size):
    lesion_size_to_value = {
        '0': 0,
        'N': 1,
        'Y': 2
    }

    return lesion_size_to_value.get(lesion_size, 0)  # Returns 0 if lesion_size is not found

test_conditions = [
    'Acute COPD exacerbation / infection', 'Acute dystonic reactions',
    'Acute laryngitis', 'Acute otitis media', 'Acute pulmonary edema',
    'Acute rhinosinusitis', 'Allergic sinusitis', 'Anaphylaxis',
    'Anemia', 'Atrial fibrillation', 'Boerhaave', 'Bronchiectasis',
    'Bronchiolitis', 'Bronchitis',
    'Bronchospasm / acute asthma exacerbation', 'Chagas',
    'Chronic rhinosinusitis', 'Cluster headache', 'Croup', 'Ebola',
    'Epiglottitis', 'GERD', 'Guillain-Barré syndrome',
    'HIV (initial infection)', 'Influenza', 'Inguinal hernia',
    'Larygospasm', 'Localized edema', 'Myasthenia gravis',
    'Myocarditis', 'PSVT', 'Pancreatic neoplasm', 'Panic attack',
    'Pericarditis', 'Pneumonia', 'Possible NSTEMI / STEMI',
    'Pulmonary embolism', 'Pulmonary neoplasm', 'SLE',
    'Scombroid food poisoning', 'Spontaneous pneumothorax',
    'Spontaneous rib fracture', 'Stable angina', 'Tuberculosis',
    'URTI', 'Unstable angina', 'Viral pharyngitis', 'Whooping cough'
]

# Create the dictionary mapping
condition_to_index = {index: condition for index, condition in enumerate(test_conditions)}


def convert_48_diseases(index):
    return condition_to_index.get(index, 'Unknown')


def get_20_mif_prediction(model, row):
    data = {most_important_20_features[i]: row[most_important_20_features[i]] for i in range(20)}
    features = pd.DataFrame(data, index=[0])

    # Diseases
    diseases = list(disease_dict.values())
    if row['PATHOLOGY'] in diseases:
        # Class probability
        pred_class_prob = model.predict_proba(features)
        # Get indices of the top 3 probabilities
        top_3_indices = np.argsort(-pred_class_prob, axis=1)[:, :3][0]

        # Get the top 3 probabilities
        top_3_probs = np.sort(pred_class_prob[0][top_3_indices])[::-1]

        # Create a dictionary mapping disease names to their probabilities
        top3_diseases_prob = {convert_number_to_disease(top_3_indices[i]): '{0}%'.format(round(top_3_probs[i]*100), 2)
                              for i in range(3)}

        return ', '.join(f"{key}: {value}" for key, value in top3_diseases_prob.items())
    else:
        return 'Out of range: {0}'.format(diseases)


def get_102_mif_prediction(model, row):
    data = {most_important_102_features[i]: row[most_important_102_features[i]] for i in range(102)}
    features = pd.DataFrame(data, index=[0])
    # Class probability
    pred_class_prob = model.predict_proba(features)
    top_3_disease = np.argsort(-pred_class_prob, axis=1)[:, :3]
    top3_diseases_prob = {}
    # Extract the probabilities at these indices
    for i in top_3_disease[0]:
        probability = '{0} %'.format(round(pred_class_prob[0][i]*100), 2)
        top3_diseases_prob[convert_48_diseases(i)] = probability

    return ', '.join(f"{key}: {value}" for key, value in top3_diseases_prob.items())

