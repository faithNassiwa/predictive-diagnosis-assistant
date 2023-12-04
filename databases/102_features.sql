DELIMITER //

CREATE PROCEDURE GetPatientDataWithFeatures()
BEGIN
    SELECT
        p.patient_id,
        p.age,
        p.gender AS sex,
        pred.disease_id,
        pr.disease_name AS pathology,
        e.question_text AS feature
    FROM
        patient p
    LEFT JOIN
        patient_evidence pe ON p.patient_id = pe.patient_id
    LEFT JOIN
        evidence e ON pe.evidence_id = e.evidence_id
    LEFT JOIN
        prediction pred ON p.patient_id = pred.patient_id
    LEFT JOIN
        diseases pr ON pred.disease_id = pr.disease_id
    WHERE
        e.question_text IN (
            'Have you had sexual intercourse with an HIV-positive partner in the past 12 months?',
            'Do you have an active cancer?',
            'Are you more irritable or has your mood been very unstable recently?',
            'Do you have painful mouth ulcers or sores?',
            'Are you currently being treated or have you recently been treated with an oral antibiotic for an ear infection?',
            'Have you been unable to move or get up for more than 3 consecutive days within the last 4 weeks?',
            'Do you have a known kidney problem resulting in an inability to retain proteins?',
            'Have you been in contact with or ate something that you have an allergy to?',
            'Have you had chills or shivers?',
            'Do you have a known severe food allergy?',
            'Are you consulting because you have high blood pressure?',
            'Did your cheeks suddenly turn red?',
            'Have you been unintentionally losing weight or have you lost your appetite?',
            'Are you taking any new oral anticoagulants ((NOACs)?',
            'Have you had unprotected sex with more than one partner in the last 6 months?',
            'Have you ever had surgery to remove lymph nodes?',
            'Have you noticed weakness in your facial muscles and/or eyes?',
            'Have you had 2 or more asthma attacks in the past year?',
            'Have you started or taken any antipsychotic medication within the last 7 days?',
            'Do you have family members who have had lung cancer?',
            'Do you currently take hormones?',
            'Do you feel like you are dying or were you afraid that you were about to die?',
            'Do you feel your abdomen is bloated or distended (swollen due to pressure from inside)?',
            'Do you have a burning sensation that starts in your stomach then goes up into your throat, and can be associated with a bitter taste in your mouth?',
            'Have any of your family members been diagnosed with cluster headaches?',
            'Do your lesions peel off?',
            'Do you have numbness, loss of sensation or tingling in the feet?',
            'Have you been treated in hospital recently for nausea, agitation, intoxication or aggressive behavior and received medication via an intravenous or intramuscular route?',
            'Do you consume energy drinks regularly?',
            'Have you been able to pass stools or gas since your symptoms increased?',
            'Do you feel your heart is beating very irregularly or in a disorganized pattern?',
            'Do you have any close family members who suffer from allergies (any type), hay fever or eczema?',
            'Have you had weakness or paralysis on one side of the face, which may still be present or completely resolved?',
            'Have you recently taken decongestants or other substances that may have stimulant effects?',
            'Is your nose or the back of your throat itchy?',
            'Do you have the perception of seeing two images of a single object seen overlapping or adjacent to each other (double vision)?',
            'Did you have your first menstrual period before the age of 12?',
            'Do you regularly drink coffee or tea?',
            'Were you born prematurely or did you suffer any complication at birth?',
            'Have you been diagnosed with hyperthyroidism?',
            'Do you have cystic fibrosis?',
            'Have you vomited several times or have you made several efforts to vomit?',
            'Have you had one or several flare-ups of chronic obstructive pulmonary disease (COPD) in the past year?',
            'Do you have a problem with poor circulation?',
            'Have you ever had a spontaneous pneumothorax?',
            'Do you have severe itching in one or both eyes?',
            'Do you find that your symptoms have worsened over the last 2 weeks and that progressively less effort is required to cause the symptoms?',
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
            'Have you ever had pericarditis?',
            'Did you vomit after coughing?',
            'Do you have pain that is increased with movement?',
            'Do you have a sore throat?',
            'Have you ever had a sexually transmitted infection?',
            'Do you have symptoms that get worse after eating?',
            'Do you have chronic kidney failure?',
            'Are you infected with the human immunodeficiency virus (HIV)?',
            'Do you have annoying muscle spasms in your face, neck or any other part of your body?',
            'Have you ever been diagnosed with obstructive sleep apnea (OSA)?',
            'Do you work in the mining sector?',
            'Have you been in contact with a person with similar symptoms in the past 2 weeks?',
            'Do you have liver cirrhosis?',
            'Are your symptoms more prominent at night?',
            'Are the symptoms or pain increased with coughing, with an effort like lifting a weight or from forcing a bowel movement?',
            'Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?',
            'Have you noticed that the tone of your voice has become deeper, softer or hoarse?',
            'Do you have difficulty articulating words/speaking?',
            'In the last month, have you been in contact with anyone infected with the Ebola virus?',
            'Do you take a calcium channel blocker (medication)?',
            'Is the lesion (or are the lesions) larger than 1cm?',
            'Are you currently using intravenous drugs?',
            'Are you immunosuppressed?',
            'Have any of your family members ever had a pneumothorax?',
            'Do you feel that your eyes produce excessive tears?',
            'Does the person have a whooping cough?',
            'Do you feel so tired that you are unable to do your usual activities or are you stuck in your bed all day long?',
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
            'Do you have a decrease in appetite?'
        )
    ORDER BY
        p.patient_id, e.question_text;
END //

DELIMITER ;

CALL GetPatientDataWithFeatures() ;
DROP PROCEDURE IF EXISTS GetPatientDataWithFeatures;