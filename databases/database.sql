DROP DATABASE IF EXISTS PROJECT;
CREATE DATABASE  Project;
USE Project;

SET global local_infile = 1;


DROP TABLE IF EXISTS patient;
CREATE TABLE patient (
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
    gender VARCHAR(2),
    age INT
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_table.csv'
into table patient
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS diseases;
CREATE TABLE diseases (
    disease_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_name VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/diseases.csv'
into table diseases
fields terminated by ',' enclosed by '"'
ignore 1 lines;

 DROP TABLE IF EXISTS evidence;
 CREATE TABLE evidence (
    evidence_id VARCHAR(255) PRIMARY KEY,
    question_text VARCHAR(255) -- The question asked to the patient
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/evidence.csv'
into table evidence
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS patient_evidence;
CREATE TABLE patient_evidence (
    patient_id INT,
    evidence_id VARCHAR(255),
    PRIMARY KEY (patient_id, evidence_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (evidence_id) REFERENCES evidence(evidence_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_evidence.csv'
into table patient_evidence
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS prediction;
CREATE TABLE prediction (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    disease_id INT,
    confidence_score FLOAT,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/prediction_table.csv'
into table prediction
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS characterize_pain;
CREATE TABLE characterize_pain (
	type_pain_id INT AUTO_INCREMENT PRIMARY KEY,
    type_pain VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/characterize_pain.csv'
into table characterize_pain
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS where_pain;
CREATE TABLE where_pain (
	where_pain_id INT AUTO_INCREMENT PRIMARY KEY,
    where_pain VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/where_pain.csv'
into table where_pain
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS traveled;
CREATE TABLE traveled (
	traveled_id INT AUTO_INCREMENT PRIMARY KEY,
    traveled VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/traveled.csv'
into table traveled
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS color_rash;
CREATE TABLE color_rash (
	color_rash_id INT AUTO_INCREMENT PRIMARY KEY,
    color_rash VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/color_rash.csv'
into table color_rash
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS peel_off;
CREATE TABLE peel_off (
	peel_off_id INT AUTO_INCREMENT PRIMARY KEY,
    peel_off_1cm VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/peel_off.csv'
into table peel_off
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS lesion_larger_1cm;
CREATE TABLE lesion_larger_1cm (
	lesion_larger_1cm_id INT AUTO_INCREMENT PRIMARY KEY,
    lesion_larger_1cm VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_lesion_larger_1cm.csv'
into table lesion_larger_1cm
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS where_swelling;
CREATE TABLE where_swelling (
	where_swelling_id INT AUTO_INCREMENT PRIMARY KEY,
    where_swelling_1cm VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/where_swelling.csv'
into table where_swelling
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS pain_radiate;
CREATE TABLE pain_radiate (
	pain_radiate_id INT AUTO_INCREMENT PRIMARY KEY,
    pain_radiate VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/pain_radiate.csv'
into table pain_radiate
fields terminated by ',' enclosed by '"'
ignore 1 lines;

DROP TABLE IF EXISTS affected_region;
CREATE TABLE affected_region (
	affected_region_id INT AUTO_INCREMENT PRIMARY KEY,
    affected_region VARCHAR(255),
    count_ INT,
    evidence VARCHAR(255)

);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/affected_region.csv'
into table affected_region
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientPainRelation (
    patient_id INT,
    type_pain_id INT,
    PRIMARY KEY (patient_id, type_pain_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (type_pain_id) REFERENCES characterize_pain(type_pain_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_characterize_pain.csv'
into table PatientPainRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientPainSomewhereRelation (
    patient_id INT,
    where_pain_id INT,
    PRIMARY KEY (patient_id, where_pain_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (where_pain_id) REFERENCES where_pain(where_pain_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_pain_somewhere.csv'
into table PatientPainSomewhereRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientTravelRelation (
    patient_id INT,
    traveled_id INT,
    PRIMARY KEY (patient_id, traveled_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (traveled_id) REFERENCES traveled(traveled_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_traveled.csv'
into table PatientTravelRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientColorRashRelation (
    patient_id INT,
    color_rash_id INT,
    PRIMARY KEY (patient_id, color_rash_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (color_rash_id) REFERENCES color_rash(color_rash_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_color_rash.csv'
into table PatientColorRashRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientPeelOffRelation (
    patient_id INT,
    peel_off_id INT,
    PRIMARY KEY (patient_id, peel_off_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (peel_off_id) REFERENCES peel_off(peel_off_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_lesion_peel_off.csv'
into table PatientPeelOffRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientLesionLarger1cmRelation (
    patient_id INT,
    lesion_larger_1cm_id INT,
    PRIMARY KEY (patient_id, lesion_larger_1cm_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (lesion_larger_1cm_id) REFERENCES lesion_larger_1cm(lesion_larger_1cm_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_lesion_larger_1cm.csv'
into table PatientLesionLarger1cmRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE Patientwhere_swellingRelation (
    patient_id INT,
    where_swelling_id INT,
    PRIMARY KEY (patient_id, where_swelling_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (where_swelling_id) REFERENCES where_swelling(where_swelling_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_swelling_located.csv'
into table Patientwhere_swellingRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientPainRadiateRelation (
    patient_id INT,
    pain_radiate_id INT,
    PRIMARY KEY (patient_id, pain_radiate_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (pain_radiate_id) REFERENCES pain_radiate(pain_radiate_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_pain_radiate.csv'
into table PatientPainRadiateRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;

CREATE TABLE PatientAffectedRegionRelation (
    patient_id INT,
    affected_region_id INT,
    PRIMARY KEY (patient_id, affected_region_id),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (affected_region_id) REFERENCES affected_region(affected_region_id)
);

load data local infile '/Users/grazianoperegrino/Desktop/Project /tables/patient_affected_region.csv'
into table PatientAffectedRegionRelation
fields terminated by ',' enclosed by '"'
ignore 1 lines;
