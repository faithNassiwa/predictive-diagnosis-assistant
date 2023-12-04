# A Predictive Diagnosis Assistant in an Electronic Medical Records Platform
The Predictive Diagnosis Assistant is a tool designed to expedite and streamline doctors’ diagnostic process.

## Summary
The Predictive Diagnosis Assistant is a tool designed to expedite and streamline doctors’ diagnostic process which can sometimes devolve into trial and error, especially when patients present symptoms common to multiple diseases. This uncertainty often results in misdiagnoses, leading both patients and facilities to incur unnecessary costs and waste time on unneeded medical procedures, such as laboratory tests and medications. Our project aims to develop a platform where symptoms entered from patient records are used to predict possible diseases or conditions which will provide a starting point for healthcare providers to make a comprehensive review of the patient’s symptoms and make the best diagnosis. 

The main dataset to be utilized comprises diagnoses, symptoms and patient records. Our approach involves training and testing multinomial classification models to predict possible diseases based on entered symptoms and integrate the best-performing model into an Electronic Medical Records (EMR) platform that will be hosted on a cloud server.  

Ultimately, the overarching goal is to enhance patient care. By providing doctors with a tool that accelerates the diagnostic process, offers data-backed insights and data driven decisions, the project contributes to better patient outcomes, faster treatment and improved services.   

[Pitch Deck](https://docs.google.com/presentation/d/1o0y3Os1FTEI1bSuc0_SHDHiaDXHbOl9T7HqM-yHe5WU/edit#slide=id.p)

## Features
* Pre-trained XGBoost Models for predicting top 10 diseases and 49 diseases
* View 1000 patient records with their corresponding disease predictions, pagination set to 20 rows. 
* Run adhoc predictions 

## Usage 
### Installation
* Clone or download the project directory from github to your computer: run in the terminal `git clone https://github.com/faithNassiwa/predictive-diagnosis-assistant.git `
* Open the downloaded folder(predictive-diagnosis-assistant) in your favorite IDE or terminal.
* Install the require modules/packages:  run in the terminal `pip install requirements.txt`


### Database Set-up

### Access the Web Application 
* To open the web application: run in the terminal `streamlit run Home.py`
* Navigate to the application in the web browser 

## Future Work


