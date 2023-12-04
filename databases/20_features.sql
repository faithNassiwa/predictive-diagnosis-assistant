DELIMITER //

CREATE PROCEDURE GetPatientData()
BEGIN
    SELECT
        p.patient_id,
        p.age,
        p.gender AS sex,
        pr.disease_name AS pathology,
        e.question_text AS feature
    FROM
        patient p
    JOIN
        patient_evidence pe ON p.patient_id = pe.patient_id
    JOIN
        evidence e ON pe.evidence_id = e.evidence_id
    LEFT JOIN
        prediction pred ON p.patient_id = pred.patient_id
    LEFT JOIN
        diseases pr ON pred.disease_id = pr.disease_id
    WHERE
        e.question_text IN (('Have you had sexual intercourse with an HIV-positive partner in the past 12 months?'),
           ('Do you have swollen or painful lymph nodes?'),
           ('Have you had sexual intercourse with an HIV-positive partner in the past 12 months?'),
           ('Are you taking any new oral anticoagulants ((NOACs)?'),
           ('Have you had unprotected sex with more than one partner in the last 6 months?'),
           ('Is your nose or the back of your throat itchy?'),
           ('Are you immunosuppressed?'),
           ('Have you had surgery within the last month?'),
           ('Do you have a chronic obstructive pulmonary disease (COPD)?'),
           ('Do you regularly take stimulant drugs?'),
           ('Are you exposed to secondhand cigarette smoke on a daily basis?'),
           ('Do you have heart failure?'),
           ('What color is the rash?'),
           ('Have you ever had a diagnosis of anemia?'),
           ('Where is the swelling located?'),
           ('Have you ever had a sexually transmitted infection?'),
           ('Where is the affected region located?'),
           ('Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for?'),
           ('Have you started or taken any antipsychotic medication within the last 7 days?'),
           ('Do you have pain somewhere, related to your reason for consulting?'),
           ('Do you have severe itching in one or both eyes?'),
           ('Are your vaccinations up to date?')
               )
    ORDER BY
        p.patient_id, e.question_text;
END //

DELIMITER ;

CALL GetPatientData() ;
DROP PROCEDURE IF EXISTS GetPatientData;

